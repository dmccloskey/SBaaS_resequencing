from .stage01_resequencing_omniExpressExome_postgresql_models import *

from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_resequencing_omniExpressExome_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for stage01_resequencing_omniExpressExome
        '''
        tables_supported = {'data_stage01_resequencing_omniExpressExome':data_stage01_resequencing_omniExpressExome,
                            'data_stage01_resequencing_omniExpressExome_annotations':data_stage01_resequencing_omniExpressExome_annotations,
                            'data_stage01_resequencing_omniExpressExome_header':data_stage01_resequencing_omniExpressExome_header,
                            'data_stage01_resequencing_omniExpressExome_annotations2':data_stage01_resequencing_omniExpressExome_annotations2,
                            'data_stage01_resequencing_omniExpressExomeFiltered':data_stage01_resequencing_omniExpressExomeFiltered,
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
    def getJoin_rows_experimentIDs_dataStage01ResequecingOmniExpressExomeAndAnnotationsAndAnnotations2(
        self,
        experiment_ids_I='',
        sample_names_I='',
        raise_I = False):
        '''Join rows between omniExpressExome, annotations, and annotations auxillary
        INPUT:
        experiment_id_I = string
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        data_O = [];
        try:
            subquery2 = '''SELECT "data_stage01_resequencing_omniExpressExome"."experiment_id",
                "data_stage01_resequencing_omniExpressExome"."sample_name",
                "data_stage01_resequencing_omniExpressExome"."SNP_Name",
                "data_stage01_resequencing_omniExpressExome"."Sample_ID",
                "data_stage01_resequencing_omniExpressExome"."Allele1_Top",
                "data_stage01_resequencing_omniExpressExome"."Allele2_Top",
                "data_stage01_resequencing_omniExpressExome"."GC_Score"
                '''
            subquery2+= '''FROM "data_stage01_resequencing_omniExpressExome" '''
            subquery2+= '''WHERE "data_stage01_resequencing_omniExpressExome"."used_" '''
            if experiment_ids_I:
                cmd_q = '''AND "data_stage01_resequencing_omniExpressExome"."experiment_id" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(experiment_ids_I));
                subquery2+=cmd_q;
            if sample_names_I:
                cmd_q = '''AND "data_stage01_resequencing_omniExpressExome"."sample_name" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(sample_names_I));
                subquery2+=cmd_q;
            subquery2+= '''ORDER BY "data_stage01_resequencing_omniExpressExome"."experiment_id" ASC, '''
            subquery2+= '''"data_stage01_resequencing_omniExpressExome"."sample_name" ASC '''

            subquery1 = '''SELECT "subquery2"."experiment_id",
                "subquery2"."sample_name",
                "subquery2"."SNP_Name",
                "subquery2"."Sample_ID",
                "subquery2"."Allele1_Top",
                "subquery2"."Allele2_Top",
                "subquery2"."GC_Score",
                "data_stage01_resequencing_omniExpressExome_annotations2"."Name",
                "data_stage01_resequencing_omniExpressExome_annotations2"."RsID"
                '''
            subquery1+= '''FROM "data_stage01_resequencing_omniExpressExome_annotations2", (%s) AS subquery2 ''' %subquery2
            subquery1+= '''WHERE "subquery2"."SNP_Name" = "data_stage01_resequencing_omniExpressExome_annotations2"."Name" '''
            subquery1+= '''ORDER BY "subquery2"."experiment_id" ASC, '''
            subquery1+= '''"subquery2"."sample_name" ASC, '''
            subquery1+= '''"data_stage01_resequencing_omniExpressExome_annotations2"."Name" ASC '''

            query_cmd = '''SELECT "subquery1"."experiment_id",
                "subquery1"."sample_name",
                "subquery1"."SNP_Name",
                "subquery1"."Sample_ID",
                "subquery1"."Allele1_Top",
                "subquery1"."Allele2_Top",
                "subquery1"."GC_Score",
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
                "data_stage01_resequencing_omniExpressExome_annotations"."RefStrand"  '''
            query_cmd+= '''FROM "data_stage01_resequencing_omniExpressExome_annotations", (%s) AS subquery1 ''' %subquery1
            query_cmd+= '''WHERE ("data_stage01_resequencing_omniExpressExome_annotations"."Name" ="subquery1"."RsID" 
                OR "data_stage01_resequencing_omniExpressExome_annotations"."Name" LIKE '%,' || "subquery1"."RsID" 
                OR "data_stage01_resequencing_omniExpressExome_annotations"."Name" LIKE "subquery1"."RsID" || ',%' 
                OR "data_stage01_resequencing_omniExpressExome_annotations"."Name" LIKE '%,' || "subquery1"."RsID" || ',%') '''
            query_cmd+= '''ORDER BY "subquery1"."experiment_id" ASC, '''
            query_cmd+= '''"subquery1"."sample_name" ASC, '''
            query_cmd+= '''"data_stage01_resequencing_omniExpressExome_annotations"."Chr" ASC, '''
            query_cmd+= '''"data_stage01_resequencing_omniExpressExome_annotations"."MapInfo" ASC '''
            query_cmd+= ';';

            query_select = sbaas_base_query_select(self.session,self.engine,self.settings)
            data_O = [dict(d) for d in query_select.execute_select(query_cmd)];

        except Exception as e:
            if raise_I: raise;
            else: print(e);

        return data_O;
    def getJoin_rows_experimentIDs_dataStage01ResequecingOmniExpressExomeAndAnnotations(
        self,
        experiment_ids_I='',
        sample_names_I='',
        raise_I = False):
        '''Join rows between omniExpressExome, annotations, and annotations auxillary
        INPUT:
        experiment_ids_I = string or list
        sample_names_I = string or list
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        data_O = [];
        try:
            subquery1 = '''SELECT "data_stage01_resequencing_omniExpressExome"."experiment_id",
                "data_stage01_resequencing_omniExpressExome"."sample_name",
                "data_stage01_resequencing_omniExpressExome"."SNP_Name",
                "data_stage01_resequencing_omniExpressExome"."Sample_ID",
                "data_stage01_resequencing_omniExpressExome"."Allele1_Top",
                "data_stage01_resequencing_omniExpressExome"."Allele2_Top",
                "data_stage01_resequencing_omniExpressExome"."GC_Score"
                '''
            subquery1+= '''FROM "data_stage01_resequencing_omniExpressExome" '''
            subquery1+= '''WHERE "data_stage01_resequencing_omniExpressExome"."used_" '''
            if experiment_ids_I:
                cmd_q = '''AND "data_stage01_resequencing_omniExpressExome"."experiment_id" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(experiment_ids_I));
                subquery1+=cmd_q;
            if sample_names_I:
                cmd_q = '''AND "data_stage01_resequencing_omniExpressExome"."sample_name" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(sample_names_I));
                subquery1+=cmd_q;
            subquery1+= '''ORDER BY "data_stage01_resequencing_omniExpressExome"."experiment_id" ASC, '''
            subquery1+= '''"data_stage01_resequencing_omniExpressExome"."sample_name" ASC '''

            query_cmd = '''SELECT "subquery1"."experiment_id",
                "subquery1"."sample_name",
                "subquery1"."SNP_Name",
                "subquery1"."Sample_ID",
                "subquery1"."Allele1_Top",
                "subquery1"."Allele2_Top",
                "subquery1"."GC_Score",
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
                "data_stage01_resequencing_omniExpressExome_annotations"."RefStrand" '''
            query_cmd+= '''FROM "data_stage01_resequencing_omniExpressExome_annotations", (%s) AS subquery1 ''' %subquery1
            query_cmd+= '''WHERE "data_stage01_resequencing_omniExpressExome_annotations"."Name" = "subquery1"."SNP_Name" '''
            query_cmd+= '''ORDER BY "subquery1"."experiment_id" ASC, '''
            query_cmd+= '''"subquery1"."sample_name" ASC, '''
            query_cmd+= '''"data_stage01_resequencing_omniExpressExome_annotations"."Chr" ASC, '''
            query_cmd+= '''"data_stage01_resequencing_omniExpressExome_annotations"."MapInfo" ASC '''
            query_cmd+= ';';

            query_select = sbaas_base_query_select(self.session,self.engine,self.settings)
            data_O = [dict(d) for d in query_select.execute_select(query_cmd)];

        except Exception as e:
            if raise_I: raise;
            else: print(e);

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
    def get_rows_experimentID_dataStage01ResequencingOmniExpressExomeFiltered(self,experiment_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_resequencing_omniExpressExomeFiltered).filter(
                    data_stage01_resequencing_omniExpressExomeFiltered.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_omniExpressExomeFiltered.used_.is_(True)).all();
            rows_O = [d.__repr__dict__() for d in data];
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def get_rows_experimentIDsAndSampleNames_dataStage01ResequencingOmniExpressExomeFiltered(
        self,
        experiment_id_I='',
        sample_names_I='',
        raise_I = False):
        '''Query rows that are used from the analysis        
        INPUT:
        experiment_ids_I = string or list
        sample_names_I = string or list
        OUTPUT:
        data_O = output specified by output_O and dictColumn_I
        '''

        data_O=[]
        try:
            query_cmd = '''SELECT "data_stage01_resequencing_omniExpressExomeFiltered"."id",
                "data_stage01_resequencing_omniExpressExomeFiltered"."experiment_id",
                "data_stage01_resequencing_omniExpressExomeFiltered"."sample_name",
                "data_stage01_resequencing_omniExpressExomeFiltered"."SNP_Name",
                "data_stage01_resequencing_omniExpressExomeFiltered"."GenomeBuild",
                "data_stage01_resequencing_omniExpressExomeFiltered"."Chr",
                "data_stage01_resequencing_omniExpressExomeFiltered"."MapInfo",
                "data_stage01_resequencing_omniExpressExomeFiltered"."mutation_data",
                "data_stage01_resequencing_omniExpressExomeFiltered"."used_",
                "data_stage01_resequencing_omniExpressExomeFiltered"."comment_" '''
            query_cmd+= '''FROM "data_stage01_resequencing_omniExpressExomeFiltered" '''
            #query_cmd+= '''WHERE "data_stage01_resequencing_omniExpressExomeFiltered"."used_" '''
            query_cmd+= '''WHERE '''
            if experiment_id_I:
                cmd_q = '''"data_stage01_resequencing_omniExpressExomeFiltered"."experiment_id" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(experiment_id_I));
                #cmd_q = '''AND "data_stage01_resequencing_omniExpressExomeFiltered"."experiment_id" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(experiment_id_I));
                query_cmd+=cmd_q;
            if sample_names_I:
                cmd_q = '''AND "data_stage01_resequencing_omniExpressExomeFiltered"."sample_name" =ANY ('{%s}'::text[]) ''' %(self.convert_list2string(sample_names_I));
                query_cmd+=cmd_q;
            query_cmd+= '''AND "data_stage01_resequencing_omniExpressExomeFiltered"."Chr"='1' ''' #testing only
            query_cmd+= '''ORDER BY experiment_id ASC, sample_name ASC,
                "Chr" ASC, "MapInfo" ASC '''
            query_cmd+= ';';

            query_select = sbaas_base_query_select(self.session,self.engine,self.settings)
            data_O = [dict(d) for d in query_select.execute_select(query_cmd)];

        except Exception as e:
            if raise_I: raise;
            else: print(e);

        return data_O;