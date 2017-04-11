#SBaaS
from .stage01_resequencing_omniExpressExome_io import stage01_resequencing_omniExpressExome_io

class stage01_resequencing_omniExpressExome_execute(stage01_resequencing_omniExpressExome_io):
    def make_annotationFilename(self,
        species_I= 'Homo_sapiens',
        release_I= '87',
        chr_I= '10'):
        '''
        Example:
        'Homo_sapiens.GRCh38.87.chromosome.10.dat'
        '''
        filename = '%s.GRCh38.%s.chromosome.%s.dat'%(species_I,release_I,chr_I)
        return filename;
    def make_sequenceFilename(self,
        species_I= 'Homo_sapiens',
        release_I= '87',
        chr_I= '10'):
        '''
        Example:
        current: 'hs_ref_GRCh38.p7_alts.fa' or 'hs_alt_CHM1_1.1_chr1.fa'?
        old: 'chr1.fa'

        '''
        filename = 'chr%s.fa'%(chr_I)
        return filename;
    def execute_filterOmniExpressExome(self,
            experiment_id_I='BloodProject01',
            sample_names_I='',
            gc_score_I = 0.15,
            include_nan_I = False,):
        '''Filter omniExpressExome data
        INPUT:
        experiment_id_I = string
        OUTPUT:
        
        NOTES:
        gc_score <= 0.2 is considered poor quality by GenScore
        gc_score < 0.2 is considered poor quality (sources: ...)
        gc_score > 0.7 is considered to be high quality  (sources: ...)

        '''
        data_O = [];
        omniExpressExome = self.getJoin_rows_experimentIDs_dataStage01ResequecingOmniExpressExomeAndAnnotations(
            experiment_ids_I=experiment_id_I,
            sample_names_I=sample_names_I,
            gc_score_I = gc_score_I,
            include_nan_I = include_nan_I,
            );
        ##BUG: remove 'nan' from GC_Score
        #GC_Score = [d['GC_Score'] for d in omniExpressExome]
        GC_Score = [];
        for i,d in enumerate(omniExpressExome):
            if str(d['GC_Score'])=='nan':
                GC_Score.append(0.0);
            else:
                GC_Score.append(d['GC_Score'])
        data_O = [{
                'experiment_id':d['experiment_id'],
                'sample_name':d['sample_name'],
                'GenomeBuild':d['GenomeBuild'],
                'Chr':d['Chr'],
                'MapInfo':d['MapInfo'],
                'SNP_Name':d['SNP_Name'],
                'used_':True,
                'comment_':None,
                'mutation_data':{'SNP_Name':d['SNP_Name'],
                    'new_seq':d['Allele1_Top'], #changed for compatibility with gd
                    'Allele2_Top':d['Allele2_Top'],
                    'GC_Score':GC_Score[i], #d['GC_Score'],
                    'IlmnID':d['IlmnID'],
                    'Name':d['Name'],
                    'IlmnStrand':d['IlmnStrand'],
                    'SNP':d['SNP'],
                    'AddressA_ID':d['AddressA_ID'],
                    'AlleleA_ProbeSeq':d['AlleleA_ProbeSeq'],
                    'AddressB_ID':d['AddressB_ID'],
                    'AlleleB_ProbeSeq':d['AlleleB_ProbeSeq'],
                    'GenomeBuild':d['GenomeBuild'],
                    'chromosome':d['Chr'], #changed for compatibility with gd
                    'position':d['MapInfo'], #changed for compatibility with gd
                    'Ploidy':d['Ploidy'],
                    'Species':d['Species'],
                    'Source':d['Source'],
                    'SourceVersion':d['SourceVersion'],
                    'SourceStrand':d['SourceStrand'],
                    'SourceSeq':d['SourceSeq'],
                    'TopGenomicSeq':d['TopGenomicSeq'],
                    'BeadSetID':d['BeadSetID'],
                    'Exp_Clusters':d['Exp_Clusters'],
                    'RefStrand':d['RefStrand'],
                    'type':'SNP', #added for compatibility with gd
                    'frequency':1.0, #added for compatibility with gd
                    },
            } for i,d in enumerate(omniExpressExome)]
        self.add_rows_table('data_stage01_resequencing_omniExpressExomeFiltered',data_O);     

