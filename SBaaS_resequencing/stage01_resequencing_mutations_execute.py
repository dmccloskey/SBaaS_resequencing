﻿'''resequencing class'''
from copy import copy
#sbaas lims
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#SBaaS models
from SBaaS_models.models_COBRA_query import models_COBRA_query
from SBaaS_models.models_BioCyc_execute import models_BioCyc_execute
#sbaas
from .stage01_resequencing_mutations_io import stage01_resequencing_mutations_io
#sbaas models
from .stage01_resequencing_mutations_postgresql_models import *
#resources
from sequencing_analysis.genome_diff import genome_diff
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_interface import calculate_interface

class stage01_resequencing_mutations_execute(stage01_resequencing_mutations_io,
                                      lims_biologicalMaterial_query,
                                      models_COBRA_query):
    #TODO:
    #1. add in query_object_I
    #2. add in query_func_I
    #3. add in query_object_annotation_I
    #4. add in query_object_annotation_func_I
    #5. split into queryData, transformData, storeData functions
    #6.
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
                data_tmp['mutation_chromosome'] = 1;
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
                                                 codonUsageTable_I='data/ecoli_codonUsageTable.csv',
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
        codonUsageTable_I = string, reference file for the codon usage table
        IS_sequences_I = string, reference file for the insertion element sequences
        IS_sequences_ref_I = string, reference file format
        translation_table_I = string, translation table to use when converting from rna to peptide sequence
        '''

        genomeannotation = genome_annotations(annotation_I=annotation_I,annotation_ref_I=annotation_ref_I,
                                              sequence_I=sequence_I,sequence_ref_I=sequence_ref_I,
                                              IS_sequences_I=IS_sequences_I,IS_sequences_ref_I=IS_sequences_ref_I,
                                              codonUsageTable_I=codonUsageTable_I);

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
            data_codon_O=[];
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
                #split into different tables depending on whether the peptide sequence changed
                if mutation['mutation_data']['type']=='SNP' and 'synonymous' in annotation['mutation_class']:
                    data_tmp['codon_triplet_ref'] = annotation['codon_triplet_ref'];
                    data_tmp['codon_triplet_new'] = annotation['codon_triplet_new'];
                    data_tmp['codon_triplet_position'] = annotation['codon_triplet_position']
                    data_tmp['codon_fraction_ref'] = annotation['codon_fraction_ref']
                    data_tmp['codon_fraction_new'] = annotation['codon_fraction_new']
                    data_tmp['codon_frequency_ref'] = annotation['codon_frequency_ref']
                    data_tmp['codon_frequency_new'] = annotation['codon_frequency_new']
                    data_tmp['codon_frequency_units'] = annotation['codon_frequency_units']
                    data_codon_O.append(data_tmp);
                else:
                    data_O.append(data_tmp);
            #upload the data to the database (each sample)
            if data_O:
                self.add_dataStage01ResequencingMutationsSeqChanges(data_O);
            if data_codon_O:
                self.add_rows_table('data_stage01_resequencing_mutationsCodonChanges',data_codon_O);

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

    def calculate_distributionOfMutationsInBioCycParentClasses(
        self,
        experiment_id_I,
        sample_names_I,
        parent_classes_I=['Transcription related'],
        database_I='ECOLI',
        names_I=[]
        ):
        '''calculate the percentages of mutations in each BioCyc parent_classes
        INPUT:
        '''
        #BioCyc dependencies
        biocyc01 = models_BioCyc_execute(self.session,self.engine,self.settings);
        biocyc01.initialize_supportedTables()
        biocyc01.initialize_tables()

        from SBaaS_models.models_BioCyc_dependencies import models_BioCyc_dependencies
        biocyc01_dep = models_BioCyc_dependencies();

        if parent_classes_I:
            parent_classes = parent_classes_I;
        else:
            parent_classes = [];
            parent_classes = biocyc01.getParsed_parentClasses_modelsBioCycPolymerSegments(
                database_I='ECOLI'
                );

        pc2Genes = {};
        for pc in parent_classes:
            #join list of genes with alternative identifiers
            biocyc_genes = biocyc01.getParsed_genesAndAccessionsAndSynonyms_namesAndParentClassesAndDatabase_modelsBioCycPolymerSegments(
                names_I=names_I,
                database_I=database_I,
                parent_classes_I='%s"%s"%s'%('%',pc,'%'),
                query_I={},
                output_O='listDict',
                dictColumn_I=None);
            if biocyc_genes:
                gene_ids = list(set([g['gene'] for g in biocyc_genes if g['gene']] +\
                    [g['common_name'] for g in biocyc_genes if g['common_name']] +\
                    [g['synonym'] for g in biocyc_genes if g['synonym']]));
                pc2Genes[pc] = gene_ids;

        #query all of the resequencing data
        mutations_rows = self.get_mutations_experimentIDAndSampleNames_dataStage01ResequencingMutationsAnnotated(
        experiment_id_I = experiment_id_I,
        sample_names_I = sample_names_I);
        mutated_genes = [];
        for row in mutations_rows:
            if row['mutation_genes']: #exclude non-annotated regions
                mutated_genes.extend(row['mutation_genes']);
        mutations_genes_cnt = len(list(set(mutated_genes)))

        #calculate the distributions for each parent_class
        data_O = [];
        for parent_class,gene_ids in pc2Genes.items():
            pc_genes_cnt = len(list(set([d for d in mutated_genes if d in gene_ids])))
            genes_ratio = pc_genes_cnt/mutations_genes_cnt;
            tmp = {'parent_class':parent_class,
                   'mutation_genes_count':mutations_genes_cnt,
                   'genes_count':pc_genes_cnt,
                   'genes_fraction':genes_ratio};
            data_O.append(tmp);

        return data_O;        
    def calculate_fractionOfMutationLocations(
        self,
        experiment_id_I,
        sample_names_I,
        mutation_locations_I = []
        ):
        '''calculate the percentages of mutations in each mutation_location
        INPUT:
        EXAMPLE:
        sample_names = '140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1,\
        140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1';
        mutation_locations_fractions = mut01.calculate_fractionOfMutationLocations(
            experiment_id_I = 'ALEsKOs01',
            sample_names_I = sample_names,);
        #export the data to disk
        from io_utilities.base_exportData import base_exportData
        iobase = base_exportData(parent_classes_fractions);
        iobase.write_dict2json(
            pg_settings.datadir_settings['workspace_data']+\
            '/_output/ALEsKOs01_0_11_parent_classes_fractions.json');
        iobase.write_dict2csv(
            pg_settings.datadir_settings['workspace_data']+\
            '/_output/ALEsKOs01_0_11_parent_classes_fractions.csv');
        '''


        #query all of the resequencing data
        mutations_rows = self.get_mutations_experimentIDAndSampleNames_dataStage01ResequencingMutationsAnnotated(
        experiment_id_I = experiment_id_I,
        sample_names_I = sample_names_I);

        mutation_locations = {};
        mutated_genes_coding = [];
        for row in mutations_rows:
            if row['mutation_genes'] : #exclude non-annotated regions
                mutated_genes.extend(row['mutation_genes']);
                if not row['mutation_location'] in mutation_locations:
                    mutation_locations[row['mutation_location']]= [];
                if mutation_locations_I and not row['mutation_location'] in mutation_locations_I:
                    continue;
                mutation_locations[row['mutation_location']].extend(row['mutation_genes'])
        mutations_genes_cnt = len(list(set(mutated_genes)))

        #calculate the distributions for each parent_class
        data_O = [];
        for parent_class,gene_ids in mutation_locations.items():
            pc_genes_cnt = len(list(set([d for d in mutated_genes if d in gene_ids])))
            genes_ratio = pc_genes_cnt/mutations_genes_cnt;
            tmp = {'parent_class':parent_class,
                   'mutation_genes_count':mutations_genes_cnt,
                   'genes_count':pc_genes_cnt,
                   'genes_fraction':genes_ratio};
            data_O.append(tmp);

        return data_O;


