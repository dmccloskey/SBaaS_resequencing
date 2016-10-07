from SBaaS_base.postgresql_orm_base import *

#TODO: add column for chromosome to postgresql
class data_stage01_resequencing_mutationsAnnotated(Base):
    __tablename__ = 'data_stage01_resequencing_mutationsAnnotated'
    id = Column(Integer, Sequence('data_stage01_resequencing_mutationsAnnotated_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_chromosome = Column(Integer) #Column(String(3))
    mutation_position = Column(Integer)
    mutation_data = Column(postgresql.JSON)
    mutation_annotations = Column(postgresql.ARRAY(String(500)))
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    mutation_links = Column(postgresql.ARRAY(String(500)))
    used_ = Column(Boolean)
    comment_ = Column(Text)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','mutation_type','mutation_position','mutation_chromosome'),
            )
    
    def __init__(self,
                row_dict_I,
                ):
        self.mutation_genes=row_dict_I['mutation_genes'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.mutation_frequency=row_dict_I['mutation_frequency'];
        self.mutation_type=row_dict_I['mutation_type'];
        self.mutation_chromosome=row_dict_I['mutation_chromosome'];
        self.mutation_position=row_dict_I['mutation_position'];
        self.mutation_data=row_dict_I['mutation_data'];
        self.mutation_annotations=row_dict_I['mutation_annotations'];
        self.mutation_locations=row_dict_I['mutation_locations'];
        self.mutation_links=row_dict_I['mutation_links'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self, experiment_id_I,
                sample_name_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_chromosome_I,
                mutation_position_I,
                mutation_data_I,
                mutation_annotations_I,
                mutation_genes_I,
                mutation_locations_I,
                mutation_links_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_chromosome=mutation_chromosome_I
        self.mutation_position=mutation_position_I
        self.mutation_data=mutation_data_I
        self.mutation_annotations=mutation_annotations_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.mutation_links=mutation_links_I
        self.used_ = used__I;
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_chromosome':self.mutation_chromosome,
                'mutation_position':self.mutation_position,
                'mutation_data':self.mutation_data,
                'mutation_annotations':self.mutation_annotations,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'mutation_links':self.mutation_links,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_resequencing_mutationsSeqChanges(Base):
    __tablename__ = 'data_stage01_resequencing_mutationsSeqChanges'
    id = Column(Integer, Sequence('data_stage01_resequencing_mutationsSeqChanges_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_chromosome = Column(Integer)
    mutation_position = Column(Integer)
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    dna_sequence_ref = Column(Text);
    dna_sequence_new = Column(Text);
    rna_sequence_ref = Column(Text);
    rna_sequence_new = Column(Text);
    peptide_sequence_ref = Column(Text);
    peptide_sequence_new = Column(Text);
    mutation_class = Column(postgresql.ARRAY(String(100))); # synonymous, nonsynonymous, frameshift, nonframeshift, other
    dna_features_region = Column(postgresql.ARRAY(String(100)))
    rna_features_region = Column(postgresql.ARRAY(String(100)))
    peptide_features_region = Column(postgresql.ARRAY(String(100)))
    dna_feature_position = Column(Integer);
    dna_feature_ref = Column(String(100));
    dna_feature_new = Column(String(100));
    rna_feature_position = Column(Integer);
    rna_feature_ref = Column(String(100));
    rna_feature_new = Column(String(100));
    peptide_feature_position = Column(Integer);
    peptide_feature_ref = Column(String(100));
    peptide_feature_new = Column(String(100));
    mutation_data = Column(postgresql.JSON)
    used_ = Column(Boolean)
    comment_ = Column(Text)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','mutation_type','mutation_chromosome','mutation_position'),
            )
    
    def __init__(self,
                row_dict_I,
                ):
        self.sample_name=row_dict_I['sample_name'];
        self.peptide_feature_new=row_dict_I['peptide_feature_new'];
        self.peptide_feature_ref=row_dict_I['peptide_feature_ref'];
        self.peptide_feature_position=row_dict_I['peptide_feature_position'];
        self.rna_feature_new=row_dict_I['rna_feature_new'];
        self.rna_feature_ref=row_dict_I['rna_feature_ref'];
        self.rna_feature_position=row_dict_I['rna_feature_position'];
        self.dna_feature_new=row_dict_I['dna_feature_new'];
        self.dna_feature_ref=row_dict_I['dna_feature_ref'];
        self.dna_feature_position=row_dict_I['dna_feature_position'];
        self.peptide_features_region=row_dict_I['peptide_features_region'];
        self.rna_features_region=row_dict_I['rna_features_region'];
        self.dna_features_region=row_dict_I['dna_features_region'];
        self.mutation_class=row_dict_I['mutation_class'];
        self.peptide_sequence_new=row_dict_I['peptide_sequence_new'];
        self.peptide_sequence_ref=row_dict_I['peptide_sequence_ref'];
        self.rna_sequence_new=row_dict_I['rna_sequence_new'];
        self.rna_sequence_ref=row_dict_I['rna_sequence_ref'];
        self.dna_sequence_new=row_dict_I['dna_sequence_new'];
        self.dna_sequence_ref=row_dict_I['dna_sequence_ref'];
        self.mutation_locations=row_dict_I['mutation_locations'];
        self.mutation_genes=row_dict_I['mutation_genes'];
        self.mutation_chromosome=row_dict_I['mutation_chromosome'];
        self.mutation_position=row_dict_I['mutation_position'];
        self.mutation_type=row_dict_I['mutation_type'];
        self.mutation_frequency=row_dict_I['mutation_frequency'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.mutation_data=row_dict_I['mutation_data'];

    def __set__row__(self, experiment_id_I,
                sample_name_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_chromosome_I,
                mutation_position_I,
                mutation_genes_I,
                mutation_locations_I,
                dna_sequence_ref_I,
                dna_sequence_new_I,
                rna_sequence_ref_I,
                rna_sequence_new_I,
                peptide_sequence_ref_I,
                peptide_sequence_new_I,
                mutation_class_I,
                dna_features_region_I,
                rna_features_region_I,
                peptide_features_region_I,
                dna_feature_position_I,
                dna_feature_ref_I,
                dna_feature_new_I,
                rna_feature_position_I,
                rna_feature_ref_I,
                rna_feature_new_I,
                peptide_feature_position_I,
                peptide_feature_ref_I,
                peptide_feature_new_I,
                mutation_data_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_chromosome=mutation_chromosome_I
        self.mutation_position=mutation_position_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.dna_sequence_ref=dna_sequence_ref_I
        self.dna_sequence_new=dna_sequence_new_I
        self.rna_sequence_ref=rna_sequence_ref_I
        self.rna_sequence_new=rna_sequence_new_I
        self.peptide_sequence_ref=peptide_sequence_ref_I
        self.peptide_sequence_new=peptide_sequence_new_I
        self.mutation_class=mutation_class_I
        self.dna_features_region=dna_features_region_I
        self.rna_features_region=rna_features_region_I
        self.peptide_features_region=peptide_features_region_I
        self.dna_feature_position=dna_feature_position_I
        self.dna_feature_ref=dna_feature_ref_I
        self.dna_feature_new=dna_feature_new_I
        self.rna_feature_position=rna_feature_position_I
        self.rna_feature_ref=rna_feature_ref_I
        self.rna_feature_new=rna_feature_new_I
        self.peptide_feature_position=peptide_feature_position_I
        self.peptide_feature_ref=peptide_feature_ref_I
        self.peptide_feature_new=peptide_feature_new_I
        self.mutation_data=mutation_data_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_chromosome':self.mutation_chromosome,
                'mutation_position':self.mutation_position,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'dna_sequence_ref':self.dna_sequence_ref,
                'dna_sequence_new':self.dna_sequence_new,
                'rna_sequence_ref':self.rna_sequence_ref,
                'rna_sequence_new':self.rna_sequence_new,
                'peptide_sequence_ref':self.peptide_sequence_ref,
                'peptide_sequence_new':self.peptide_sequence_new,
                'mutation_class':self.mutation_class,
                'dna_features_region':self.dna_features_region,
                'rna_features_region':self.rna_features_region,
                'peptide_features_region':self.peptide_features_region,
                'dna_feature_position':self.dna_feature_position,
                'dna_feature_ref':self.dna_feature_ref,
                'dna_feature_new':self.dna_feature_new,
                'rna_feature_position':self.rna_feature_position,
                'rna_feature_ref':self.rna_feature_ref,
                'rna_feature_new':self.rna_feature_new,
                'peptide_feature_position':self.peptide_feature_position,
                'peptide_feature_ref':self.peptide_feature_ref,
                'peptide_feature_new':self.peptide_feature_new,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_resequencing_mutationsCodonChanges(Base):
    __tablename__ = 'data_stage01_resequencing_mutationsCodonChanges'
    id = Column(Integer, Sequence('data_stage01_resequencing_mutationsCodonChanges_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    mutation_frequency = Column(Float)
    mutation_type = Column(String(3))
    mutation_chromosome = Column(Integer)
    mutation_position = Column(Integer)
    mutation_genes = Column(postgresql.ARRAY(String(25)))
    mutation_locations = Column(postgresql.ARRAY(String(100)))
    dna_sequence_ref = Column(Text);
    dna_sequence_new = Column(Text);
    rna_sequence_ref = Column(Text);
    rna_sequence_new = Column(Text);
    codon_triplet_ref = Column(String(3));
    codon_triplet_new = Column(String(3));
    mutation_class = Column(postgresql.ARRAY(String(100))); # synonymous, nonsynonymous, frameshift, nonframeshift, other
    dna_features_region = Column(postgresql.ARRAY(String(100)))
    rna_features_region = Column(postgresql.ARRAY(String(100)))
    dna_feature_position = Column(Integer);
    dna_feature_ref = Column(String(100));
    dna_feature_new = Column(String(100));
    rna_feature_position = Column(Integer);
    rna_feature_ref = Column(String(100));
    rna_feature_new = Column(String(100));
    codon_triplet_position = Column(Integer);
    peptide_feature_ref = Column(String(100));
    peptide_feature_new = Column(String(100));
    codon_fraction_ref = Column(Float);
    codon_fraction_new = Column(Float);
    codon_frequency_ref = Column(Float);
    codon_frequency_new = Column(Float);
    codon_frequency_units = Column(String(50)); #per thousand
    mutation_data = Column(postgresql.JSON)
    used_ = Column(Boolean)
    comment_ = Column(Text)

    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name','mutation_type','mutation_chromosome','mutation_position'),
            )
    
    def __init__(self,
                row_dict_I,
                ):
        self.sample_name=row_dict_I['sample_name'];
        self.peptide_feature_new=row_dict_I['peptide_feature_new'];
        self.peptide_feature_ref=row_dict_I['peptide_feature_ref'];
        self.codon_triplet_position=row_dict_I['codon_triplet_position'];
        self.rna_feature_new=row_dict_I['rna_feature_new'];
        self.rna_feature_ref=row_dict_I['rna_feature_ref'];
        self.rna_feature_position=row_dict_I['rna_feature_position'];
        self.dna_feature_new=row_dict_I['dna_feature_new'];
        self.dna_feature_ref=row_dict_I['dna_feature_ref'];
        self.dna_feature_position=row_dict_I['dna_feature_position'];
        self.rna_features_region=row_dict_I['rna_features_region'];
        self.dna_features_region=row_dict_I['dna_features_region'];
        self.mutation_class=row_dict_I['mutation_class'];
        self.codon_triplet_new=row_dict_I['codon_triplet_new'];
        self.codon_triplet_ref=row_dict_I['codon_triplet_ref'];
        self.rna_sequence_new=row_dict_I['rna_sequence_new'];
        self.rna_sequence_ref=row_dict_I['rna_sequence_ref'];
        self.dna_sequence_new=row_dict_I['dna_sequence_new'];
        self.dna_sequence_ref=row_dict_I['dna_sequence_ref'];
        self.mutation_locations=row_dict_I['mutation_locations'];
        self.mutation_genes=row_dict_I['mutation_genes'];
        self.mutation_chromosome=row_dict_I['mutation_chromosome'];
        self.mutation_position=row_dict_I['mutation_position'];
        self.mutation_type=row_dict_I['mutation_type'];
        self.mutation_frequency=row_dict_I['mutation_frequency'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.mutation_data=row_dict_I['mutation_data'];
        self.codon_fraction_new=row_dict_I['codon_fraction_new'];
        self.codon_fraction_ref=row_dict_I['codon_fraction_ref'];
        self.codon_frequency_new=row_dict_I['codon_frequency_new'];
        self.codon_frequency_ref=row_dict_I['codon_frequency_ref'];
        self.codon_frequency_units=row_dict_I['codon_frequency_units'];

    def __set__row__(self, experiment_id_I,
                sample_name_I,
                mutation_frequency_I,
                mutation_type_I,
                mutation_chromosome_I,
                mutation_position_I,
                mutation_genes_I,
                mutation_locations_I,
                dna_sequence_ref_I,
                dna_sequence_new_I,
                rna_sequence_ref_I,
                rna_sequence_new_I,
                codon_triplet_ref_I,
                codon_triplet_new_I,
                mutation_class_I,
                dna_features_region_I,
                rna_features_region_I,
                dna_feature_position_I,
                dna_feature_ref_I,
                dna_feature_new_I,
                rna_feature_position_I,
                rna_feature_ref_I,
                rna_feature_new_I,
                codon_triplet_position_I,
                peptide_feature_ref_I,
                peptide_feature_new_I,
                mutation_data_I,
                #TODO:
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name=sample_name_I
        self.mutation_frequency=mutation_frequency_I
        self.mutation_type=mutation_type_I
        self.mutation_chromosome=mutation_chromosome_I
        self.mutation_position=mutation_position_I
        self.mutation_genes=mutation_genes_I
        self.mutation_locations=mutation_locations_I
        self.dna_sequence_ref=dna_sequence_ref_I
        self.dna_sequence_new=dna_sequence_new_I
        self.rna_sequence_ref=rna_sequence_ref_I
        self.rna_sequence_new=rna_sequence_new_I
        self.codon_triplet_ref=codon_triplet_ref_I
        self.codon_triplet_new=codon_triplet_new_I
        self.mutation_class=mutation_class_I
        self.dna_features_region=dna_features_region_I
        self.rna_features_region=rna_features_region_I
        self.dna_feature_position=dna_feature_position_I
        self.dna_feature_ref=dna_feature_ref_I
        self.dna_feature_new=dna_feature_new_I
        self.rna_feature_position=rna_feature_position_I
        self.rna_feature_ref=rna_feature_ref_I
        self.rna_feature_new=rna_feature_new_I
        self.codon_triplet_position=codon_triplet_position_I
        self.peptide_feature_ref=peptide_feature_ref_I
        self.peptide_feature_new=peptide_feature_new_I
        #TODO:
        self.mutation_data=mutation_data_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'mutation_frequency':self.mutation_frequency,
                'mutation_type':self.mutation_type,
                'mutation_chromosome':self.mutation_chromosome,
                'mutation_position':self.mutation_position,
                'mutation_genes':self.mutation_genes,
                'mutation_locations':self.mutation_locations,
                'dna_sequence_ref':self.dna_sequence_ref,
                'dna_sequence_new':self.dna_sequence_new,
                'rna_sequence_ref':self.rna_sequence_ref,
                'rna_sequence_new':self.rna_sequence_new,
                'codon_triplet_ref':self.codon_triplet_ref,
                'codon_triplet_new':self.codon_triplet_new,
                'mutation_class':self.mutation_class,
                'dna_features_region':self.dna_features_region,
                'rna_features_region':self.rna_features_region,
                'dna_feature_position':self.dna_feature_position,
                'dna_feature_ref':self.dna_feature_ref,
                'dna_feature_new':self.dna_feature_new,
                'rna_feature_position':self.rna_feature_position,
                'rna_feature_ref':self.rna_feature_ref,
                'rna_feature_new':self.rna_feature_new,
                'codon_triplet_position':self.codon_triplet_position,
                'peptide_feature_ref':self.peptide_feature_ref,
                'peptide_feature_new':self.peptide_feature_new,
                'codon_fraction_ref':self.codon_fraction_ref,
                'codon_fraction_new':self.codon_fraction_new,
                'codon_frequency_ref':self.codon_frequency_ref,
                'codon_frequency_new':self.codon_frequency_new,
                'codon_frequency_units':self.codon_frequency_units,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())