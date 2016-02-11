from SBaaS_base.postgresql_orm_base import *

class data_stage01_resequencing_histogram(Base):
    __tablename__ = 'data_stage01_resequencing_histogram'
    id = Column(Integer, Sequence('data_stage01_resequencing_histogram_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    feature_id = Column(String(500))
    feature_units = Column(String(50))
    bin = Column(Float)
    bin_width = Column(Float)
    frequency = Column(Integer)
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('analysis_id','feature_id','feature_units','bin',),
            )

    def __init__(self,analysis_id_I,
        feature_id_I,
        feature_units_I,
        bin_I,
        bin_width_I,
        frequency_I,
        used__I,
        comment__I,):
        self.analysis_id=analysis_id_I
        self.feature_id=feature_id_I
        self.feature_units=feature_units_I
        self.bin=bin_I
        self.bin_width=bin_width_I
        self.frequency=frequency_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
                'feature_id':self.feature_id,
                'feature_units':self.feature_units,
                'bin':self.bin,
                'bin_width':self.bin_width,
                'frequency':self.frequency,
                'used_':self.used_,
                'comment_':self.comment_,}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())