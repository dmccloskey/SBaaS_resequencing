#sbaas
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#sbaas models
from .stage01_resequencing_coverage_postgresql_models import *

class stage01_resequencing_coverage_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {
            'data_stage01_resequencing_amplificationAnnotations':data_stage01_resequencing_amplificationAnnotations,
            'data_stage01_resequencing_amplifications':data_stage01_resequencing_amplifications,
            'data_stage01_resequencing_amplificationStats':data_stage01_resequencing_amplificationStats,
            'data_stage01_resequencing_coverage':data_stage01_resequencing_coverage,
            'data_stage01_resequencing_coverageStats':data_stage01_resequencing_coverageStats,
                        };
        self.set_supportedTables(tables_supported);
    def drop_dataStage01_resequencing_coverage(self):
        try:
            data_stage01_resequencing_coverage.__table__.drop(self.engine,True);
            data_stage01_resequencing_coverageStats.__table__.drop(self.engine,True);
            data_stage01_resequencing_amplifications.__table__.drop(self.engine,True);
            data_stage01_resequencing_amplificationStats.__table__.drop(self.engine,True);
            data_stage01_resequencing_amplificationAnnotations.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_resequencing_coverage(self):
        try:
            data_stage01_resequencing_coverage.__table__.create(self.engine,True);
            data_stage01_resequencing_coverageStats.__table__.create(self.engine,True);
            data_stage01_resequencing_amplifications.__table__.create(self.engine,True);
            data_stage01_resequencing_amplificationStats.__table__.create(self.engine,True);
            data_stage01_resequencing_amplificationAnnotations.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_coverage(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_resequencing_coverage).filter(
                        data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_coverage.sample_name.like(sn)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_resequencing_coverageStats).filter(
                        data_stage01_resequencing_coverageStats.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_coverageStats.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_coverage).filter(data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_coverageStats).filter(data_stage01_resequencing_coverageStats.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_coverage).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_coverageStats).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_amplifications(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_resequencing_amplifications).filter(
                        data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplifications.sample_name.like(sn)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_resequencing_amplificationStats).filter(
                        data_stage01_resequencing_amplificationStats.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplificationStats.sample_name.like(sn)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(
                        data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplificationAnnotations.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_amplifications).filter(data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationStats).filter(data_stage01_resequencing_amplificationStats.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_amplifications).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationStats).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_resequencing_amplificationAnnotations(self,experiment_id_I = None, sample_names_I=[]):
        try:
            if experiment_id_I and sample_names_I:
                for sn in sample_names_I:
                    reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(
                        data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I),
                        data_stage01_resequencing_amplificationAnnotations.sample_name.like(sn)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_resequencing_amplificationAnnotations).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def add_dataStage01ResequencingCoverage(self, data_I):
        '''add rows of data_stage01_resequencing_coverage'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_coverage(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['data_dir'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['genome_index'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['reads'],
                    d['scale_factor'],
                    d['downsample_factor'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingCoverageStats(self, data_I):
        '''add rows of data_stage01_resequencing_coverageStats'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_coverageStats(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['reads_min'],
                    d['reads_max'],
                    d['reads_lb'],
                    d['reads_ub'],
                    d['reads_iq1'],
                    d['reads_iq3'],
                    d['reads_median'],
                    d['reads_mean'],
                    d['reads_var'],
                    d['reads_n'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingAmplifications(self, data_I):
        '''add rows of data_stage01_resequencing_amplifications'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_amplifications(
                        #d['analysis_id'],
                        d['experiment_id'],
                        d['sample_name'],
                        d['genome_chromosome'],
                        d['genome_strand'],
                        d['genome_index'],
                        d['strand_start'],
                        d['strand_stop'],
                        d['reads'],
                        d['reads_min'],
                        d['reads_max'],
                        d['indices_min'],
                        d['consecutive_tol'],
                        d['scale_factor'],
                        d['downsample_factor'],
                        d['amplification_start'],
                        d['amplification_stop'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingAmplificationStats(self, data_I):
        '''add rows of data_stage01_resequencing_amplificationStats'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_amplificationStats(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['reads_min'],
                    d['reads_max'],
                    d['reads_lb'],
                    d['reads_ub'],
                    d['reads_iq1'],
                    d['reads_iq3'],
                    d['reads_median'],
                    d['reads_mean'],
                    d['reads_var'],
                    d['reads_n'],
                    d['amplification_start'],
                    d['amplification_stop'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01ResequencingAmplificationAnnotations(self, data_I):
        '''add rows of data_stage01_resequencing_amplificationAnnotations'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_resequencing_amplificationAnnotations(
                    #d['analysis_id'],
                    d['experiment_id'],
                    d['sample_name'],
                    d['genome_chromosome'],
                    d['genome_strand'],
                    d['strand_start'],
                    d['strand_stop'],
                    d['feature_annotations'],
                    d['feature_genes'],
                    d['feature_locations'],
                    d['feature_links'],
                    d['feature_start'],
                    d['feature_stop'],
                    d['feature_types'],
                    d['amplification_start'],
                    d['amplification_stop'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingCoverage(self,data_I):
        '''update rows of data_stage01_resequencing_coverage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_coverage).filter(
                           data_stage01_resequencing_coverage.id==d['id']).update(
                            {
                                #'analysis_id':d['analysis_id'],
                             'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'data_dir':d['data_dir'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'genome_index':d['genome_index'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads':d['reads'],
                            'scale_factor':d['scale_factor'],
                            'downsample_factor':d['downsample_factor'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingCoverageStats(self,data_I):
        '''update rows of data_stage01_resequencing_coverageStats'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_coverageStats).filter(
                           data_stage01_resequencing_coverageStats.id==d['id']).update(
                            {
                                #'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads_min':d['reads_min'],
                            'reads_max':d['reads_max'],
                            'reads_lb':d['reads_lb'],
                            'reads_ub':d['reads_ub'],
                            'reads_iq1':d['reads_iq1'],
                            'reads_iq3':d['reads_iq3'],
                            'reads_median':d['reads_median'],
                            'reads_mean':d['reads_mean'],
                            'reads_var':d['reads_var'],
                            'reads_n':d['reads_n'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingAmplifications(self,data_I):
        '''update rows of data_stage01_resequencing_amplifications'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_amplifications).filter(
                           data_stage01_resequencing_amplifications.id==d['id']).update(
                            {
                            #'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'genome_index':d['genome_index'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads':d['reads'],
                            'reads_min':d['reads_min'],
                            'reads_max':d['reads_max'],
                            'indices_min':d['indices_min'],
                            'consecutive_tol':d['consecutive_tol'],
                            'scale_factor':d['scale_factor'],
                            'downsample_factor':d['downsample_factor'],
                            'amplification_start':d['amplification_start'],
                            'amplification_stop':d['amplification_stop'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01ResequencingAmplificationStats(self,data_I):
        '''update rows of data_stage01_resequencing_amplificationStats'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_resequencing_amplificationStats).filter(
                           data_stage01_resequencing_amplificationStats.id==d['id']).update(
                            {
                            #'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'genome_chromosome':d['genome_chromosome'],
                            'genome_strand':d['genome_strand'],
                            'strand_start':d['strand_start'],
                            'strand_stop':d['strand_stop'],
                            'reads_min':d['reads_min'],
                            'reads_max':d['reads_max'],
                            'reads_lb':d['reads_lb'],
                            'reads_ub':d['reads_ub'],
                            'reads_iq1':d['reads_iq1'],
                            'reads_iq3':d['reads_iq3'],
                            'reads_median':d['reads_median'],
                            'reads_mean':d['reads_mean'],
                            'reads_var':d['reads_var'],
                            'reads_n':d['reads_n'],
                            'amplification_start':d['amplification_start'],
                            'amplification_stop':d['amplification_stop'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    # query data from data_stage01_resequencing_coverage
    def get_sampleNames_experimentID_dataStage01ResequencingCoverage(self,experiment_id_I):
        '''Query sample names by experiment_id from data_stage01_resequencing_coverage'''
        try:
            data = self.session.query(data_stage01_resequencing_coverage.sample_name).filter(
                    data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_coverage.used_).group_by(
                    data_stage01_resequencing_coverage.sample_name).order_by(
                    data_stage01_resequencing_coverage.sample_name.asc()).all();
            data_O = [];
            for d in data: 
                data_O.append(d.sample_name);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(self,experiment_id_I,sample_name_I):
        '''Query data_dirs by experiment_id and sample_name from data_stage01_resequencing_coverage'''
        try:
            data = self.session.query(data_stage01_resequencing_coverage.data_dir).filter(
                    data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_coverage.sample_name.like(sample_name_I),
                    data_stage01_resequencing_coverage.used_).group_by(
                    data_stage01_resequencing_coverage.data_dir).order_by(
                    data_stage01_resequencing_coverage.data_dir.asc()).all();
            data_O = [];
            for d in data: 
                data_O.append(d.data_dir);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverage(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_coverage'''
        try:
            data = self.session.query(data_stage01_resequencing_coverage).filter(
                    data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_coverage.sample_name.like(sample_name_I),
                    data_stage01_resequencing_coverage.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'data_dir':d.data_dir,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'genome_index':d.genome_index,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'reads':d.reads,
                'scale_factor':d.scale_factor,
                'downsample_factor':d.downsample_factor,
                'used_':d.used_,
                'comment_':d.comment_}
                              );
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverage_visualization(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_coverage'''
        try:
            data = self.session.query(data_stage01_resequencing_coverage).filter(
                    data_stage01_resequencing_coverage.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_coverage.sample_name.like(sample_name_I),
                    data_stage01_resequencing_coverage.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'data_dir':d.data_dir,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'genome_index':d.genome_index,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'reads':d.reads,
                'scale_factor':d.scale_factor,
                'downsample_factor':d.downsample_factor,
                'used_':d.used_,
                'comment_':d.comment_,
                'sample_name_strand':"_".join([d.sample_name,d.genome_strand])}
                              );
            return data_O;
        except SQLAlchemyError as e:
            print(e);
            
    # query data from data_stage01_resequencing_coverageStats
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverageStats(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_coverageStats'''
        try:
            data = self.session.query(data_stage01_resequencing_coverageStats).filter(
                    data_stage01_resequencing_coverageStats.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_coverageStats.sample_name.like(sample_name_I),
                    data_stage01_resequencing_coverageStats.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'reads_min':d.reads_min,
                'reads_max':d.reads_max,
                'reads_lb':d.reads_lb,
                'reads_ub':d.reads_ub,
                'reads_iq1':d.reads_iq1,
                'reads_iq3':d.reads_iq3,
                'reads_median':d.reads_median,
                'reads_mean':d.reads_mean,
                'reads_var':d.reads_var,
                'reads_n':d.reads_n,
                'used_':d.used_,
                'comment_':d.comment_});
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    # query data from data_stage01_resequencing_amplifications
    def get_sampleNames_experimentID_dataStage01ResequencingAmplifications(self,experiment_id_I):
        '''Query sample names by experiment_id from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.sample_name).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.sample_name).order_by(
                    data_stage01_resequencing_amplifications.sample_name.asc()).all();
            data_O = [];
            for d in data: 
                data_O.append(d.sample_name);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_chromosomes_experimentIDAndSampleName_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I):
        '''Query chromosomes by experiment_id and sample_name from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.genome_chromosome).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.genome_chromosome).order_by(
                    data_stage01_resequencing_amplifications.genome_chromosome.asc()).all();
            data_O = [];
            for d in data: 
                data_O.append(d.genome_chromosome);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_strands_experimentIDAndSampleNameAndChromosome_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I,chromosome_I):
        '''Query strands by experiment_id and sample_name and chromosome from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.genome_strand).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.genome_chromosome==chromosome_I,
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.genome_strand).order_by(
                    data_stage01_resequencing_amplifications.genome_strand.asc()).all();
            data_O = [];
            for d in data: 
                data_O.append(d.genome_strand);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_startAndStops_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I,chromosome_I,strand_I):
        '''Query start and stop by experiment_id and sample_name and chromosome and strand from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.strand_start,
                    data_stage01_resequencing_amplifications.strand_stop).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.genome_chromosome==chromosome_I,
                    data_stage01_resequencing_amplifications.genome_strand.like(strand_I),
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.strand_start,
                    data_stage01_resequencing_amplifications.strand_stop).order_by(
                    data_stage01_resequencing_amplifications.strand_start.asc()).all();
            start_O = [];
            stop_O = [];
            for d in data: 
                start_O.append(d.strand_start);
                stop_O.append(d.strand_stop);
            return start_O,stop_O;
        except SQLAlchemyError as e:
            print(e);
    def get_genomeIndexAndReads_experimentIDAndSampleNameAndChromosomeAndStrandAndStartAndStop_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I,chromosome_I,strand_I,start_I,stop_I):
        '''Query index and reads by experiment_id and sample_name and chromosome and strand and start and stop from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.genome_index,
                    data_stage01_resequencing_amplifications.reads).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.genome_chromosome==chromosome_I,
                    data_stage01_resequencing_amplifications.genome_strand.like(strand_I),
                    data_stage01_resequencing_amplifications.strand_start==start_I,
                    data_stage01_resequencing_amplifications.strand_stop==stop_I,
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.genome_index,
                    data_stage01_resequencing_amplifications.reads).order_by(
                    data_stage01_resequencing_amplifications.genome_index.asc()).all();
            genome_index_O = [];
            reads_O = [];
            for d in data: 
                genome_index_O.append(d.genome_index);
                reads_O.append(d.reads);
            return genome_index_O,reads_O;
        except SQLAlchemyError as e:
            print(e);
    def get_amplificationRegions_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I,chromosome_I,strand_I):
        '''Query start and stop by experiment_id and sample_name and chromosome and strand from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.amplification_start,
                    data_stage01_resequencing_amplifications.amplification_stop).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.genome_chromosome==chromosome_I,
                    data_stage01_resequencing_amplifications.genome_strand.like(strand_I),
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.amplification_start,
                    data_stage01_resequencing_amplifications.amplification_stop).order_by(
                    data_stage01_resequencing_amplifications.amplification_start.asc()).all();
            start_O = [];
            stop_O = [];
            for d in data: 
                start_O.append(d.amplification_start);
                stop_O.append(d.amplification_stop);
            return start_O,stop_O;
        except SQLAlchemyError as e:
            print(e);
    def get_genomeIndexAndReads_experimentIDAndSampleNameAndChromosomeAndStrandAndAmplificationRegions_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I,chromosome_I,strand_I,start_I,stop_I):
        '''Query index and reads by experiment_id and sample_name and chromosome and strand and start and stop from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications.genome_index,
                    data_stage01_resequencing_amplifications.reads).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.genome_chromosome==chromosome_I,
                    data_stage01_resequencing_amplifications.genome_strand.like(strand_I),
                    data_stage01_resequencing_amplifications.amplification_start==start_I,
                    data_stage01_resequencing_amplifications.amplification_stop==stop_I,
                    data_stage01_resequencing_amplifications.used_).group_by(
                    data_stage01_resequencing_amplifications.genome_index,
                    data_stage01_resequencing_amplifications.reads).order_by(
                    data_stage01_resequencing_amplifications.genome_index.asc()).all();
            genome_index_O = [];
            reads_O = [];
            for d in data: 
                genome_index_O.append(d.genome_index);
                reads_O.append(d.reads);
            return genome_index_O,reads_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplifications(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'genome_index':d.genome_index,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'reads':d.reads,
                'reads_min':d.reads_min,
                'reads_max':d.reads_max,
                'indices_min':d.indices_min,
                'consecutive_tol':d.consecutive_tol,
                'scale_factor':d.scale_factor,
                'downsample_factor':d.downsample_factor,
                'amplification_start':d.amplification_start,
                'amplification_stop':d.amplification_stop,
                'used_':d.used_,
                'comment_':d.comment_});
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplifications_visualization(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_amplifications'''
        try:
            data = self.session.query(data_stage01_resequencing_amplifications).filter(
                    data_stage01_resequencing_amplifications.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplifications.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplifications.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'genome_index':d.genome_index,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'reads':d.reads,
                'reads_min':d.reads_min,
                'reads_max':d.reads_max,
                'indices_min':d.indices_min,
                'consecutive_tol':d.consecutive_tol,
                'scale_factor':d.scale_factor,
                'downsample_factor':d.downsample_factor,
                'amplification_start':d.amplification_start,
                'amplification_stop':d.amplification_stop,
                'used_':d.used_,
                'comment_':d.comment_,
                'sample_name_strand':"_".join([d.sample_name,d.genome_strand])});
            return data_O;
        except SQLAlchemyError as e:
            print(e);
            
    # query data from data_stage01_resequencing_amplifications
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationStats(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_amplificationStats'''
        try:
            data = self.session.query(data_stage01_resequencing_amplificationStats).filter(
                    data_stage01_resequencing_amplificationStats.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplificationStats.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplificationStats.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'reads_min':d.reads_min,
                'reads_max':d.reads_max,
                'reads_lb':d.reads_lb,
                'reads_ub':d.reads_ub,
                'reads_iq1':d.reads_iq1,
                'reads_iq3':d.reads_iq3,
                'reads_median':d.reads_median,
                'reads_mean':d.reads_mean,
                'reads_var':d.reads_var,
                'reads_n':d.reads_n,
                'amplification_start':d.amplification_start,
                'amplification_stop':d.amplification_stop,
                'used_':d.used_,
                'comment_':d.comment_
                    });
            return data_O;
        except SQLAlchemyError as e:
            print(e);
            
    # query data from data_stage01_resequencing_amplificationAnnotations
    def get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationAnnotations(self,experiment_id_I,sample_name_I):
        '''Query rows by experiment_id and sample_name from data_stage01_resequencing_amplificationAnnotations'''
        try:
            data = self.session.query(data_stage01_resequencing_amplificationAnnotations).filter(
                    data_stage01_resequencing_amplificationAnnotations.experiment_id.like(experiment_id_I),
                    data_stage01_resequencing_amplificationAnnotations.sample_name.like(sample_name_I),
                    data_stage01_resequencing_amplificationAnnotations.used_).all();
            data_O = [];
            for d in data: 
                data_O.append({'id':d.id,
                #'analysis_id':d.analysis_id,
                'experiment_id':d.experiment_id,
                'sample_name':d.sample_name,
                'genome_chromosome':d.genome_chromosome,
                'genome_strand':d.genome_strand,
                'strand_start':d.strand_start,
                'strand_stop':d.strand_stop,
                'feature_annotations':d.feature_annotations,
                'feature_genes':d.feature_genes,
                'feature_locations':d.feature_locations,
                'feature_links':d.feature_links,
                'feature_start':d.feature_start,
                'feature_stop':d.feature_stop,
                'feature_types':d.feature_types,
                'amplification_start':d.amplification_start,
                'amplification_stop':d.amplification_stop,
                'used_':d.used_,
                'comment_':d.comment_});
            return data_O;
        except SQLAlchemyError as e:
            print(e);