from SBaaS_base.postgresql_orm_base import *
    
class data_stage01_resequencing_lineage(Base):
    #TODO: rename to _timecourse
    __tablename__ = 'data_stage01_resequencing_lineage'
    id = Column(Integer, Sequence('data_stage01_resequencing_lineage_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    lineage_name = Column(String(500)) #lineage_name
    sample_name = Column(String(100))
    intermediate = Column(Integer)
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_position = Column(Integer)
    mutation_data = Column(postgresql.JSON)
    mutation_annotations = Column(postgresql.ARRAY(String(500)))
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    mutation_links = Column(postgresql.ARRAY(String(500)))
    comment_ = Column(Text)

    #__table_args__ = (
    #    UniqueConstraint('lineage_name','experiment_id','sample_name','intermediate'),
    #        )
    def __init__(self,
                row_dict_I,
                ):
        self.comment_=row_dict_I['comment_'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.lineage_name=row_dict_I['lineage_name'];
        self.sample_name=row_dict_I['sample_name'];
        self.intermediate=row_dict_I['intermediate'];
        self.mutation_frequency=row_dict_I['mutation_frequency'];
        self.mutation_type=row_dict_I['mutation_type'];
        self.mutation_position=row_dict_I['mutation_position'];
        self.mutation_data=row_dict_I['mutation_data'];
        self.mutation_annotations=row_dict_I['mutation_annotations'];
        self.mutation_genes=row_dict_I['mutation_genes'];
        self.mutation_locations=row_dict_I['mutation_locations'];
        self.mutation_links=row_dict_I['mutation_links'];

    def __set__row__(self, 
                experiment_id_I,
                lineage_name_I,
                sample_name_I,
                intermediate_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_position_I,
                mutation_data_I,
                mutation_annotations_I,
                mutation_genes_I,
                mutation_locations_I,
                mutation_links_I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.lineage_name=lineage_name_I
        self.sample_name=sample_name_I
        self.intermediate=intermediate_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_position=mutation_position_I
        self.mutation_data=mutation_data_I
        self.mutation_annotations=mutation_annotations_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.mutation_links=mutation_links_I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'lineage_name':self.lineage_name,
                'sample_name':self.sample_name,
                'intermediate':self.intermediate,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_position':self.mutation_position,
                'mutation_data':self.mutation_data,
                'mutation_annotations':self.mutation_annotations,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'mutation_links':self.mutation_links,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())