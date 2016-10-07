from .stage01_resequencing_omniExpressExome_postgresql_models import *

from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete
from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_resequencing_omniExpressExome_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for stage01_resequencing_omniExpressExome
        '''
        tables_supported = {'data_stage01_resequencing_omniExpressExome':data_stage01_resequencing_omniExpressExome,
                            'data_stage01_resequencing_omniExpressExome_annotations':data_stage01_resequencing_omniExpressExome_annotations,
                            'data_stage01_resequencing_omniExpressExome_header':data_stage01_resequencing_omniExpressExome_header,
                        };
        self.set_supportedTables(tables_supported);
    #SPLIT 2:
    def reset_data_stage01_resequencing_omniExpressExome(self,
            tables_I = ['data_stage01_resequencing_omniExpressExome',
                        'data_stage01_resequencing_omniExpressExome_header'],
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
                        #'value':self.convert_string2StringString(experiment_id_I),
		                'operator':'LIKE',
                        'connector':'AND'
                        }
	                ];
                table_model = self.convert_tableStringList2SqlalchemyModelDict([table]);
                query = querydelete.make_queryFromString(table_model,query);
                querydelete.reset_table_sqlalchemyModel(query_I=query,warn_I=warn_I);
        except Exception as e:
            print(e);
    def _get_rows_experimentID_dataStage01ResequencingomniExpressExome(self,
                experiment_id_I,
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query rows by experiment_id from data_stage01_resequencing_omniExpressExome
        INPUT:
        experiment_id_I = string
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_omniExpressExome'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [{"table_name":tables[0]}];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'experiment_id',
            'value':experiment_id_I,
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
            'column_name':'sample_name_short',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'component_name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'time_point',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            if k not in query.items():
                query[k]=[];
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    
    #SPLIT 1:   
    def get_rows_experimentID_dataStage01ResequencingomniExpressExome(self,experiment_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_omniExpressExome).filter(
                    data_stage01_resequencing_omniExpressExome.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_omniExpressExome.used_.is_(True)).all();
            rows_O = [d.__repr__dict__() for d in data];
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    