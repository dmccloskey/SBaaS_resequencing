from copy import copy
#sbaas lims
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#sbaas
from .stage01_resequencing_endpoints_dependencies import stage01_resequencing_endpoints_dependencies
from .stage01_resequencing_endpoints_io import stage01_resequencing_endpoints_io
from .stage01_resequencing_gd_query import stage01_resequencing_gd_query
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
#sbaas models
from .stage01_resequencing_endpoints_postgresql_models import *
#resources
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_interface import calculate_interface

class stage01_resequencing_endpoints_execute(stage01_resequencing_endpoints_io,
                                             stage01_resequencing_endpoints_dependencies,
                                           lims_biologicalMaterial_query,
                                           stage01_resequencing_gd_query,
                                           stage01_resequencing_analysis_query):


    def execute_analyzeEndpointReplicates_population(self,analysis_id_I=None,experiment_id=None,end_points=None):
        '''Analyze a endpoint replicates to identify the following:
        1. conserved mutations among replicates
        2. unique mutations among replicates
        Input:
           experiment_id = experiment id
           end_points = {analysis_id: [sample_name_1,sample_name_2,sample_name_3,...]}
        Output:
        '''
        #TODO: drive from analysis table

        print('Executing analyzeEndpointReplicates_population...')

        # get the analysis info
        analysis_info = [];
        analysis_info = self.get_rows_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);

        # get the experiments and strains
        analysis_id = analysis_id_I;
        experiment_ids = [];
        strains = [];
        for row in analysis_info:
            experiment_ids.append(row['experiment_id'])
            strains.append(row['sample_name'])

        # get the data
        data_O = [];
        analyzed_strain1 = []; # strain1s that have been analyzed
        analyzed_mutation_pairs = []; # mutation pairs that have been analyzed
        matched_mutations = {};
        for cnt1,strain1 in enumerate(strains):
            # query strain 1 data:
            strain1_mutations = [];
            strain1_mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_ids[cnt1],strain1);
            analyzed_strain1.append(strain1);
            analyzed_strain1_mutations = []; # mutations from strain 1 that have been analyzed
            analyzed_strain2_mutations_all = []; # all mutations from strain 2 that have been analyzed
            strain2_cnt = 0;
            for cnt2,strain2 in enumerate(strains):
                if strain2 == strain1: continue; # do not compare the same strain to itself
                print('comparing ' + strain1 + ' to ' + strain2);
                # query strain 1 data:
                strain2_mutations = [];
                strain2_mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_ids[cnt2],strain2);
                analyzed_strain2_mutations = []; # mutations from strain 2 that have been analyzed
                # extract common mutations
                analyzed_strain1_mutations_tmp = [];
                analyzed_strain2_mutations_tmp = [];
                matched_mutations_tmp = {}
                data_tmp = [];
                matched_mutations_tmp,\
                    analyzed_strain1_mutations_tmp,\
                    analyzed_strain2_mutations_tmp,\
                    data_tmp = self._extract_commonMutations(matched_mutations,\
                        analyzed_strain1_mutations,\
                        analyzed_strain2_mutations,\
                        strain1_mutations,strain2_mutations,
                        strain1,strain2_cnt,analysis_id);
                
                analyzed_strain1_mutations.extend(analyzed_strain1_mutations_tmp)
                analyzed_strain2_mutations.extend(analyzed_strain2_mutations_tmp)
                analyzed_strain2_mutations_all.append(analyzed_strain2_mutations);
                matched_mutations.update(matched_mutations_tmp);
                data_O.extend(data_tmp);
                strain2_cnt += 1;
            # extract unique mutations
            data_tmp = [];
            data_tmp = self._extract_uniqueMutations(analyzed_strain1_mutations,analyzed_strain2_mutations_all,strain1_mutations,analysis_id);
            data_O.extend(data_tmp);
        for d in data_O:
            row = [];
            row = data_stage01_resequencing_endpoints(d['experiment_id'],
                #TODO: test
                d['endpoint_name'], #=analysis_id
                #d['analysis_id'],
                d['sample_name'],
                d['mutation_frequency'],
                d['mutation_type'],
                d['mutation_position'],
                d['mutation_data'],
                #json.dumps(d['mutation_data'],
                d['isUnique'],
                None,None,None,None,None);
            self.session.add(row);
        self.session.commit();
    def execute_annotateMutations_endpoints(self,analysis_id_I,
                                                 ref_genome_I='data/U00096.2.gb',
                                                 ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        genomeannotation = genome_annotations(record_I=ref_genome_I,ref_I=ref_I);

        print('Executing annotateMutations_endpoints...')
        data_O = [];
        ## query sample names from the experiment
        #if sample_names_I:
        #    sample_names = sample_names_I;
        #else:
        #    sample_names = [];
        #    sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingEndpoints(experiment_id);
        #for sn in sample_names:
        

        # get the analysis info
        analysis_info = [];
        analysis_info = self.get_rows_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);

        # get the experiments and strains
        analysis_id = analysis_id_I;
        experiment_ids = [];
        sample_names = [];
        for row in analysis_info:
            experiment_ids.append(row['experiment_id'])
            sample_names.append(row['sample_name'])
        for cnt,sn in enumerate(sample_names):
            print('annotating mutation for sample_name ' + sn);
            # query rows that match the sample name
            rows = [];
            rows = self.get_row_experimentIDAndSampleName_dataStage01ResequencingEndpoints(experiment_ids[cnt],sn);
            for row in rows:
                # annotate each mutation based on the position
                annotation = {};
                annotation = genomeannotation._find_genesFromMutationPosition(row['mutation_data']['position']);
                row['mutation_genes'] = annotation['gene']
                row['mutation_locations'] = annotation['location']
                row['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                row['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                            row['mutation_links'].append(ecogene_link)
                        else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                data_O.append(row);
        # update rows in the database
        self.update_dataStage01ResequencingEndpoints(data_O);