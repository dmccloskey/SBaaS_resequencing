#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_endpoints_postgresql_models import *

class stage01_resequencing_endpoints_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_resequencing_endpoints':data_stage01_resequencing_endpoints,
                        };
        self.set_supportedTables(tables_supported);
    def drop_dataStage01_resequencing_endpoints(self):
        try:
            data_stage01_resequencing_endpoints.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_endpoints(self,experiment_id_I = None,analysis_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            elif analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_endpoints).filter(data_stage01_resequencing_endpoints.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_endpoints).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_resequencing_endpoints(self):
        try:
            data_stage01_resequencing_endpoints.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01ResequencingEndpoints(self, data_I):
        '''add rows of data_stage01_resequencing_endpoints'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_endpoints(d['experiment_id'],
                            d['analysis_id'],
                            d['sample_name'],
                            d['mutation_frequency'],
                            d['mutation_type'],
                            d['mutation_position'],
                            d['mutation_data'],
                            d['isUnique'],
                            d['mutation_annotations'],
                            d['mutation_genes'],
                            d['mutation_locations'],
                            d['mutation_links'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01ResequencingEndpoints(self,data_I):
        '''update rows of data_stage01_resequencing_endpoints'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_endpoints).filter(
                           data_stage01_resequencing_endpoints.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'analysis_id':d['analysis_id'],
                            'sample_name':d['sample_name'],
                            'mutation_frequency':d['mutation_frequency'],
                            'mutation_type':d['mutation_type'],
                            'mutation_position':d['mutation_position'],
                            'mutation_data':d['mutation_data'],
                            'isUnique':d['isUnique'],
                            'mutation_annotations':d['mutation_annotations'],
                            'mutation_genes':d['mutation_genes'],
                            'mutation_locations':d['mutation_locations'],
                            'mutation_links':d['mutation_links'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    # query sample names from data_stage01_resequencing_endpoints
    def get_sampleNames_experimentID_dataStage01ResequencingEndpoints(self,experiment_id_I):
        '''Query samples names from resequencing endpoints'''
        try:
            sample_names = self.session.query(data_stage01_resequencing_endpoints.experiment_id,
                    data_stage01_resequencing_endpoints.sample_name).filter(
                    data_stage01_resequencing_endpoints.experiment_id.like(experiment_id_I)).group_by(data_stage01_resequencing_endpoints.experiment_id,
                    data_stage01_resequencing_endpoints.sample_name).order_by(
                    data_stage01_resequencing_endpoints.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: 
                sample_names_O.append(sn.sample_name);
            return sample_names_O
        except SQLAlchemyError as e:
            print(e);
    # query row from data_stage01_resequencing_endpoints
    def get_row_experimentIDAndSampleName_dataStage01ResequencingEndpoints(self,experiment_id_I,sample_name_I):
        '''Query samples names from resequencing endpoints'''
        try:
            data = self.session.query(data_stage01_resequencing_endpoints).filter(
                    data_stage01_resequencing_endpoints.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_endpoints.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_tmp = {};
                data_tmp['id']=d.id;
                data_tmp['experiment_id']=d.experiment_id;
                data_tmp['analysis_id']=d.analysis_id;
                data_tmp['sample_name']=d.sample_name;
                data_tmp['mutation_frequency']=d.mutation_frequency;
                data_tmp['mutation_type']=d.mutation_type;
                data_tmp['mutation_position']=d.mutation_position;
                data_tmp['mutation_data']=d.mutation_data;
                data_tmp['isUnique']=d.isUnique;
                data_tmp['mutation_annotations']=d.mutation_annotations;
                data_tmp['mutation_genes']=d.mutation_genes;
                data_tmp['mutation_locations']=d.mutation_locations;
                data_tmp['mutation_links']=d.mutation_links;
                data_tmp['comment_']=d.comment_;
                data_O.append(data_tmp);
            return data_O;
        except SQLAlchemyError as e:
            print(e);