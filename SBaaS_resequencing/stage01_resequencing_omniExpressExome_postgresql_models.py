from SBaaS_base.postgresql_orm_base import *
class data_stage01_resequencing_omniExpressExome_header(Base):
    __tablename__ = 'data_stage01_resequencing_omniExpressExome_header'
    id = Column(Integer, Sequence('data_stage01_resequencing_omniExpressExome_header_id_seq'))
    GSGT_Version = Column(String(100))
    processing_date = Column(DateTime)
    kit_type = Column(String(100))
    experiment_id = Column(String(10))
    sample_name = Column(String(100))
    used_ = Column(Boolean)
    comment_ = Column(Text)
    __table_args__ = (
        UniqueConstraint('GSGT_Version','processing_date','kit_type','experiment_id','sample_name'),
        PrimaryKeyConstraint('id'),
    )
    def __init__(self,row_dict_I,):
        self.GSGT_Version = row_dict_I['GSGT_Version']
        self.processing_date = row_dict_I['processing_date']
        self.kit_type = row_dict_I['kit_type']
        self.experiment_id = row_dict_I['experiment_id']
        self.sample_name = row_dict_I['sample_name']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self, GSGT_Version_I,processing_date_I,kit_type_I,experiment_id_I,sample_name_I,used__I,comment__I):
        self.GSGT_Version = GSGT_Version_I
        self.processing_date = processing_date_I
        self.kit_type = kit_type_I
        self.experiment_id = experiment_id_I
        self.sample_name = sample_name_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'GSGT_Version':self.GSGT_Version,
        'processing_date':self.processing_date,
        'kit_type':self.kit_type,
        'experiment_id':self.experiment_id,
        'sample_name':self.sample_name,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_resequencing_omniExpressExome(Base):
    __tablename__ = 'data_stage01_resequencing_omniExpressExome'
    id = Column(Integer, Sequence('data_stage01_resequencing_omniExpressExome_id_seq'))
    experiment_id = Column(String(100))
    sample_name = Column(String(100))
    SNP_Name = Column(String(100))
    Sample_ID = Column(String(100))
    Allele1_Top = Column(String(1))
    Allele2_Top = Column(String(1))
    GC_Score = Column(Float)
    used_ = Column(Boolean)
    comment_ = Column(Text)
    __table_args__ = (
        UniqueConstraint('experiment_id','sample_name','SNP_Name'),
        PrimaryKeyConstraint('id'),
    )
    def __init__(self,row_dict_I,):
        self.experiment_id = row_dict_I['experiment_id']
        self.sample_name = row_dict_I['sample_name']
        self.SNP_Name = row_dict_I['SNP_Name']
        self.Sample_ID = row_dict_I['Sample_ID']
        self.Allele1_Top = row_dict_I['Allele1_Top']
        self.Allele2_Top = row_dict_I['Allele2_Top']
        self.GC_Score = row_dict_I['GC_Score']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self, experiment_id_I,sample_name_I,SNP_Name_I,Sample_ID_I,Allele1_Top_I,Allele2_Top_I,GC_Score_I,used__I,comment__I):
        self.experiment_id = experiment_id_I
        self.sample_name = sample_name_I
        self.SNP_Name = SNP_Name_I
        self.Sample_ID = Sample_ID_I
        self.Allele1_Top = Allele1_Top_I
        self.Allele2_Top = Allele2_Top_I
        self.GC_Score = GC_Score_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'experiment_id':self.experiment_id,
        'sample_name':self.sample_name,
        'SNP_Name':self.SNP_Name,
        'Sample_ID':self.Sample_ID,
        'Allele1_Top':self.Allele1_Top,
        'Allele2_Top':self.Allele2_Top,
        'GC_Score':self.GC_Score,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_resequencing_omniExpressExome_annotations(Base):
    __tablename__ = 'data_stage01_resequencing_omniExpressExome_annotations'
    id = Column(Integer, Sequence('data_stage01_resequencing_omniExpressExome_annotations_id_seq'))
    IlmnID = Column(String(100))
    Name = Column(String(100))
    IlmnStrand = Column(String(10))
    SNP = Column(String(10))
    AddressA_ID = Column(String(50))
    AlleleA_ProbeSeq = Column(String(100))
    AddressB_ID = Column(String(50))
    AlleleB_ProbeSeq = Column(String(100))
    GenomeBuild = Column(Integer)
    Chr = Column(Integer)
    MapInfo = Column(Integer)
    Ploidy = Column(String(10))
    Species = Column(String(50))
    Source = Column(String(50))
    SourceVersion = Column(Integer)
    SourceStrand = Column(String(10))
    SourceSeq = Column(Text)
    TopGenomicSeq = Column(Text)
    BeadSetID = Column(Integer)
    Exp_Clusters = Column(Integer)
    RefStrand = Column(String(1))
    used_ = Column(Boolean)
    comment_ = Column(Text)
    __table_args__ = (
        UniqueConstraint('Name','GenomeBuild','Chr','MapInfo'),
        PrimaryKeyConstraint('id'),
    )
    def __init__(self,row_dict_I,):
        self.IlmnID = row_dict_I['IlmnID']
        self.Name = row_dict_I['Name']
        self.IlmnStrand = row_dict_I['IlmnStrand']
        self.SNP = row_dict_I['SNP']
        self.AddressA_ID = row_dict_I['AddressA_ID']
        self.AlleleA_ProbeSeq = row_dict_I['AlleleA_ProbeSeq']
        self.AddressB_ID = row_dict_I['AddressB_ID']
        self.AlleleB_ProbeSeq = row_dict_I['AlleleB_ProbeSeq']
        self.GenomeBuild = row_dict_I['GenomeBuild']
        self.Chr = row_dict_I['Chr']
        self.MapInfo = row_dict_I['MapInfo']
        self.Ploidy = row_dict_I['Ploidy']
        self.Species = row_dict_I['Species']
        self.Source = row_dict_I['Source']
        self.SourceVersion = row_dict_I['SourceVersion']
        self.SourceStrand = row_dict_I['SourceStrand']
        self.SourceSeq = row_dict_I['SourceSeq']
        self.TopGenomicSeq = row_dict_I['TopGenomicSeq']
        self.BeadSetID = row_dict_I['BeadSetID']
        self.Exp_Clusters = row_dict_I['Exp_Clusters']
        self.RefStrand = row_dict_I['RefStrand']
        self.used_=row_dict_I['used_']
        self.comment_=row_dict_I['comment_']
    def __set__row__(self, IlmnID_I,Name_I,IlmnStrand_I,SNP_I,AddressA_ID_I,AlleleA_ProbeSeq_I,AddressB_ID_I,AlleleB_ProbeSeq_I,GenomeBuild_I,Chr_I,MapInfo_I,Ploidy_I,Species_I,Source_I,SourceVersion_I,SourceStrand_I,SourceSeq_I,TopGenomicSeq_I,BeadSetID_I,Exp_Clusters_I,RefStrand_I,used__I,comment__I):
        self.IlmnID = IlmnID_I
        self.Name = Name_I
        self.IlmnStrand = IlmnStrand_I
        self.SNP = SNP_I
        self.AddressA_ID = AddressA_ID_I
        self.AlleleA_ProbeSeq = AlleleA_ProbeSeq_I
        self.AddressB_ID = AddressB_ID_I
        self.AlleleB_ProbeSeq = AlleleB_ProbeSeq_I
        self.GenomeBuild = GenomeBuild_I
        self.Chr = Chr_I
        self.MapInfo = MapInfo_I
        self.Ploidy = Ploidy_I
        self.Species = Species_I
        self.Source = Source_I
        self.SourceVersion = SourceVersion_I
        self.SourceStrand = SourceStrand_I
        self.SourceSeq = SourceSeq_I
        self.TopGenomicSeq = TopGenomicSeq_I
        self.BeadSetID = BeadSetID_I
        self.Exp_Clusters = Exp_Clusters_I
        self.RefStrand = RefStrand_I
        self.used_ = used__I
        self.comment_ = comment__I
    def __repr__dict__(self):
        return {
        'IlmnID':self.IlmnID,
        'Name':self.Name,
        'IlmnStrand':self.IlmnStrand,
        'SNP':self.SNP,
        'AddressA_ID':self.AddressA_ID,
        'AlleleA_ProbeSeq':self.AlleleA_ProbeSeq,
        'AddressB_ID':self.AddressB_ID,
        'AlleleB_ProbeSeq':self.AlleleB_ProbeSeq,
        'GenomeBuild':self.GenomeBuild,
        'Chr':self.Chr,
        'MapInfo':self.MapInfo,
        'Ploidy':self.Ploidy,
        'Species':self.Species,
        'Source':self.Source,
        'SourceVersion':self.SourceVersion,
        'SourceStrand':self.SourceStrand,
        'SourceSeq':self.SourceSeq,
        'TopGenomicSeq':self.TopGenomicSeq,
        'BeadSetID':self.BeadSetID,
        'Exp_Clusters':self.Exp_Clusters,
        'RefStrand':self.RefStrand,
        'id':self.id,
        'used_':self.used_,
        'comment_':self.comment_,
        }
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

