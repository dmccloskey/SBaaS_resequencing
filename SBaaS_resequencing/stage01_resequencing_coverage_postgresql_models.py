from SBaaS_base.postgresql_orm_base import *

class data_stage01_resequencing_coverage(Base):
    
    __tablename__ = 'data_stage01_resequencing_coverage'
    id = Column(Integer, Sequence('data_stage01_resequencing_coverage_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    data_dir = Column(String(500)); #
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    genome_index = Column(Integer);
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads = Column(Float);
    scale_factor = Column(Boolean);
    downsample_factor = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.data_dir=row_dict_I['data_dir'];
        self.genome_chromosome=row_dict_I['genome_chromosome'];
        self.genome_strand=row_dict_I['genome_strand'];
        self.genome_index=row_dict_I['genome_index'];
        self.strand_start=row_dict_I['strand_start'];
        self.strand_stop=row_dict_I['strand_stop'];
        self.reads=row_dict_I['reads'];
        self.scale_factor=row_dict_I['scale_factor'];
        self.downsample_factor=row_dict_I['downsample_factor'];

    def __set__row__(self, 
        #analysis_id_I, 
        experiment_id_I,
        sample_name_I,
        data_dir_I,
        genome_chromosome_I,
        genome_strand_I,
        genome_index_I,
        strand_start_I,
        strand_stop_I,
        reads_I,
        scale_factor_I,
        downsample_factor_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.data_dir=data_dir_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.genome_index=genome_index_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads=reads_I
        self.scale_factor=scale_factor_I
        self.downsample_factor=downsample_factor_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'data_dir':self.data_dir,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'genome_index':self.genome_index,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads':self.reads,
                'scale_factor':self.scale_factor,
                'downsample_factor':self.downsample_factor,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_coverageStats(Base):
    
    __tablename__ = 'data_stage01_resequencing_coverageStats'
    id = Column(Integer, Sequence('data_stage01_resequencing_coverageStats_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads_min = Column(Float);
    reads_max = Column(Float);
    reads_lb = Column(Float);
    reads_ub = Column(Float);
    reads_iq1 = Column(Float);
    reads_iq3 = Column(Float);
    reads_median = Column(Float);
    reads_mean = Column(Float);
    reads_var = Column(Float);
    reads_n = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.reads_median=row_dict_I['reads_median'];
        self.reads_iq3=row_dict_I['reads_iq3'];
        self.strand_start=row_dict_I['strand_start'];
        self.strand_stop=row_dict_I['strand_stop'];
        self.reads_min=row_dict_I['reads_min'];
        self.reads_max=row_dict_I['reads_max'];
        self.reads_lb=row_dict_I['reads_lb'];
        self.reads_ub=row_dict_I['reads_ub'];
        self.reads_iq1=row_dict_I['reads_iq1'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.reads_n=row_dict_I['reads_n'];
        self.reads_var=row_dict_I['reads_var'];
        self.reads_mean=row_dict_I['reads_mean'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.genome_chromosome=row_dict_I['genome_chromosome'];
        self.genome_strand=row_dict_I['genome_strand'];

    def __set__row__(self, 
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        strand_start_I,
        strand_stop_I,
        reads_min_I,
        reads_max_I,
        reads_lb_I,
        reads_ub_I,
        reads_iq1_I,
        reads_iq3_I,
        reads_median_I,
        reads_mean_I,
        reads_var_I,
        reads_n_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads_min=reads_min_I
        self.reads_max=reads_max_I
        self.reads_lb=reads_lb_I
        self.reads_ub=reads_ub_I
        self.reads_iq1=reads_iq1_I
        self.reads_iq3=reads_iq3_I
        self.reads_median=reads_median_I
        self.reads_mean=reads_mean_I
        self.reads_var=reads_var_I
        self.reads_n=reads_n_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads_min':self.reads_min,
                'reads_max':self.reads_max,
                'reads_lb':self.reads_lb,
                'reads_ub':self.reads_ub,
                'reads_iq1':self.reads_iq1,
                'reads_iq3':self.reads_iq3,
                'reads_median':self.reads_median,
                'reads_mean':self.reads_mean,
                'reads_var':self.reads_var,
                'reads_n':self.reads_n,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_amplifications(Base):
    
    __tablename__ = 'data_stage01_resequencing_amplifications'
    id = Column(Integer, Sequence('data_stage01_resequencing_amplifications_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    genome_index = Column(Integer);
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads = Column(Float);
    reads_min = Column(Float);
    reads_max = Column(Float);
    indices_min = Column(Integer);
    consecutive_tol = Column(Integer);
    scale_factor = Column(Boolean);
    downsample_factor = Column(Integer);
    amplification_start = Column(Integer);
    amplification_stop = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','genome_index'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.reads_max=row_dict_I['reads_max'];
        self.reads_min=row_dict_I['reads_min'];
        self.indices_min=row_dict_I['indices_min'];
        self.consecutive_tol=row_dict_I['consecutive_tol'];
        self.used_=row_dict_I['used_'];
        self.amplification_stop=row_dict_I['amplification_stop'];
        self.amplification_start=row_dict_I['amplification_start'];
        self.downsample_factor=row_dict_I['downsample_factor'];
        self.scale_factor=row_dict_I['scale_factor'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.genome_chromosome=row_dict_I['genome_chromosome'];
        self.genome_strand=row_dict_I['genome_strand'];
        self.comment_=row_dict_I['comment_'];
        self.genome_index=row_dict_I['genome_index'];
        self.strand_start=row_dict_I['strand_start'];
        self.strand_stop=row_dict_I['strand_stop'];
        self.reads=row_dict_I['reads'];

    def __set__row__(self, 
        #analysis_id_I, 
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        genome_index_I,
        strand_start_I,
        strand_stop_I,
        reads_I,
        reads_min_I,
        reads_max_I,
        indices_min_I,
        consecutive_tol_I,
        scale_factor_I,
        downsample_factor_I,
        amplification_start_I,
        amplification_stop_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.genome_index=genome_index_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads=reads_I
        self.reads_min=reads_min_I
        self.reads_max=reads_max_I
        self.indices_min=indices_min_I
        self.consecutive_tol=consecutive_tol_I
        self.scale_factor=scale_factor_I
        self.downsample_factor=downsample_factor_I
        self.amplification_start=amplification_start_I
        self.amplification_stop=amplification_stop_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'genome_index':self.genome_index,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads':self.reads,
                'reads_min':self.reads_min,
                'reads_max':self.reads_max,
                'indices_min':self.indices_min,
                'consecutive_tol':self.consecutive_tol,
                'scale_factor':self.scale_factor,
                'downsample_factor':self.downsample_factor,
                'amplification_start':self.amplification_start,
                'amplification_stop':self.amplification_stop,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_amplificationStats(Base):
    
    __tablename__ = 'data_stage01_resequencing_amplificationStats'
    id = Column(Integer, Sequence('data_stage01_resequencing_amplificationStats_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    reads_min = Column(Float);
    reads_max = Column(Float);
    reads_lb = Column(Float);
    reads_ub = Column(Float);
    reads_iq1 = Column(Float);
    reads_iq3 = Column(Float);
    reads_median = Column(Float);
    reads_mean = Column(Float);
    reads_var = Column(Float);
    reads_n = Column(Float);
    amplification_start = Column(Integer);
    amplification_stop = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.genome_chromosome=row_dict_I['genome_chromosome'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.strand_stop=row_dict_I['strand_stop'];
        self.reads_min=row_dict_I['reads_min'];
        self.reads_max=row_dict_I['reads_max'];
        self.reads_lb=row_dict_I['reads_lb'];
        self.reads_ub=row_dict_I['reads_ub'];
        self.reads_iq1=row_dict_I['reads_iq1'];
        self.reads_iq3=row_dict_I['reads_iq3'];
        self.reads_median=row_dict_I['reads_median'];
        self.reads_mean=row_dict_I['reads_mean'];
        self.reads_var=row_dict_I['reads_var'];
        self.reads_n=row_dict_I['reads_n'];
        self.amplification_start=row_dict_I['amplification_start'];
        self.amplification_stop=row_dict_I['amplification_stop'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.strand_start=row_dict_I['strand_start'];
        self.genome_strand=row_dict_I['genome_strand'];
        self.sample_name=row_dict_I['sample_name'];

    def __set__row__(self,
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        strand_start_I,
        strand_stop_I,
        reads_min_I,
        reads_max_I,
        reads_lb_I,
        reads_ub_I,
        reads_iq1_I,
        reads_iq3_I,
        reads_median_I,
        reads_mean_I,
        reads_var_I,
        reads_n_I,
        amplification_start_I,
        amplification_stop_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.reads_min=reads_min_I
        self.reads_max=reads_max_I
        self.reads_lb=reads_lb_I
        self.reads_ub=reads_ub_I
        self.reads_iq1=reads_iq1_I
        self.reads_iq3=reads_iq3_I
        self.reads_median=reads_median_I
        self.reads_mean=reads_mean_I
        self.reads_var=reads_var_I
        self.reads_n=reads_n_I
        self.amplification_start=amplification_start_I
        self.amplification_stop=amplification_stop_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'reads_min':self.reads_min,
                'reads_max':self.reads_max,
                'reads_lb':self.reads_lb,
                'reads_ub':self.reads_ub,
                'reads_iq1':self.reads_iq1,
                'reads_iq3':self.reads_iq3,
                'reads_median':self.reads_median,
                'reads_mean':self.reads_mean,
                'reads_var':self.reads_var,
                'reads_n':self.reads_n,
                'amplification_start':self.amplification_start,
                'amplification_stop':self.amplification_stop,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_amplificationAnnotations(Base):
    
    __tablename__ = 'data_stage01_resequencing_amplificationAnnotations'
    id = Column(Integer, Sequence('data_stage01_resequencing_amplificationAnnotations_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    genome_chromosome = Column(Integer); # e.g., 1
    genome_strand = Column(String(25)); # plus or minus
    strand_start = Column(Integer);
    strand_stop = Column(Integer);
    feature_annotations = Column(postgresql.ARRAY(String(500)))
    feature_genes = Column(postgresql.ARRAY(String(25)))
    feature_locations = Column(postgresql.ARRAY(String(100)))
    feature_links = Column(postgresql.ARRAY(String(500)))
    feature_start = Column(Integer);
    feature_stop = Column(Integer);
    feature_types = Column(postgresql.ARRAY(String(500)));
    amplification_start = Column(Integer);
    amplification_stop = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
        #UniqueConstraint('analysis_id','experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop'),
        UniqueConstraint('experiment_id','sample_name','genome_chromosome','genome_strand','amplification_start','amplification_stop',
                         'feature_locations','feature_genes','feature_annotations',
                         'feature_start','feature_stop','feature_types'
                         ),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.feature_annotations=row_dict_I['feature_annotations'];
        self.strand_stop=row_dict_I['strand_stop'];
        self.amplification_stop=row_dict_I['amplification_stop'];
        self.amplification_start=row_dict_I['amplification_start'];
        self.feature_types=row_dict_I['feature_types'];
        self.feature_stop=row_dict_I['feature_stop'];
        self.used_=row_dict_I['used_'];
        self.strand_start=row_dict_I['strand_start'];
        self.genome_strand=row_dict_I['genome_strand'];
        self.genome_chromosome=row_dict_I['genome_chromosome'];
        self.sample_name=row_dict_I['sample_name'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.comment_=row_dict_I['comment_'];
        self.feature_start=row_dict_I['feature_start'];
        self.feature_links=row_dict_I['feature_links'];
        self.feature_locations=row_dict_I['feature_locations'];
        self.feature_genes=row_dict_I['feature_genes'];

    def __set__row__(self,
        #analysis_id_I,
        experiment_id_I,
        sample_name_I,
        genome_chromosome_I,
        genome_strand_I,
        strand_start_I,
        strand_stop_I,
        feature_annotations_I,
        feature_genes_I,
        feature_locations_I,
        feature_links_I,
        feature_start_I,
        feature_stop_I,
        feature_types_I,
        amplification_start_I,
        amplification_stop_I,
        used__I,
        comment__I):
        #self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.genome_chromosome=genome_chromosome_I
        self.genome_strand=genome_strand_I
        self.strand_start=strand_start_I
        self.strand_stop=strand_stop_I
        self.feature_annotations=feature_annotations_I
        self.feature_genes=feature_genes_I
        self.feature_locations=feature_locations_I
        self.feature_links=feature_links_I
        self.feature_start=feature_start_I
        self.feature_stop=feature_stop_I
        self.feature_types=feature_types_I
        self.amplification_start=amplification_start_I
        self.amplification_stop=amplification_stop_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                #'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'genome_chromosome':self.genome_chromosome,
                'genome_strand':self.genome_strand,
                'strand_start':self.strand_start,
                'strand_stop':self.strand_stop,
                'feature_annotations':self.feature_annotations,
                'feature_genes':self.feature_genes,
                'feature_locations':self.feature_locations,
                'feature_links':self.feature_links,
                'feature_start':self.feature_start,
                'feature_stop':self.feature_stop,
                'feature_types':self.feature_types,
                'amplification_start':self.amplification_start,
                'amplification_stop':self.amplification_stop,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())