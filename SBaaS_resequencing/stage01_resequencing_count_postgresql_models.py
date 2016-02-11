from SBaaS_base.postgresql_orm_base import *

class data_stage01_resequencing_count(Base):
    __tablename__ = 'data_stage01_resequencing_count'
    id = Column(Integer, Sequence('data_stage01_resequencing_count_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    feature_id = Column(String(500))
    feature_units = Column(String(50))
    element_id = Column(String(500))
    frequency = Column(Integer)
    fraction = Column(Float)
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('analysis_id','feature_id','feature_units','element_id',),
            )

    def __init__(self,analysis_id_I,
            feature_id_I,
            feature_units_I,
            element_id_I,
            frequency_I,
            fraction_I,
            used__I,
            comment__I,):
        self.analysis_id=analysis_id_I
        self.feature_id=feature_id_I
        self.feature_units=feature_units_I
        self.element_id=element_id_I
        self.frequency=frequency_I
        self.fraction=fraction_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
                'feature_id':self.feature_id,
                'feature_units':self.feature_units,
                'element_id':self.element_id,
                'frequency':self.frequency,
                'fraction':self.fraction,
                'used_':self.used_,
                'comment_':self.comment_,
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_resequencing_countPerSample(Base):
    __tablename__ = 'data_stage01_resequencing_countPerSample'
    id = Column(Integer, Sequence('data_stage01_resequencing_countPerSample_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    lineage_name = Column(String(500)) # equivalent to sample_name_abbreviation
    sample_name = Column(String(500)) # equivalent to sample_name_abbreviation
    time_point = Column(String(10)) # converted to intermediate in lineage analysis
    feature_id = Column(String(500))
    feature_units = Column(String(50))
    element_id = Column(String(500))
    frequency = Column(Integer)
    fraction = Column(Float)
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('analysis_id','feature_id','feature_units','element_id','experiment_id','lineage_name','sample_name','time_point'),
            )

    def __init__(self,analysis_id_I,
            experiment_id_I,
            lineage_name_I,
            sample_name_I,
            time_point_I,
            feature_id_I,
            feature_units_I,
            element_id_I,
            frequency_I,
            fraction_I,
            used__I,
            comment__I,):
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.lineage_name=lineage_name_I
        self.sample_name=sample_name_I
        self.time_point=time_point_I
        self.feature_id=feature_id_I
        self.feature_units=feature_units_I
        self.element_id=element_id_I
        self.frequency=frequency_I
        self.fraction=fraction_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
            'experiment_id':self.experiment_id,
            'lineage_name':self.lineage_name,
            'sample_name':self.sample_name,
            'time_point':self.time_point,
                'feature_id':self.feature_id,
                'feature_units':self.feature_units,
                'element_id':self.element_id,
                'frequency':self.frequency,
                'fraction':self.fraction,
                'used_':self.used_,
                'comment_':self.comment_,
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())