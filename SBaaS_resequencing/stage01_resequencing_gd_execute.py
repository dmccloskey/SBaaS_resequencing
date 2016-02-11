'''resequencing class'''
from copy import copy
#sbaas lims
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#SBaaS models
from SBaaS_models.models_COBRA_query import models_COBRA_query
#sbaas
from .stage01_resequencing_gd_io import stage01_resequencing_gd_io
#sbaas models
from .stage01_resequencing_gd_postgresql_models import *
#resources
from sequencing_analysis.genome_diff import genome_diff
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_interface import calculate_interface

class stage01_resequencing_gd_execute(stage01_resequencing_gd_io,
                                      lims_biologicalMaterial_query,
                                      models_COBRA_query):
    
    #Analysis
    def execute_filterMutations_population(self,experiment_id,p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1,sample_names_I=None):
        '''Filter mutations that do not meet the desired criteria
        INPUT:
        experiment_id = string
        p_value_criteria = float, minimum breseq p-value
        quality_criteria = float, minimum breseq quality score
        frequency_criteria = float, minimum breseq frequency of mutation in the population
        sample_names_I = [] of strings, specific sample names to use in the experiment
        '''

        print('Executing filterMutations_population...')
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingMetadata(experiment_id);
        for sn in sample_names:
            print('Filtering mutations for sample_name ' + sn);
            #query mutation data filtered by frequency
            data_mutations_list = [];
            data_mutations_list = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutations(experiment_id,sn,frequency_criteria=frequency_criteria);
            for data_mutations in data_mutations_list:
                print('Filtering mutations for mutation id ' + str(data_mutations['mutation_id']));
                #query data filtered by evidence-specific criteria
                data_evidence_list = [];
                for pid in data_mutations['parent_ids']:
                    print('Filtering mutations for parent id ' + str(pid));
                    data_evidence_dict = {};
                    data_evidence_dict = self.get_evidence_experimentIDAndSampleNameAndParentID_dataStage01ResequencingEvidence(experiment_id,sn,pid,
                                                    p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria);
                    data_evidence_list.append(data_evidence_dict);
                if data_evidence_list[0]: #check that filtered evidence was found
                    data_O.append(data_mutations);
        #add data to the database table
        self.add_dataStage01ResequencingMutationsFiltered(data_O);
    def execute_annotateFilteredMutations(self,experiment_id,sample_names_I=[],
                                                 annotation_I='data/U00096.2.gb',
                                                 annotation_ref_I = 'genbank',
                                                 biologicalmaterial_id_I='MG1655',
                                                 ):
        '''Annotate filtered mutations using a reference annotation
        INPUT:
        experiment_id = string
        sample_names_I = [] of strings
        annotation_I = string, reference file for the sequencing annotation
        annotation_ref_I = string, reference file data base source
        biologicalmaterial_id_I = string
        '''

        genomeannotation = genome_annotations(annotation_I=annotation_I,annotation_ref_I=annotation_ref_I);

        print('Executing annotation of filtered mutations...')
        genotype_phenotype_O = [];
        # query sample names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingMutationsFiltered(experiment_id);
        for sn in sample_names:
            print('analyzing sample_name ' + sn);
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,sn);
            mutation_data_O = [];
            for end_cnt,mutation in enumerate(mutations):
                print('analyzing mutations')
                data_tmp = {};
                # annotate each mutation based on the position
                annotation = {};
                annotation = genomeannotation._find_genesFromMutationPosition(mutation['mutation_data']['position']);
                data_tmp['mutation_genes'] = annotation['gene']
                data_tmp['mutation_locations'] = annotation['location']
                data_tmp['mutation_annotations'] = annotation['product']
                # generate a link to ecogene for the genes
                data_tmp['mutation_links'] = [];
                for bnumber in annotation['locus_tag']:
                    if bnumber:
                        ecogenes = [];
                        ecogenes = self.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                        if ecogenes:
                            ecogene = ecogenes[0];
                            ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                            data_tmp['mutation_links'].append(ecogene_link)
                        else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                data_tmp['experiment_id'] = mutation['experiment_id'];
                data_tmp['sample_name'] = mutation['sample_name'];
                frequency = 1.0;
                if 'frequency' in mutation['mutation_data']:
                    frequency = mutation['mutation_data']['frequency'];
                data_tmp['mutation_frequency'] = frequency
                data_tmp['mutation_position'] = mutation['mutation_data']['position']
                data_tmp['mutation_type'] = mutation['mutation_data']['type']
                data_tmp['mutation_data'] = mutation['mutation_data'];
                mutation_data_O.append(data_tmp);
                # add data to the database
                row = [];
                row = data_stage01_resequencing_mutationsAnnotated(data_tmp['experiment_id'],
                        data_tmp['sample_name'],
                        data_tmp['mutation_frequency'],
                        data_tmp['mutation_type'],
                        data_tmp['mutation_position'],
                        data_tmp['mutation_data'],
                        data_tmp['mutation_annotations'],
                        data_tmp['mutation_genes'],
                        data_tmp['mutation_locations'],
                        data_tmp['mutation_links'],
                        True,
                        None);
                self.session.add(row);
        self.session.commit();
    def execute_mutateFilteredMutations(self,experiment_id,sample_names_I=[],
                                                 annotation_I='data/U00096.2.gb',
                                                 annotation_ref_I = 'genbank',
                                                 sequence_I='data/U00096.2.fas',
                                                 sequence_ref_I = 'fasta',
                                                IS_sequences_I='data/ecoli_IS_sequences.fasta',
                                                IS_sequences_ref_I = 'fasta',
                                                 translation_table_I='Bacterial',
                                                 ):
        '''Mutate filtered mutations to determine the change in dna, rna, and peptide sequences
        INPUT:
        experiment_id = string
        sample_names_I = [] of strings
        annotation_I = string, reference file for the sequencing annotation
        annotation_ref_I = string, reference file data base source
        sequence_I = string, reference file for the sequence
        sequence_I = string, reference file format
        IS_sequences_I = string, reference file for the insertion element sequences
        IS_sequences_I = string, reference file format
        translation_table_I = string, translation table to use when converting from rna to peptide sequence
        '''

        genomeannotation = genome_annotations(annotation_I=annotation_I,annotation_ref_I=annotation_ref_I,
                                              sequence_I=sequence_I,sequence_ref_I=sequence_ref_I,
                                              IS_sequences_I=IS_sequences_I,IS_sequences_ref_I=IS_sequences_ref_I);

        print('Executing annotation of filtered mutations...')
        data_O = [];
        # query sample names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingMutationsFiltered(experiment_id);
        for sn in sample_names:
            print('analyzing sample_name ' + sn);
            data_O = [];
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(experiment_id,sn);
            for end_cnt,mutation in enumerate(mutations):
                print('analyzing mutations')
                data_tmp = {};
                # annotate each mutation based on the position
                annotation = {};
                annotation = genomeannotation._mutate_peptideFromMutationData(mutation['mutation_data'],translation_table_I=translation_table_I);
                if not annotation['gene']: continue;
                data_tmp['mutation_genes'] = annotation['gene']
                data_tmp['mutation_locations'] = annotation['location']
                data_tmp['mutation_data'] = annotation['mutation_data']
                data_tmp['dna_sequence_ref'] = annotation['dna_sequence_ref'];
                data_tmp['dna_sequence_new'] = annotation['dna_sequence_new'];
                data_tmp['rna_sequence_ref'] = annotation['rna_sequence_ref'];
                data_tmp['rna_sequence_new'] = annotation['rna_sequence_new'];
                data_tmp['peptide_sequence_ref'] = annotation['peptide_sequence_ref'];
                data_tmp['peptide_sequence_new'] = annotation['peptide_sequence_new'];
                data_tmp['mutation_class'] = annotation['mutation_class'];
                data_tmp['dna_feature_position'] = annotation['dna_feature_position']
                data_tmp['dna_feature_ref'] = annotation['dna_feature_ref']
                data_tmp['dna_feature_new'] = annotation['dna_feature_new']
                data_tmp['rna_feature_position'] = annotation['rna_feature_position']
                data_tmp['rna_feature_ref'] = annotation['rna_feature_ref']
                data_tmp['rna_feature_new'] = annotation['rna_feature_new']
                data_tmp['peptide_feature_position'] = annotation['peptide_feature_position']
                data_tmp['peptide_feature_ref'] = annotation['peptide_feature_ref']
                data_tmp['peptide_feature_new'] = annotation['peptide_feature_new']
                data_tmp['experiment_id'] = mutation['experiment_id'];
                data_tmp['sample_name'] = mutation['sample_name'];
                data_tmp['dna_features_region'] = None;
                data_tmp['rna_features_region'] = None;
                data_tmp['peptide_features_region'] = None;
                frequency = 1.0;
                if 'frequency' in mutation['mutation_data']:
                    frequency = mutation['mutation_data']['frequency'];
                data_tmp['mutation_frequency'] = frequency
                data_tmp['mutation_position'] = mutation['mutation_data']['position']
                data_tmp['mutation_type'] = mutation['mutation_data']['type']
                #data_tmp['mutation_data'] = mutation['mutation_data'];
                data_tmp['used_'] = True;
                data_tmp['comment_'] = None;
                data_O.append(data_tmp);
            #upload the data to the database (each sample)
            self.add_dataStage01ResequencingMutationsSeqChanges(data_O);

    def map_geneName2ModelReaction(self,
            biologicalmaterial_id_I,gene_name_I,
            model_id_I,):
        """return the model reaction rows whose enzymes are produced by a given gene
        INPUT:
        biologicalmaterial_id_I = string, e.g. MG1655
        gene_name_I = string, e.g. pgi
        model_id_I = string, e.g. iJO1366
        OUTPUT:
        rows_O = rows from data_stage02_physiology_modelReactions
        """

        rows_O = [];
        orderedLocusNames = [];
        orderedLocusNames = self.get_orderedLocusName_biologicalmaterialIDAndGeneName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,gene_name_I);
        for oln in orderedLocusNames:
            rows_tmp = [];
            rows_tmp = self.get_rows_modelIDAndOrderedLocusName_dataStage02PhysiologyModelReactions(model_id_I,oln['ordered_locus_name']);
            for r in rows_tmp:
                r['mutation_gene'] = gene_name_I;
                rows_O.append(r);
        return rows_O;

    def execute_mapGeneName2ModelReaction_mutationsAnnotated(self,
            experiment_id,filename_O,
            biologicalmaterial_id_I,
            model_id_I,
            sample_names_I=[],
            gene_names_I=[]):
        """return the model reaction rows whose enzymes are produced by a given gene
        INPUT:
        biologicalmaterial_id_I = string, e.g. MG1655
        gene_name_I = string, e.g. pgi
        model_id_I = string, e.g. iJO1366
        OUTPUT:
        filename_O = name of output file
                    rows from data_stage02_physiology_modelReactions in a .csv file
        """
        
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingMetadata(experiment_id);
        for sn in sample_names:
            #query the mutations from the experiment
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_id,sn);
            for mutation in mutations:
                for gene_name in mutation['mutation_genes']:
                    if gene_names_I:
                        if not gene_name in gene_names_I:
                            continue
                    rows = [];
                    rows = self.map_geneName2ModelReaction(
                                    biologicalmaterial_id_I,gene_name,
                                    model_id_I);
                    if rows:
                        for r in rows:
                            r['experiment_id']=mutation['experiment_id'];
                            r['sample_name']=mutation['sample_name'];
                            r['mutation_frequency']=mutation['mutation_frequency'];
                            r['mutation_type']=mutation['mutation_type'];
                            r['mutation_position']=mutation['mutation_position'];
                            r['mutation_data']=mutation['mutation_data'];
                            r['mutation_annotations']=mutation['mutation_annotations'];
                            r['mutation_genes']=mutation['mutation_genes'];
                            r['mutation_locations']=mutation['mutation_locations'];
                            r['mutation_links']=mutation['mutation_links'];
                            r['used_']=mutation['used_'];
                            r['comment_']=mutation['comment_'];
                            r['biologicalmaterial_id'] = biologicalmaterial_id_I;
                            r['model_id'] = model_id_I;
                            data_O.append(r);
        #export the data to .csv
        self.export_mapGeneName2ModelReaction_csv(data_O,filename_O);
