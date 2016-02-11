from copy import copy
#sbaas lims
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#sbaas
from .stage01_resequencing_lineage_io import stage01_resequencing_lineage_io
from .stage01_resequencing_gd_query import stage01_resequencing_gd_query
#sbaas models
from .stage01_resequencing_lineage_postgresql_models import *
#resources
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_interface import calculate_interface
from python_statistics.calculate_count import calculate_count

class stage01_resequencing_lineage_execute(stage01_resequencing_lineage_io,
                                           lims_biologicalMaterial_query,
                                           stage01_resequencing_gd_query):
    def execute_analyzeLineage_population(self,experiment_id,strain_lineage):
        '''Analyze a strain lineage to identify the following:
        1. conserved mutations
        2. changes in frequency of mutations
        3. hitch-hiker mutations

        Input:
           experiment_id = experiment id
           strain_lineage = {"lineage_name":{0:sample_name,1:sample_name,2:sample_name,...,n:sample_name}}
                               where n is the end-point strain
        Output:

        TODO: drive from analysis table
        TODO: convert time-point to lineage
               lineage = [i for i,tp in enumerate(time_points)];
        '''

        print('Executing analyzeLineage_population...')
        data_O = [];
        for lineage_name,strain in strain_lineage.items():
            print('analyzing lineage ' + lineage_name);
            lineage = list(strain.keys());
            end_point = max(lineage)
            # query end data:
            end_mutations = [];
            end_mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain[end_point]);
            intermediates = [i for i in lineage if i!=end_point];
            intermediate_mutations = [];
            for intermediate in intermediates:
                print('analyzing intermediate ' + str(intermediate));
                # query intermediate data:
                intermediate_mutations = [];
                intermediate_mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,strain[intermediate]);
                data_O.extend(self._extract_mutationsLineage(lineage_name,end_mutations,intermediate_mutations,intermediate,end_point));
        for d in data_O:
            row = [];
            row = data_stage01_resequencing_lineage(d['experiment_id'],
                d['lineage_name'],
                d['sample_name'],
                d['intermediate'],
                d['mutation_frequency'],
                d['mutation_type'],
                d['mutation_position'],
                d['mutation_data'],
                None,None,None,None,None);
            self.session.add(row);
        self.session.commit();
    def execute_annotateMutations_lineage(self,experiment_id,sample_names_I=[],
                                                 ref_genome_I='data/U00096.2.gb',
                                                 ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):
        '''Annotate mutations for date_stage01_resequencing_lineage
        based on position, reference genome, and reference genome biologicalmaterial_id'''

        genomeannotation = genome_annotations(annotation_I=ref_genome_I,annotation_ref_I=ref_I);

        print('Executing annotateMutations_lineage...')
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingLineage(experiment_id);
        for sn in sample_names:
            print('annotating mutation for sample_name ' + sn);
            # query rows that match the sample name
            rows = [];
            rows = self.get_row_experimentIDAndSampleName_dataStage01ResequencingLineage(experiment_id,sn);
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
        self.update_dataStage01ResequencingLineage(data_O);

