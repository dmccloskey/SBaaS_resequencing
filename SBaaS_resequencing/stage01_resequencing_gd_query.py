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
            'data_stage01_resequencing_mutationsFiltered':data_stage01_resequencing_mutationsFiltered,
            'data_stage01_resequencing_validation':data_stage01_resequencing_validation,
            'data_stage01_resequencing_evidence':data_stage01_resequencing_evidence,
                        };
        self.set_supportedTables(tables_supported);
    def reset_dataStage01_resequencing_gd(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_metadata).filter(data_stage01_resequencing_metadata.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).filter(data_stage01_resequencing_mutations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).filter(data_stage01_resequencing_evidence.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).filter(data_stage01_resequencing_validation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).filter(data_stage01_resequencing_mutationsFiltered.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_metadata).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutations).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_evidence).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_validation).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_mutationsFiltered).delete(synchronize_session=False);
            self.session.commit();
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
