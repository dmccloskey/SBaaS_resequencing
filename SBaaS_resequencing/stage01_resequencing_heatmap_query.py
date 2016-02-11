#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_heatmap_postgresql_models import *

class stage01_resequencing_heatmap_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_resequencing_heatmap':data_stage01_resequencing_heatmap,
                            'data_stage01_resequencing_dendrogram':data_stage01_resequencing_dendrogram,
                        };
        self.set_supportedTables(tables_supported);

    # query data from data_stage01_resequencing_heatmap
    def get_rows_analysisID_dataStage01ResequencingHeatmap(self,analysis_id_I):
        '''Query rows by analysisid and sample_name from data_stage01_resequencing_heatmap'''
        try:
            data = self.session.query(data_stage01_resequencing_heatmap).filter(
                    data_stage01_resequencing_heatmap.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_heatmap.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                'analysis_id':d.analysis_id,
            'col_index':d.col_index,
            'row_index':d.row_index,
            'value':d.value,
            'col_leaves':d.col_leaves,
            'row_leaves':d.row_leaves,
            'col_label':d.col_label,
            'row_label':d.row_label,
            'col_pdist_metric':d.col_pdist_metric,
            'row_pdist_metric':d.row_pdist_metric,
            'col_linkage_method':d.col_linkage_method,
            'row_linkage_method':d.row_linkage_method,
            'value_units':d.value_units,
            'used_':d.used_,
            'comment_':d.comment_}
                              );
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_resequencing_heatmap(self):
        try:
            data_stage01_resequencing_heatmap.__table__.drop(self.engine,True);
            data_stage01_resequencing_dendrogram.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_heatmapAndDendrogram(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_heatmap).filter(data_stage01_resequencing_heatmap.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_dendrogram).filter(data_stage01_resequencing_dendrogram.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_heatmap).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_dendrogram).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_resequencing_heatmap(self):
        try:
            data_stage01_resequencing_heatmap.__table__.create(self.engine,True);
            data_stage01_resequencing_dendrogram.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_heatmap(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_heatmap).filter(data_stage01_resequencing_heatmap.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_heatmap).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_dendrogram(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_dendrogram).filter(data_stage01_resequencing_dendrogram.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_dendrogram).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);