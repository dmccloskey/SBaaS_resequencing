#sbaas
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_mutations_postgresql_models import *
from sequencing_analysis.genome_diff import genome_diff

class stage01_resequencing_mutations_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {
            'data_stage01_resequencing_mutationsAnnotated':data_stage01_resequencing_mutationsAnnotated,
            'data_stage01_resequencing_mutationsSeqChanges':data_stage01_resequencing_mutationsSeqChanges,
            'data_stage01_resequencing_mutationsCodonChanges':data_stage01_resequencing_mutationsCodonChanges,
                        };
        self.set_supportedTables(tables_supported);
    def reset_dataStage01_mutations(self,
            tables_I = [],
            experiment_id_I = None,
            warn_I=True):
        try:
            querydelete = sbaas_base_query_delete(session_I=self.session,engine_I=self.engine,settings_I=self.settings,data_I=self.data);
            for table in tables_I:
                query = {};
                query['delete_from'] = [{'table_name':table}];
                query['where'] = [{
                        'table_name':table,
                        'column_name':'experiment_id',
                        'value':experiment_id_I,
		                'operator':'LIKE',
                        'connector':'AND'
                        }
	                ];
                table_model = self.convert_tableStringList2SqlalchemyModelDict([table]);
                query = querydelete.make_queryFromString(table_model,query);
                querydelete.reset_table_sqlalchemyModel(query_I=query,warn_I=warn_I);
        except Exception as e:
            print(e);

    # query data from data_stage01_resequencing_mutationsAnnotated
    def get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation data'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I),
                    data_stage01_resequencing_mutationsAnnotated.used_).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_position.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_type.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_frequency.asc()).all();
            data_O = [];
            for d in data: 
                data_dict = {'experiment_id':d.experiment_id,
                            'sample_name':d.sample_name,
                            'mutation_frequency':d.mutation_frequency,
                            'mutation_type':d.mutation_type,
                            'mutation_position':d.mutation_position,
                            'mutation_data':d.mutation_data,
                            'mutation_annotations':d.mutation_annotations,
                            'mutation_genes':d.mutation_genes,
                            'mutation_locations':d.mutation_locations,
                            'mutation_links':d.mutation_links,
                            'used_':d.used_,
                            'comment_':d.comment_};
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query mutation information from data_stage01_resequencing_mutationsAnnotated
    def get_mutationData_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation information from resequencing lineage'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_tmp_str = '';
                mutation_genes_str = '';
                for gene in d.mutation_genes:
                    mutation_genes_str = mutation_genes_str + gene + '-/-'
                mutation_genes_str = mutation_genes_str[:-3];
                data_tmp_str = d.mutation_type+'_'+mutation_genes_str+'_'+str(d.mutation_position)
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query column queries from data_stage01_resequencing_mutationsAnnotated
    def get_mutationGenes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation genes from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_genes).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).group_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes.asc()).all();
            data_O = [];
            genomediff = genome_diff();
            for cnt,d in enumerate(data): 
                data_tmp_str = genomediff._make_mutationGenesStr(d.mutation_genes)
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_mutationTypes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_types from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_type).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).group_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_type).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_type.asc()).all();
            data_O = [];
            for cnt,d in enumerate(data): 
                data_O.append(d.mutation_type);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_mutationPositions_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_positions from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_position).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).group_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_position).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_position.asc()).all();
            data_O = [];
            for cnt,d in enumerate(data): 
                data_O.append(d.mutation_position);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_mutationLocations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_locations from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_locations).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).group_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_locations).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_locations.asc()).all();
            data_O = [];
            for cnt,d in enumerate(data): 
                data_O.append(d.mutation_locations);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_mutationIDs_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation genes from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_genes,
                    data_stage01_resequencing_mutationsAnnotated.mutation_type,
                    data_stage01_resequencing_mutationsAnnotated.mutation_position).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).group_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes,
                    data_stage01_resequencing_mutationsAnnotated.mutation_type,
                    data_stage01_resequencing_mutationsAnnotated.mutation_position).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_type.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_position.asc()).all();
            data_O = [];
            genomediff = genome_diff();
            for cnt,d in enumerate(data): 
                data_tmp_str = genomediff._make_mutationID(d.mutation_genes,d.mutation_type,d.mutation_position);
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);        
    def get_AllMutationGenes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation genes from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_genes).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes.asc()).all();
            data_O = [];
            genomediff = genome_diff();
            for cnt,d in enumerate(data): 
                data_tmp_str = genomediff._make_mutationGenesStr(d.mutation_genes)
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_AllMutationTypes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_types from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_type).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_type.asc()).all();
            data_O = [];
            for cnt,d in enumerate(data): 
                data_O.append(d.mutation_type);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_AllMutationPositions_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_positions from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_position).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_position.asc()).all();
            data_O = [];
            for cnt,d in enumerate(data): 
                data_O.append(d.mutation_position);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_AllMutationLocations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_locations from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_locations).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_locations.asc()).all();
            data_O = [];
            genomediff = genome_diff();
            for cnt,d in enumerate(data): 
                data_tmp_str = genomediff._make_mutationLocationsStr(d.mutation_locations);
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_AllMutationIDs_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation genes from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_genes,
                    data_stage01_resequencing_mutationsAnnotated.mutation_type,
                    data_stage01_resequencing_mutationsAnnotated.mutation_position).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_genes.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_type.asc(),
                    data_stage01_resequencing_mutationsAnnotated.mutation_position.asc()).all();
            data_O = [];
            genomediff = genome_diff();
            for cnt,d in enumerate(data): 
                data_tmp_str = genomediff._make_mutationID(d.mutation_genes,d.mutation_type,d.mutation_position);
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_AllMutationFrequencies_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation_frequency from data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated.mutation_frequency).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsAnnotated.mutation_frequency.asc()).all();
            data_O = [];
            for cnt,d in enumerate(data): 
                data_O.append(d.mutation_frequency);
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_resequencing_mutationsSeqChanges
    def get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsSeqChanges(self,experiment_id_I,sample_name_I):
        '''Query mutation data'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsSeqChanges).filter(
                    data_stage01_resequencing_mutationsSeqChanges.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsSeqChanges.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = d.__repr__dict__();
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_resequencing_mutationsSeqChanges and data_stage01_resequencing_mutationsAnnotated
    def get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsSeqChangesAndAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation data from join of data_stage01_resequencing_mutationsSeqChanges and data_stage01_resequencing_mutationsAnnotated'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsSeqChanges.experiment_id,
                    data_stage01_resequencing_mutationsSeqChanges.sample_name,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_frequency,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_type,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_position,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_genes,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_locations,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_data,
                    data_stage01_resequencing_mutationsAnnotated.mutation_annotations,
                    data_stage01_resequencing_mutationsAnnotated.mutation_links,
                    data_stage01_resequencing_mutationsSeqChanges.dna_sequence_ref,
                    data_stage01_resequencing_mutationsSeqChanges.dna_sequence_new,
                    data_stage01_resequencing_mutationsSeqChanges.rna_sequence_ref,
                    data_stage01_resequencing_mutationsSeqChanges.rna_sequence_new,
                    data_stage01_resequencing_mutationsSeqChanges.peptide_sequence_ref,
                    data_stage01_resequencing_mutationsSeqChanges.peptide_sequence_new,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_class,
                    data_stage01_resequencing_mutationsSeqChanges.dna_features_region,
                    data_stage01_resequencing_mutationsSeqChanges.rna_features_region,
                    data_stage01_resequencing_mutationsSeqChanges.peptide_features_region,
                    data_stage01_resequencing_mutationsSeqChanges.dna_feature_position,
                    data_stage01_resequencing_mutationsSeqChanges.dna_feature_ref,
                    data_stage01_resequencing_mutationsSeqChanges.dna_feature_new,
                    data_stage01_resequencing_mutationsSeqChanges.rna_feature_position,
                    data_stage01_resequencing_mutationsSeqChanges.rna_feature_ref,
                    data_stage01_resequencing_mutationsSeqChanges.rna_feature_new,
                    data_stage01_resequencing_mutationsSeqChanges.peptide_feature_position,
                    data_stage01_resequencing_mutationsSeqChanges.peptide_feature_ref,
                    data_stage01_resequencing_mutationsSeqChanges.peptide_feature_new,
                    data_stage01_resequencing_mutationsSeqChanges.used_,
                    data_stage01_resequencing_mutationsSeqChanges.comment_).filter(
                    data_stage01_resequencing_mutationsSeqChanges.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsSeqChanges.sample_name.like(sample_name_I),
                    data_stage01_resequencing_mutationsSeqChanges.experiment_id.like(data_stage01_resequencing_mutationsAnnotated.experiment_id),
                    data_stage01_resequencing_mutationsSeqChanges.sample_name.like(data_stage01_resequencing_mutationsAnnotated.sample_name),
                    data_stage01_resequencing_mutationsSeqChanges.mutation_type.like(data_stage01_resequencing_mutationsAnnotated.mutation_type),
                    data_stage01_resequencing_mutationsSeqChanges.mutation_position==data_stage01_resequencing_mutationsAnnotated.mutation_position,
                    data_stage01_resequencing_mutationsSeqChanges.mutation_genes==data_stage01_resequencing_mutationsAnnotated.mutation_genes).all()
            #group_by(
            #        data_stage01_resequencing_mutationsSeqChanges.experiment_id,
            #        data_stage01_resequencing_mutationsSeqChanges.sample_name,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_frequency,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_type,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_position,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_genes,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_locations,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_data,
            #        data_stage01_resequencing_mutationsAnnotated.mutation_annotations,
            #        data_stage01_resequencing_mutationsAnnotated.mutation_links,
            #        data_stage01_resequencing_mutationsSeqChanges.dna_sequence_ref,
            #        data_stage01_resequencing_mutationsSeqChanges.dna_sequence_new,
            #        data_stage01_resequencing_mutationsSeqChanges.rna_sequence_ref,
            #        data_stage01_resequencing_mutationsSeqChanges.rna_sequence_new,
            #        data_stage01_resequencing_mutationsSeqChanges.peptide_sequence_ref,
            #        data_stage01_resequencing_mutationsSeqChanges.peptide_sequence_new,
            #        data_stage01_resequencing_mutationsSeqChanges.mutation_class,
            #        data_stage01_resequencing_mutationsSeqChanges.dna_features_region,
            #        data_stage01_resequencing_mutationsSeqChanges.rna_features_region,
            #        data_stage01_resequencing_mutationsSeqChanges.peptide_features_region,
            #        data_stage01_resequencing_mutationsSeqChanges.dna_feature_position,
            #        data_stage01_resequencing_mutationsSeqChanges.dna_feature_ref,
            #        data_stage01_resequencing_mutationsSeqChanges.dna_feature_new,
            #        data_stage01_resequencing_mutationsSeqChanges.rna_feature_position,
            #        data_stage01_resequencing_mutationsSeqChanges.rna_feature_ref,
            #        data_stage01_resequencing_mutationsSeqChanges.rna_feature_new,
            #        data_stage01_resequencing_mutationsSeqChanges.peptide_feature_position,
            #        data_stage01_resequencing_mutationsSeqChanges.peptide_feature_ref,
            #        data_stage01_resequencing_mutationsSeqChanges.peptide_feature_new,
            #        data_stage01_resequencing_mutationsSeqChanges.used_,
            #        data_stage01_resequencing_mutationsSeqChanges.comment_).all();
            data_O = [];
            for d in data: 
                data_dict = {
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'mutation_frequency':d.mutation_frequency,
                'mutation_type':d.mutation_type,
                'mutation_position':d.mutation_position,
                'mutation_genes':d.mutation_genes,
                'mutation_locations':d.mutation_locations,
                'mutation_data':d.mutation_data,
                'mutation_annotations':d.mutation_annotations,
                'mutation_links':d.mutation_links,
                'dna_sequence_ref':d.dna_sequence_ref,
                'dna_sequence_new':d.dna_sequence_new,
                'rna_sequence_ref':d.rna_sequence_ref,
                'rna_sequence_new':d.rna_sequence_new,
                'peptide_sequence_ref':d.peptide_sequence_ref,
                'peptide_sequence_new':d.peptide_sequence_new,
                'mutation_class':d.mutation_class,
                'dna_features_region':d.dna_features_region,
                'rna_features_region':d.rna_features_region,
                'peptide_features_region':d.peptide_features_region,
                'dna_feature_position':d.dna_feature_position,
                'dna_feature_ref':d.dna_feature_ref,
                'dna_feature_new':d.dna_feature_new,
                'rna_feature_position':d.rna_feature_position,
                'rna_feature_ref':d.rna_feature_ref,
                'rna_feature_new':d.rna_feature_new,
                'peptide_feature_position':d.peptide_feature_position,
                'peptide_feature_ref':d.peptide_feature_ref,
                'peptide_feature_new':d.peptide_feature_new,
                'used_':d.used_,
                'comment_':d.comment_}
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query specific columns from data_stage01_resequencing_mutationsSeqChanges
    def get_allMutationClasses_experimentIDAndSampleName_dataStage01ResequencingMutationsSeqChanges(self,experiment_id_I,sample_name_I):
        '''Query mutation data'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsSeqChanges.mutation_class).filter(
                    data_stage01_resequencing_mutationsSeqChanges.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsSeqChanges.sample_name.like(sample_name_I)).order_by(
                    data_stage01_resequencing_mutationsSeqChanges.mutation_class.asc()).all();
            data_O = [];
            genomediff = genome_diff();
            for d in data: 
                data_tmp_str = genomediff._make_mutationClassStr(d.mutation_class);
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);