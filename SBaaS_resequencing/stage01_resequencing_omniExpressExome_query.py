﻿from .stage01_resequencing_omniExpressExome_postgresql_models import *

from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete
from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_resequencing_omniExpressExome_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for stage01_resequencing_omniExpressExome
        '''
        tables_supported = {'data_stage01_resequencing_omniExpressExome':data_stage01_resequencing_omniExpressExome,
                            'data_stage01_resequencing_omniExpressExome_annotations':data_stage01_resequencing_omniExpressExome_annotations,
                            'data_stage01_resequencing_omniExpressExome_header':data_stage01_resequencing_omniExpressExome_header,
                            'data_stage01_resequencing_OmniExpressExome_annotationsAuxillary':data_stage01_resequencing_OmniExpressExome_annotationsAuxillary,
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
    def _get_rows_experimentID_dataStage01ResequencingOmniExpressExome(self,
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
            'column_name':'sample_name',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':'SNP_Name',
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
    def getJoin_rows_experimentID_dataStage01ResequecingOmniExpressExome(
        self,experiment_id_I):
        '''Join rows between omniExpressExome, annotations, and annotations auxillary
        INPUT:
        experiment_id_I = string
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        data_O = [];
        try:
            query_cmd = '''SELECT "data_stage01_resequencing_omniExpressExome"."experiment_id",
                "data_stage01_resequencing_omniExpressExome"."sample_name",
                "data_stage01_resequencing_omniExpressExome"."SNP_Name",
                "data_stage01_resequencing_omniExpressExome"."Sample_ID",
                "data_stage01_resequencing_omniExpressExome"."Allele1_Top",
                "data_stage01_resequencing_omniExpressExome"."Allele2_Top",
                "data_stage01_resequencing_omniExpressExome"."GC_Score",
                "data_stage01_resequencing_omniExpressExome_annotations"."IlmnID",
                "data_stage01_resequencing_omniExpressExome_annotations"."Name",
                "data_stage01_resequencing_omniExpressExome_annotations"."IlmnStrand",
                "data_stage01_resequencing_omniExpressExome_annotations"."SNP",
                "data_stage01_resequencing_omniExpressExome_annotations"."AddressA_ID",
                "data_stage01_resequencing_omniExpressExome_annotations"."AlleleA_ProbeSeq",
                "data_stage01_resequencing_omniExpressExome_annotations"."AddressB_ID",
                "data_stage01_resequencing_omniExpressExome_annotations"."AlleleB_ProbeSeq",
                "data_stage01_resequencing_omniExpressExome_annotations"."GenomeBuild",
                "data_stage01_resequencing_omniExpressExome_annotations"."Chr",
                "data_stage01_resequencing_omniExpressExome_annotations"."MapInfo",
                "data_stage01_resequencing_omniExpressExome_annotations"."Ploidy",
                "data_stage01_resequencing_omniExpressExome_annotations"."Species",
                "data_stage01_resequencing_omniExpressExome_annotations"."Source",
                "data_stage01_resequencing_omniExpressExome_annotations"."SourceVersion",
                "data_stage01_resequencing_omniExpressExome_annotations"."SourceStrand",
                "data_stage01_resequencing_omniExpressExome_annotations"."SourceSeq",
                "data_stage01_resequencing_omniExpressExome_annotations"."TopGenomicSeq",
                "data_stage01_resequencing_omniExpressExome_annotations"."BeadSetID",
                "data_stage01_resequencing_omniExpressExome_annotations"."Exp_Clusters",
                "data_stage01_resequencing_omniExpressExome_annotations"."RefStrand",
                "data_stage01_resequencing_OmniExpressExome_annotationsAuxillary"."Name",
                "data_stage01_resequencing_OmniExpressExome_annotationsAuxillary"."RsID"
                '''

            query_cmd+= '''WHERE "data_stage01_resequencing_omniExpressExome"."experiment_id" = %s '''
            if calculated_concentration_units_I:
                cmd_q = "AND calculated_concentration_units =ANY ('{%s}'::text[]) " %(self.convert_list2string(calculated_concentration_units_I));
                cmd+=cmd_q;
        except Exception as e:
            if raise_I: raise;
            else: print(e);

        query['where'] = [
            {"table_name":tables[0],
            'column_name':'experiment_id',
            'value':experiment_id_I,
            'operator':'=',
            'connector':'AND'
                        },
            {"table_name":tables[0],
            'column_name':'used_',
            'value':'true',
            'operator':'IS',
            'connector':'AND'
                },
            {"table_name":tables[0],
            'column_name':"SNP_Name",
            'value':'''"data_stage01_resequencing_OmniExpressExome_annotationsAuxillary".""Name" ''',
            'operator':'=',
            'connector':'AND'
                },
            {"table_name":tables[1],
            'column_name':"Name",
            'value':'''"data_stage01_resequencing_OmniExpressExome_annotationsAuxillary".""RsID" ''',
            'operator':'=',
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
            {"table_name":tables[0],
            'column_name':'Chr',
            'order':'ASC',
            },
            {"table_name":tables[0],
            'column_name':"MapInfo",
            'order':'ASC',
            },
        ];

        data_O = [dict(d) for d in query_select.execute_select(query_cmd)];
        return data_O;
    
    #SPLIT 1:   
    def get_rows_experimentID_dataStage01ResequencingOmniExpressExome(self,experiment_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_omniExpressExome).filter(
                    data_stage01_resequencing_omniExpressExome.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_omniExpressExome.used_.is_(True)).all();
            rows_O = [d.__repr__dict__() for d in data];
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    