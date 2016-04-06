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
                            'data_stage01_resequencing_endpointLineages':data_stage01_resequencing_endpointLineages,
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
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_endpointLineages(self,experiment_id_I = None,analysis_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_endpointLineages).filter(data_stage01_resequencing_endpointLineages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            elif analysis_id_I:
                reset = self.session.query(data_stage01_resequencing_endpointLineages).filter(data_stage01_resequencing_endpointLineages.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
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
    def getAggregateFunction_rows_analysisID_dataStage01ResequencingEndpoints(self,
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='scalar',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_resequencing_endpoints
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpoints'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":column_name_I,
             'aggregate_function':aggregate_function_I,
             'label':aggregate_label_I,
             }
            ];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'analysis_id',
            'value':analysis_id_I,
            'operator':'LIKE',
            'connector':'AND'
                        },
            #{"table_name":tables[0],
            #'column_name':'used_',
            #'value':'true',
            #'operator':'IS',
            #'connector':'AND'
            #    },
	    ];

        #additional query blocks
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
    def getGroupAndCount_analysisIDAndMutationTypeAndMutationPositionAndMutationGenes_analysisID_dataStage01ResequencingEndpoints(self,
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_resequencing_endpoints
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpoints'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'mutation_type',
             },
            {"table_name":tables[0],
             "column_name":'mutation_position',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
            ];
        query['group_by'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'mutation_type',
             },
            {"table_name":tables[0],
             "column_name":'mutation_position',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
	    ];
        query['order_by'] = [
            {
            'label':'count_1',
            'order':'ASC',
                        },
            {"table_name":tables[0],
            'column_name':'mutation_position',
            'order':'ASC',
                        },
	    ];

        #additional query blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k]=[];
            for r in v:
                query[k].append(r);

        data_O = self.getAggregateFunction_rows_analysisID_dataStage01ResequencingEndpoints(
                analysis_id_I=analysis_id_I,
                column_name_I=column_name_I,
                aggregate_function_I=aggregate_function_I,
                aggregate_label_I=aggregate_label_I,
                query_I=query,
                output_O=output_O,
                dictColumn_I=dictColumn_I
            );
        return data_O;
    def getGroupAndCount_analysisIDAndSampleNameAndMutationGenes_analysisID_dataStage01ResequencingEndpoints(self,
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_resequencing_endpoints
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpoints'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'sample_name',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
            ];
        query['group_by'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'sample_name',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'sample_name',
            'order':'ASC',
                        },
            {"table_name":tables[0],
            'column_name':'mutation_genes',
            'order':'ASC',
                        },
	    ];

        #additional query blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k]=[];
            for r in v:
                query[k].append(r);

        data_O = self.getAggregateFunction_rows_analysisID_dataStage01ResequencingEndpoints(
                analysis_id_I=analysis_id_I,
                column_name_I=column_name_I,
                aggregate_function_I=aggregate_function_I,
                aggregate_label_I=aggregate_label_I,
                query_I=query,
                output_O=output_O,
                dictColumn_I=dictColumn_I
            );
        return data_O;
    
    def get_rows_analysisID_dataStage01ResequencingEndpointLineages(self,
                analysis_id_I,
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query rows by analysis_id from data_stage01_resequencing_endpointLineages
        INPUT:
        analysis_id_I = string
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpointLineages'];
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
            #{"table_name":tables[0],
            #'column_name':'used_',
            #'value':'true',
            #'operator':'IS',
            #'connector':'AND'
            #    },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'experiment_id',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'lineage_name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mutation_position',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'mutation_type',
            'order':'ASC',
            },
        ];

        #additional blocks
        for k,v in query_I.items():
            for r in v:
                query[k].append(r);
        
        data_O = self.get_rows_tables(
            tables_I=tables,
            query_I=query,
            output_O=output_O,
            dictColumn_I=dictColumn_I);
        return data_O;
    def getAggregateFunction_rows_analysisID_dataStage01ResequencingEndpointLineages(self,
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='scalar',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_resequencing_endpointLineages
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpointLineages'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":column_name_I,
             'aggregate_function':aggregate_function_I,
             'label':aggregate_label_I,
             }
            ];
        query['where'] = [
            {"table_name":tables[0],
            'column_name':'analysis_id',
            'value':analysis_id_I,
            'operator':'LIKE',
            'connector':'AND'
                        },
            #{"table_name":tables[0],
            #'column_name':'used_',
            #'value':'true',
            #'operator':'IS',
            #'connector':'AND'
            #    },
	    ];

        #additional query blocks
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
    def getGroupAndCount_analysisIDAndMutationTypeAndMutationPositionAndMutationGenes_analysisID_dataStage01ResequencingEndpointLineages(self,
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_resequencing_endpointLineages
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpointLineages'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'mutation_type',
             },
            {"table_name":tables[0],
             "column_name":'mutation_position',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
            ];
        query['group_by'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'mutation_type',
             },
            {"table_name":tables[0],
             "column_name":'mutation_position',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
	    ];
        query['order_by'] = [
            {
            'label':'count_1',
            'order':'ASC',
                        },
            {"table_name":tables[0],
            'column_name':'mutation_position',
            'order':'ASC',
                        },
	    ];

        #additional query blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k]=[];
            for r in v:
                query[k].append(r);

        data_O = self.getAggregateFunction_rows_analysisID_dataStage01ResequencingEndpointLineages(
                analysis_id_I=analysis_id_I,
                column_name_I=column_name_I,
                aggregate_function_I=aggregate_function_I,
                aggregate_label_I=aggregate_label_I,
                query_I=query,
                output_O=output_O,
                dictColumn_I=dictColumn_I
            );
        return data_O;
    def getGroupAndCount_analysisIDAndLineageNameAndMutationGenes_analysisID_dataStage01ResequencingEndpointLineages(self,
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I={},
                output_O='listDict',
                dictColumn_I=None):
        '''Query row count by analysis_id from data_stage01_resequencing_endpointLineages
        INPUT:
        analysis_id_I = string
        column_name_I = string
        aggregate_function_I = name of the aggregate function to call on the column
        output_O = string
        dictColumn_I = string
        OPTIONAL INPUT:
        query_I = additional query blocks
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        tables = ['data_stage01_resequencing_endpointLineages'];
        # get the listDict data
        data_O = [];
        query = {};
        query['select'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'lineage_name',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
            ];
        query['group_by'] = [
            {"table_name":tables[0],
             "column_name":'analysis_id',
             },
            {"table_name":tables[0],
             "column_name":'lineage_name',
             },
            {"table_name":tables[0],
             "column_name":'mutation_genes',
             },
	    ];
        query['order_by'] = [
            {"table_name":tables[0],
            'column_name':'lineage_name',
            'order':'ASC',
                        },
            {"table_name":tables[0],
            'column_name':'mutation_genes',
            'order':'ASC',
                        },
	    ];

        #additional query blocks
        for k,v in query_I.items():
            if not k in query.keys():
                query[k]=[];
            for r in v:
                query[k].append(r);

        data_O = self.getAggregateFunction_rows_analysisID_dataStage01ResequencingEndpointLineages(
                analysis_id_I=analysis_id_I,
                column_name_I=column_name_I,
                aggregate_function_I=aggregate_function_I,
                aggregate_label_I=aggregate_label_I,
                query_I=query,
                output_O=output_O,
                dictColumn_I=dictColumn_I
            );
        return data_O;