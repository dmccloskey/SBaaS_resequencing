#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_analysis_postgresql_models import *

class stage01_resequencing_analysis_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_resequencing_analysis':data_stage01_resequencing_analysis
                        };
        self.set_supportedTables(tables_supported);
    def reset_dataStage01_resequencing_analysis(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_analysis).filter(data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_analysis).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_resequencing_analysis
    def get_analysis_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).all();
            analysis_id_O = []
            experiment_id_O = []
            lineage_name_O = []
            sample_name_O = []
            analysis_type_O = []
            analysis_O = {};
            if data: 
                for d in data:
                    analysis_id_O.append(d.analysis_id);
                    experiment_id_O.append(d.experiment_id);
                    lineage_name_O.append(d.lineage_name);
                    sample_name_O.append(d.sample_name);
                    analysis_type_O.append(d.analysis_type);
                analysis_id_O = list(set(analysis_id_O))
                experiment_id_O = list(set(experiment_id_O))
                lineage_name_O = list(set(lineage_name_O))
                sample_name_O = list(set(sample_name_O))
                analysis_type_O = list(set(analysis_type_O))
                analysis_O={
                        'analysis_id':analysis_id_O,
                        'experiment_id':experiment_id_O,
                        'lineage_name':lineage_name_O,
                        'sample_name':sample_name_O,
                        'analysis_type':analysis_type_O};
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndLineageName_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.lineage_name).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.lineage_name).order_by(
                    data_stage01_resequencing_analysis.experiment_id.asc(),
                    data_stage01_resequencing_analysis.lineage_name.asc()).all();
            experiment_id_O = []
            lineage_name_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    lineage_name_O.append(d.lineage_name);                
            return  experiment_id_O,lineage_name_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleName_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.sample_name).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.sample_name).order_by(
                    data_stage01_resequencing_analysis.experiment_id.asc(),
                    data_stage01_resequencing_analysis.sample_name.asc()).all();
            experiment_id_O = []
            sample_name_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_O.append(d.sample_name);                
            return  experiment_id_O,sample_name_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.sample_name,
                    data_stage01_resequencing_analysis.time_point).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.sample_name,
                    data_stage01_resequencing_analysis.time_point).order_by(
                    data_stage01_resequencing_analysis.experiment_id.asc(),
                    data_stage01_resequencing_analysis.sample_name.asc(),
                    data_stage01_resequencing_analysis.time_point.asc()).all();
            experiment_id_O = []
            sample_name_O = []
            time_point_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    sample_name_O.append(d.sample_name);    
                    time_point_O.append(d.time_point);              
            return  experiment_id_O,sample_name_O,time_point_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.lineage_name,
                    data_stage01_resequencing_analysis.sample_name,
                    data_stage01_resequencing_analysis.time_point).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.lineage_name,
                    data_stage01_resequencing_analysis.sample_name,
                    data_stage01_resequencing_analysis.time_point).order_by(
                    data_stage01_resequencing_analysis.experiment_id.asc(),
                    data_stage01_resequencing_analysis.lineage_name.asc(),
                    data_stage01_resequencing_analysis.sample_name.asc(),
                    data_stage01_resequencing_analysis.time_point.asc()).all();
            experiment_id_O = []
            lineage_name_O = []
            sample_name_O = []
            time_point_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    lineage_name_O.append(d.lineage_name); 
                    sample_name_O.append(d.sample_name);    
                    time_point_O.append(d.time_point);              
            return  experiment_id_O,lineage_name_O,sample_name_O,time_point_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndLineageNameAndSampleName_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.lineage_name,
                    data_stage01_resequencing_analysis.sample_name).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).group_by(
                    data_stage01_resequencing_analysis.experiment_id,
                    data_stage01_resequencing_analysis.lineage_name,
                    data_stage01_resequencing_analysis.sample_name).order_by(
                    data_stage01_resequencing_analysis.experiment_id.asc(),
                    data_stage01_resequencing_analysis.lineage_name.asc(),
                    data_stage01_resequencing_analysis.sample_name.asc()).all();
            experiment_id_O = []
            lineage_name_O = []
            sample_name_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    lineage_name_O.append(d.lineage_name); 
                    sample_name_O.append(d.sample_name);            
            return  experiment_id_O,lineage_name_O,sample_name_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_analysis).filter(
                    data_stage01_resequencing_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_resequencing_analysis.used_.is_(True)).all();
            analysis_O = [];
            if data: 
                for d in data:
                    analysis_O.append({
                        'analysis_id':d.analysis_id,
                        'experiment_id':d.experiment_id,
                        'lineage_name':d.lineage_name,
                        'sample_name':d.sample_name,
                        'analysis_type':d.analysis_type});
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);
    
    def get_rows_analysisID_dataStage01ResequencingAnalysis(self,
                analysis_id_I,
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query rows by analysis_id from data_stage01_resequencing_analysis
        INPUT:
        analysis_id_I = string
        query_I = {}
        output_O = string
        dictColumn_I = string
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_analysis'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [{"table_name":tables[0]}];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'analysis_id',
            'value':analysis_id_I,
            'operator':'LIKE',
            'connector':'AND'
                        },
            {"table_name":tables[0],
            'column_name':'used_',
            'value':'true',
            'operator':'IS',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'experiment_id',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'sample_name',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k]=[];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def getGroup_experimentIDAndLineageNameAndSampleName_analysisID_dataStage01ResequencingAnalysis(self,
                analysis_id_I,
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query rows by analysis_id from data_stage01_resequencing_analysis
        INPUT:
        analysis_id_I = string
        query_I = {}
        output_O = string
        dictColumn_I = string
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_analysis'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],'column_name':'experiment_id'},
            {"table_name":tables[0],'column_name':'lineage_name'},
            {"table_name":tables[0],'column_name':'sample_name'},
            ];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'analysis_id',
            'value':analysis_id_I,
            'operator':'LIKE',
            'connector':'AND'
                        },
            {"table_name":tables[0],
            'column_name':'used_',
            'value':'true',
            'operator':'IS',
            'connector':'AND'
                },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'experiment_id',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'sample_name',
            'order':'ASC',
            },
        ];
        query['group_by'] = [
            {"table_name":tables[0],'column_name':'experiment_id'},
            {"table_name":tables[0],'column_name':'lineage_name'},
            {"table_name":tables[0],'column_name':'sample_name'},
            ];

        #additional blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k]=[];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;