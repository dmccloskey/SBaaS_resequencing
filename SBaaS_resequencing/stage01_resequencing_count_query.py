#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_count_postgresql_models import *

class stage01_resequencing_count_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_resequencing_count':data_stage01_resequencing_count,
                            'data_stage01_resequencing_countPerSample':data_stage01_resequencing_countPerSample
                        };
        self.set_supportedTables(tables_supported);
    def drop_dataStage01_resequencing_count(self):
        try:
            data_stage01_resequencing_count.__table__.drop(self.engine,True);
            data_stage01_resequencing_countPerSample.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_resequencing_count(self):
        try:
            data_stage01_resequencing_count.__table__.create(self.engine,True);
            data_stage01_resequencing_countPerSample.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

    #data_stage01_resequencing_count      
    def reset_dataStage01_resequencing_count(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_count).filter(data_stage01_resequencing_count.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);  
    def add_dataStage01ResequencingCount(self, data_I):
        '''add rows of data_stage01_resequencing_count'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_count(d
                        #d['analysis_id'],
                        #d['feature_id'],
                        #d['feature_units'],
                        #d['element_id'],
                        #d['frequency'],
                        #d['fraction'],
                        #d['used_'],
                        #d['comment_'],
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingCount(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_count).filter(
                           data_stage01_resequencing_count.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'feature_id':d['feature_id'],
                            'feature_units':d['feature_units'],
                            'element_id':d['element_id'],
                            'frequency':d['frequency'],
                            'fraction':d['fraction'],
                            'used_':d['used_'],
                            'comment_':d['comment_'],},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query data from data_stage01_resequencing_count
    def get_rows_analysisID_dataStage01ResequencingCount(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_count).filter(
                    data_stage01_resequencing_count.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_count.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    rows_O.append(d.__repr__dict__());
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsAsFeaturesDict_analysisID_dataStage01ResequencingCount(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_count).filter(
                    data_stage01_resequencing_count.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_count.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.feature_id in rows_O.keys():
                        rows_O[d.feature_id].append(d.__repr__dict__());
                    else:
                        rows_O[d.feature_id] = [];
                        rows_O[d.feature_id].append(d.__repr__dict__());
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    #data_stage01_resequencing_countPerSample      
    def reset_dataStage01_resequencing_countPerSample(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_countPerSample).filter(data_stage01_resequencing_countPerSample.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);  
    def add_dataStage01ResequencingCountPerSample(self, data_I):
        '''add rows of data_stage01_resequencing_countPerSample'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_countPerSample(d
                        #d['analysis_id'],
                        #d['experiment_id'],
                        #d['lineage_name'],
                        #d['sample_name'],
                        #d['time_point'],
                        #d['feature_id'],
                        #d['feature_units'],
                        #d['element_id'],
                        #d['frequency'],
                        #d['fraction'],
                        #d['used_'],
                        #d['comment_'],
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingCountPerSample(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_countPerSample).filter(
                           data_stage01_resequencing_countPerSample.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'lineage_name':d['lineage_name'],
                            'sample_name':d['sample_name'],
                            'time_point':d['time_point'],
                            'feature_id':d['feature_id'],
                            'feature_units':d['feature_units'],
                            'element_id':d['element_id'],
                            'frequency':d['frequency'],
                            'fraction':d['fraction'],
                            'used_':d['used_'],
                            'comment_':d['comment_'],},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query data from data_stage01_resequencing_countPerSample
    def get_rows_analysisID_dataStage01ResequencingCountPerSample(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_countPerSample).filter(
                    data_stage01_resequencing_countPerSample.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_countPerSample.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    rows_O.append(d.__repr__dict__());
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsAsFeaturesDict_analysisID_dataStage01ResequencingCountPerSample(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_countPerSample).filter(
                    data_stage01_resequencing_countPerSample.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_countPerSample.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.feature_id in rows_O.keys():
                        rows_O[d.feature_id].append(d.__repr__dict__());
                    else:
                        rows_O[d.feature_id] = [];
                        rows_O[d.feature_id].append(d.__repr__dict__());
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

