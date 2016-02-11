#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_gd_postgresql_models import *
from sequencing_analysis.genome_diff import genome_diff

class stage01_resequencing_gd_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {
            'data_stage01_resequencing_metadata':data_stage01_resequencing_metadata,
            'data_stage01_resequencing_mutations':data_stage01_resequencing_mutations,
            'data_stage01_resequencing_mutationsAnnotated':data_stage01_resequencing_mutationsAnnotated,
            'data_stage01_resequencing_mutationsFiltered':data_stage01_resequencing_mutationsFiltered,
            'data_stage01_resequencing_mutationsSeqChanges':data_stage01_resequencing_mutationsSeqChanges,
            'data_stage01_resequencing_validation':data_stage01_resequencing_validation,
            'data_stage01_resequencing_evidence':data_stage01_resequencing_evidence,
                        };
        self.set_supportedTables(tables_supported);

    def drop_dataStage01_resequencing_gd(self):
        try:
            data_stage01_resequencing_evidence.__table__.drop(self.engine,True);
            data_stage01_resequencing_mutations.__table__.drop(self.engine,True);
            data_stage01_resequencing_metadata.__table__.drop(self.engine,True);
            data_stage01_resequencing_validation.__table__.drop(self.engine,True);
            data_stage01_resequencing_mutationsFiltered.__table__.drop(self.engine,True);
            data_stage01_resequencing_mutationsAnnotated.__table__.drop(self.engine,True);
            data_stage01_resequencing_mutationsSeqChanges.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

    def drop_dataStage01_resequencing_mutationsSeqChanges(self):
        try:
            data_stage01_resequencing_mutationsSeqChanges.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_gd(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_metadata).filter(data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).filter(data_stage01_resequencing_mutations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).filter(data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).filter(data_stage01_resequencing_validation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsSeqChanges).filter(data_stage01_resequencing_mutationsSeqChanges.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_metadata).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsSeqChanges).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_resequencing_gd(self):
        try:
            data_stage01_resequencing_metadata.__table__.create(self.engine,True);
            data_stage01_resequencing_mutations.__table__.create(self.engine,True);
            data_stage01_resequencing_evidence.__table__.create(self.engine,True);
            data_stage01_resequencing_validation.__table__.create(self.engine,True);
            data_stage01_resequencing_mutationsFiltered.__table__.create(self.engine,True);
            data_stage01_resequencing_mutationsAnnotated.__table__.create(self.engine,True);
            data_stage01_resequencing_mutationsSeqChanges.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_metadataAndmutationsAndEvidenceAndValidation(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_metadata).filter(data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).filter(data_stage01_resequencing_mutations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).filter(data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).filter(data_stage01_resequencing_validation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_metadata).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_filtered(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_mutationsSeqChanges(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_mutationsSeqChanges).filter(data_stage01_resequencing_mutationsSeqChanges.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_mutationsSeqChanges).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_mutationsAnnotated(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_mutationsAnnotated).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01ResequencingMutations(self, data_I):
        '''add rows of data_stage01_resequencing_mutations'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_mutations(d['experiment_id'],
                                    d['sample_name'],
                                    d['mutation_id'],
                                    d['parent_ids'],
                                    d['mutation_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingMutationsFiltered(self, data_I):
        '''add rows of data_stage01_resequencing_mutationsFiltered'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_mutationsFiltered(d['experiment_id'],
                                    d['sample_name'],
                                    d['mutation_id'],
                                    d['parent_ids'],
                                    d['mutation_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingMetadata(self, data_I):
        '''add rows of data_stage01_resequencing_metadata'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_metadata(d['experiment_id'],
                            d['sample_name'],
                            d['genome_diff'],
                            d['refseq'],
                            d['readseq'],
                            d['author']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingEvidence(self, data_I):
        '''add rows of data_stage01_resequencing_evidence'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_evidence(d['experiment_id'],
                        d['sample_name'],
                        d['parent_id'],
                        d['evidence_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingValidation(self, data_I):
        '''add rows of data_stage01_resequencing_validation'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_validation(d['experiment_id'],
                        d['sample_name'],
                        d['validation_id'],
                        d['validation_data']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingMetadata(self,data_I):
        '''update rows of dataStage01ResequencingMetadata'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_metadata).filter(
                            data_stage01_resequencing_metadata.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_diff':d['genome_diff'],
                            'refseq':d['refseq'],
                            'readseq':d['readseq'],
                            'author':d['author']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingMutations(self,data_I):
        '''update rows of dataStage01ResequencingMutations'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_mutations).filter(
                            data_stage01_resequencing_mutations.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'mutation_id':d['mutation_id'],
                            'parent_ids':d['parent_ids'],
                            'mutation_data':d['mutation_data']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingEvidence(self,data_I):
        '''update rows of dataStage01ResequencingEvidence'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_evidence).filter(
                            data_stage01_resequencing_evidence.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'parent_id':d['parent_id'],
                            'evidence_data':d['evidence_data']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingValidation(self,data_I):
        '''update rows of dataStage01ResequencingValidation'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_validation).filter(
                            data_stage01_resequencing_validation.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'validation_id':d['validation_id'],
                            'validation_data':d['validation_data']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingMutationsFiltered(self,data_I):
        '''update rows of dataStage01ResequencingMutationsFiltered'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(
                            data_stage01_resequencing_mutationsFiltered.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'mutation_id':d['mutation_id'],
                            'parent_ids':d['parent_ids'],
                            'mutation_data':d['mutation_data']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingMutationsAnnotated(self, data_I):
        '''add rows of dataStage01ResequencingMutationsAnnotated'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_mutationsAnnotated(
                            d['experiment_id'],
                            d['sample_name'],
                            d['mutation_frequency'],
                            d['mutation_type'],
                            d['mutation_position'],
                            d['mutation_data'],
                            d['mutation_annotations'],
                            d['mutation_genes'],
                            d['mutation_locations'],
                            d['mutation_links'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingMutationsAnnotated(self,data_I):
        '''update rows of dataStage01ResequencingMutationsAnnotated'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(
                            data_stage01_resequencing_mutationsAnnotated.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'mutation_frequency':d['mutation_frequency'],
                            'mutation_type':d['mutation_type'],
                            'mutation_position':d['mutation_position'],
                            'mutation_data':d['mutation_data'],
                            'mutation_annotations':d['mutation_annotations'],
                            'mutation_genes':d['mutation_genes'],
                            'mutation_locations':d['mutation_locations'],
                            'mutation_links':d['mutation_links'],
                            'used_':d['used_'],
                            'comment_':d['comment_']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingMutationsSeqChanges(self, data_I):
        '''add rows of dataStage01ResequencingMutationsSeqChanges'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_mutationsSeqChanges(
                            d['experiment_id'],
                            d['sample_name'],
                            d['mutation_frequency'],
                            d['mutation_type'],
                            d['mutation_position'],
                            d['mutation_genes'],
                            d['mutation_locations'],
                            d['dna_sequence_ref'],
                            d['dna_sequence_new'],
                            d['rna_sequence_ref'],
                            d['rna_sequence_new'],
                            d['peptide_sequence_ref'],
                            d['peptide_sequence_new'],
                            d['mutation_class'],
                            d['dna_features_region'],
                            d['rna_features_region'],
                            d['peptide_features_region'],
                            d['dna_feature_position'],
                            d['dna_feature_ref'],
                            d['dna_feature_new'],
                            d['rna_feature_position'],
                            d['rna_feature_ref'],
                            d['rna_feature_new'],
                            d['peptide_feature_position'],
                            d['peptide_feature_ref'],
                            d['peptide_feature_new'],
                            d['mutation_data'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingMutationsSeqChanges(self,data_I):
        '''update rows of dataStage01ResequencingMutationsSeqChanges'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_mutationsSeqChanges).filter(
                            data_stage01_resequencing_mutationsSeqChanges.id == d['id']
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'mutation_frequency':d['mutation_frequency'],
                            'mutation_type':d['mutation_type'],
                            'mutation_position':d['mutation_position'],
                            'mutation_genes':d['mutation_genes'],
                            'mutation_locations':d['mutation_locations'],
                            'dna_sequence_ref':d['dna_sequence_ref'],
                            'dna_sequence_new':d['dna_sequence_new'],
                            'rna_sequence_ref':d['rna_sequence_ref'],
                            'rna_sequence_new':d['rna_sequence_new'],
                            'peptide_sequence_ref':d['peptide_sequence_ref'],
                            'peptide_sequence_new':d['peptide_sequence_new'],
                            'mutation_class':d['mutation_class'],
                            'dna_features_region':d['dna_features_region'],
                            'rna_features_region':d['rna_features_region'],
                            'peptide_features_region':d['peptide_features_region'],
                            'mutation_data':d['mutation_data'],
                            'used_':d['used_'],
                            'comment_':d['comment_']
							},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query sample names from data_stage01_resequencing_metadata
    def get_sampleNames_experimentID_dataStage01ResequencingMetadata(self,experiment_id_I):
        '''Query samples names from resequencing metadata'''
        try:
            sample_names = self.session.query(data_stage01_resequencing_metadata.experiment_id,
                    data_stage01_resequencing_metadata.sample_name).filter(
                    data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).order_by(
                    data_stage01_resequencing_metadata.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: 
                sample_names_O.append(sn.sample_name);
            return sample_names_O
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentID_dataStage01ResequencingMetadata(self,experiment_id_I):
        '''Query data table rows by experiment_id'''
        try:
            data = self.session.query(data_stage01_resequencing_metadata).filter(
                    data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).all();
            data_O = [];
            for d in data: 
                data_O.append(d.__repr__dict__());
            return data_O
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_resequencing_mutations
    def get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutations(self,experiment_id_I,sample_name_I,
              frequency_criteria=0.1):
        '''Query mutation data
        NOTES:
        1. JSON is not a standard type across databases, therefore the key/values of the JSON
            object will be filtered post-query'''
        #1 filter sample_names that do not meet the frequency criteria
        try:
            data = self.session.query(data_stage01_resequencing_mutations).filter(
                    data_stage01_resequencing_mutations.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutations.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['experiment_id'] = d.experiment_id;
                data_dict['sample_name'] = d.sample_name;
                data_dict['mutation_id'] = d.mutation_id;
                data_dict['parent_ids'] = d.parent_ids;
                data_dict['mutation_data'] = d.mutation_data;
                #data_dict['mutation_data'] = json.loads(d.mutation_data);
                data_O.append(data_dict);
            # filter:
            data_filtered = [];
            for d in data_O:
                if 'frequency' in d['mutation_data'] and d['mutation_data']['frequency'] >= frequency_criteria:
                    data_filtered.append(d);
                #note: frequency is only provided for population resequences
                elif 'frequency' not in d['mutation_data']:
                    data_filtered.append(d);
            return data_filtered;
        except SQLAlchemyError as e:
            print(e);
            
    # query data from data_stage01_resequencing_evidence
    def get_evidence_experimentIDAndSampleNameAndParentID_dataStage01ResequencingEvidence(self,experiment_id_I,sample_name_I,parent_id_I,
              p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1):
        '''Query evidence data
        NOTES:
        1. JSON is not a standard type across databases, therefore the key/values of the JSON
            object will be filtered post-query'''
        #2 filter sample_names by evidence-specific criteria
        try:
            data = self.session.query(data_stage01_resequencing_evidence).filter(
                    data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_evidence.sample_name.like(sample_name_I),
                    data_stage01_resequencing_evidence.parent_id == parent_id_I).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['experiment_id'] = d.experiment_id;
                data_dict['sample_name'] = d.sample_name;
                data_dict['parent_id'] = d.parent_id;
                data_dict['evidence_data'] = d.evidence_data;
                #data_dict['evidence_data'] = json.loads(d.evidence_data);
                data_O.append(data_dict);
            # filter:
            data_filtered = [];
            data_filtered_dict = {};
            data_filtered = self._filter_evidenceByPValueAndQualityAndFrequency(data_O,p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria)
            return data_filtered;
        except SQLAlchemyError as e:
            print(e);
    def get_evidence_experimentIDAndSampleName_dataStage01ResequencingEvidence(self,experiment_id_I,sample_name_I,
              p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1):
        '''Query evidence data
        NOTES:
        1. JSON is not a standard type across databases, therefore the key/values of the JSON
            object will be filtered post-query'''
        #2 filter sample_names by evidence-specific criteria
        try:
            data = self.session.query(data_stage01_resequencing_evidence).filter(
                    data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_evidence.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['experiment_id'] = d.experiment_id;
                data_dict['sample_name'] = d.sample_name;
                data_dict['parent_id'] = d.parent_id;
                data_dict['evidence_data'] = d.evidence_data;
                #data_dict['evidence_data'] = json.loads(d.evidence_data);
                data_O.append(data_dict);
            # filter:
            data_filtered = [];
            data_filtered_dict = {};
            data_filtered = self._filter_evidenceByPValueAndQualityAndFrequency(data,p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria)
            return data_filtered;
        except SQLAlchemyError as e:
            print(e);
            
    # query data from data_stage01_resequencing_mutationsFiltered
    def get_sampleNames_experimentID_dataStage01ResequencingMutationsFiltered(self,experiment_id_I):
        '''Query mutation data'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsFiltered.sample_name).filter(
                    data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).group_by(
                    data_stage01_resequencing_mutationsFiltered.sample_name).order_by(
                    data_stage01_resequencing_mutationsFiltered.sample_name.asc()).all();
            sample_names_O = [];
            for d in data: 
                sample_names_O.append(d.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_resequencing_mutationsFiltered
    def get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsFiltered(self,experiment_id_I,sample_name_I):
        '''Query mutation data'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsFiltered.experiment_id,
                    data_stage01_resequencing_mutationsFiltered.sample_name,
                    data_stage01_resequencing_mutationsFiltered.mutation_id,
                    data_stage01_resequencing_mutationsFiltered.parent_ids,
                    data_stage01_resequencing_mutationsFiltered.mutation_data).filter(
                    data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsFiltered.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_dict = {};
                data_dict['experiment_id'] = d.experiment_id;
                data_dict['sample_name'] = d.sample_name;
                data_dict['mutation_id'] = d.mutation_id;
                data_dict['parent_ids'] = d.parent_ids;
                data_dict['mutation_data'] = d.mutation_data;
                #data_dict['mutation_data'] = json.loads(d.mutation_data);
                data_O.append(data_dict);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_resequencing_mutationsAnnotated
    def get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(self,experiment_id_I,sample_name_I):
        '''Query mutation data'''
        try:
            data = self.session.query(data_stage01_resequencing_mutationsAnnotated).filter(
                    data_stage01_resequencing_mutationsAnnotated.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_mutationsAnnotated.sample_name.like(sample_name_I)).all();
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