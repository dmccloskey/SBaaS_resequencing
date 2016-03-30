#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_lineage_postgresql_models import *

class stage01_resequencing_lineage_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_resequencing_lineage':data_stage01_resequencing_lineage,
                        };
        self.set_supportedTables(tables_supported);
    # query sample names from data_stage01_resequencing_lineage
    def get_sampleNames_experimentID_dataStage01ResequencingLineage(self,experiment_id_I):
        '''Query samples names from resequencing lineage'''
        try:
            sample_names = self.session.query(data_stage01_resequencing_lineage.experiment_id,
                    data_stage01_resequencing_lineage.sample_name).filter(
                    data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I)).group_by(data_stage01_resequencing_lineage.experiment_id,
                    data_stage01_resequencing_lineage.sample_name).order_by(
                    data_stage01_resequencing_lineage.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: 
                sample_names_O.append(sn.sample_name);
            return sample_names_O
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndLineageName_dataStage01ResequencingLineage(self,experiment_id_I,lineage_name_I):
        '''Query samples names from resequencing lineage'''
        try:
            data = self.session.query(data_stage01_resequencing_lineage.experiment_id,
                    data_stage01_resequencing_lineage.sample_name).filter(
                    data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_lineage.lineage_name.like(lineage_name_I)).group_by(
                    data_stage01_resequencing_lineage.experiment_id,
                    data_stage01_resequencing_lineage.sample_name).order_by(
                    data_stage01_resequencing_lineage.lineage_name.asc()).all();
            data_O = [];
            for d in data: 
                #data_tmp = {};
                #data_tmp['sample_name']=d.sample_name;
                #data_O.append(data_tmp);
                data_O.append(d.sample_name);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # Query intermediates from data_stage01_resequencing_lineage
    def get_intermediates_experimentIDAndLineageName_dataStage01ResequencingLineage(self,experiment_id_I,lineage_name_I):
        '''Query intermediates from resequencing lineage'''
        try:
            data = self.session.query(data_stage01_resequencing_lineage.experiment_id,
                    data_stage01_resequencing_lineage.intermediate).filter(
                    data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_lineage.lineage_name.like(lineage_name_I)).group_by(
                    data_stage01_resequencing_lineage.experiment_id,
                    data_stage01_resequencing_lineage.intermediate).order_by(
                    data_stage01_resequencing_lineage.intermediate.asc()).all();
            data_O = [];
            for d in data: 
                #data_tmp = {};
                #data_tmp['intermediate']=d.intermediate;
                #data_O.append(data_tmp);
                data_O.append(d.intermediate);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query mutation information from data_stage01_resequencing_lineage
    def get_mutationData_experimentIDAndLineageName_dataStage01ResequencingLineage(self,experiment_id_I,lineage_name_I):
        '''Query mutation information from resequencing lineage'''
        try:
            data = self.session.query(data_stage01_resequencing_lineage.mutation_type,
                    data_stage01_resequencing_lineage.mutation_position,
                    data_stage01_resequencing_lineage.mutation_genes,
                    data_stage01_resequencing_lineage.mutation_locations).filter(
                    data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_lineage.lineage_name.like(lineage_name_I)).group_by(
                    data_stage01_resequencing_lineage.mutation_type,
                    data_stage01_resequencing_lineage.mutation_position,
                    data_stage01_resequencing_lineage.mutation_genes,
                    data_stage01_resequencing_lineage.mutation_locations).order_by(
                    data_stage01_resequencing_lineage.mutation_type.asc(),
                    data_stage01_resequencing_lineage.mutation_position.asc(),
                    data_stage01_resequencing_lineage.mutation_genes.asc(),
                    data_stage01_resequencing_lineage.mutation_locations.asc()).all();
            data_O = [];
            for d in data: 
                #data_tmp = {};
                #data_tmp['mutation_type']=d.mutation_type;
                #data_tmp['mutation_position']=d.mutation_position;
                #data_tmp['mutation_genes']=d.mutation_genes;
                #data_tmp['mutation_locations']=d.mutation_locations;
                #data_O.append(data_tmp);
                data_tmp_str = '';
                mutation_genes_str = '';
                for gene in d.mutation_genes:
                    mutation_genes_str = mutation_genes_str + gene + '-/-'
                mutation_genes_str = mutation_genes_str[:-3];
                #mutation_locations_str = '';
                #for location in d.mutation_locations:
                #    mutation_locations_str = mutation_locations_str + location + '&'
                #mutation_locations_str = mutation_locations_str[:-1];
                data_tmp_str = d.mutation_type+'_'+mutation_genes_str+'_'+str(d.mutation_position)
                data_O.append(data_tmp_str);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query row from data_stage01_resequencing_lineage
    def get_row_experimentIDAndSampleName_dataStage01ResequencingLineage(self,experiment_id_I,sample_name_I):
        '''Query samples names from resequencing lineage'''
        try:
            data = self.session.query(data_stage01_resequencing_lineage).filter(
                    data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_lineage.sample_name.like(sample_name_I)).all();
            data_O = [];
            for d in data: 
                data_tmp = {};
                data_tmp['id']=d.id;
                data_tmp['experiment_id']=d.experiment_id;
                data_tmp['lineage_name']=d.lineage_name;
                data_tmp['sample_name']=d.sample_name;
                data_tmp['intermediate']=d.intermediate;
                data_tmp['mutation_frequency']=d.mutation_frequency;
                data_tmp['mutation_type']=d.mutation_type;
                data_tmp['mutation_position']=d.mutation_position;
                data_tmp['mutation_data']=d.mutation_data;
                data_tmp['mutation_annotations']=d.mutation_annotations;
                data_tmp['mutation_genes']=d.mutation_genes;
                data_tmp['mutation_locations']=d.mutation_locations;
                data_tmp['mutation_links']=d.mutation_links;
                data_tmp['comment_']=d.comment_;
                data_O.append(data_tmp);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_experimentIDAndLineageName_dataStage01ResequencingLineage(self,experiment_id_I,lineage_name_I):
        '''Query samples names from resequencing lineage'''
        try:
            data = self.session.query(data_stage01_resequencing_lineage).filter(
                    data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_lineage.lineage_name.like(lineage_name_I)).all();
            data_O = [];
            for d in data: 
                data_tmp = {};
                data_tmp['id']=d.id;
                data_tmp['experiment_id']=d.experiment_id;
                data_tmp['lineage_name']=d.lineage_name;
                data_tmp['sample_name']=d.sample_name;
                data_tmp['intermediate']=d.intermediate;
                data_tmp['mutation_frequency']=d.mutation_frequency;
                data_tmp['mutation_type']=d.mutation_type;
                data_tmp['mutation_position']=d.mutation_position;
                data_tmp['mutation_data']=d.mutation_data;
                data_tmp['mutation_annotations']=d.mutation_annotations;
                data_tmp['mutation_genes']=d.mutation_genes;
                data_tmp['mutation_locations']=d.mutation_locations;
                data_tmp['mutation_links']=d.mutation_links;
                data_tmp['comment_']=d.comment_;
                data_tmp_str = '';
                mutation_genes_str = '';
                for gene in d.mutation_genes:
                    mutation_genes_str = mutation_genes_str + gene + '-/-'
                mutation_genes_str = mutation_genes_str[:-3];
                #mutation_locations_str = '';
                #for location in d.mutation_locations:
                #    mutation_locations_str = mutation_locations_str + location + '&'
                #mutation_locations_str = mutation_locations_str[:-1];
                data_tmp_str = d.mutation_type+'_'+mutation_genes_str+'_'+str(d.mutation_position)
                data_tmp['mutation_id'] = data_tmp_str;
                data_O.append(data_tmp);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsIO_lineageName_dataStage01ResequencingLineage(self,lineage_name_I):
        '''Query rows from resequencing lineage
        for visualization, mutation_data is omitted'''
        try:
            data = self.session.query(data_stage01_resequencing_lineage).filter(
                    data_stage01_resequencing_lineage.lineage_name.like(lineage_name_I)).order_by(
                    data_stage01_resequencing_lineage.sample_name.asc()).all();
            data_O = [];
            for d in data: 
                data_tmp = {};
                data_tmp['id']=d.id;
                data_tmp['experiment_id']=d.experiment_id;
                data_tmp['lineage_name']=d.lineage_name;
                data_tmp['sample_name']=d.sample_name;
                data_tmp['intermediate']=d.intermediate;
                data_tmp['mutation_frequency']=d.mutation_frequency;
                data_tmp['mutation_type']=d.mutation_type;
                data_tmp['mutation_position']=d.mutation_position;
                #data_tmp['mutation_data']=d.mutation_data;
                data_tmp['mutation_annotations']=d.mutation_annotations;
                data_tmp['mutation_genes']=d.mutation_genes;
                data_tmp['mutation_locations']=d.mutation_locations;
                data_tmp['mutation_links']=d.mutation_links;
                data_tmp['comment_']=d.comment_;
                data_tmp_str = '';
                mutation_genes_str = '';
                for gene in d.mutation_genes:
                    mutation_genes_str = mutation_genes_str + gene + '-/-'
                mutation_genes_str = mutation_genes_str[:-3];
                #mutation_locations_str = '';
                #for location in d.mutation_locations:
                #    mutation_locations_str = mutation_locations_str + location + '&'
                #mutation_locations_str = mutation_locations_str[:-1];
                data_tmp_str = d.mutation_type+'_'+mutation_genes_str+'_'+str(d.mutation_position)
                data_tmp['mutation_id'] = data_tmp_str;
                data_O.append(data_tmp);
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01ResequencingLineage(self, data_I):
        '''add rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_lineage(d['experiment_id'],
                                d['lineage_name'],
                                d['sample_name'],
                                d['intermediate'],
                                d['mutation_frequency'],
                                d['mutation_type'],
                                d['mutation_position'],
                                d['mutation_data'],
                                d['mutation_annotations'],
                                d['mutation_genes'],
                                d['mutation_locations'],
                                d['mutation_links'],
                                d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01ResequencingLineage(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    #if d['mutation_genes']:
                    #    d['mutation_genes']=d['mutation_genes'].split();
                    #if d['mutation_location']:
                    #    d['mutation_location']=d['mutation_location'].split();
                    data_update = self.session.query(data_stage01_resequencing_lineage).filter(
                           data_stage01_resequencing_lineage.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                                'lineage_name':d['lineage_name'],
                                'sample_name':d['sample_name'],
                                'intermediate':d['intermediate'],
                                'mutation_frequency':d['mutation_frequency'],
                                'mutation_type':d['mutation_type'],
                                'mutation_position':d['mutation_position'],
                                'mutation_data':d['mutation_data'],
                                'mutation_annotations':d['mutation_annotations'],
                                'mutation_genes':d['mutation_genes'],
                                'mutation_locations':d['mutation_locations'],
                                'mutation_links':d['mutation_links'],
                                'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage01_resequencing_lineage(self):
        try:
            data_stage01_resequencing_lineage.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_lineage(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_lineage).filter(data_stage01_resequencing_lineage.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            #else:
            #    reset = self.session.query(data_stage01_resequencing_lineage).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_resequencing_lineage(self):
        try:
            data_stage01_resequencing_lineage.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);