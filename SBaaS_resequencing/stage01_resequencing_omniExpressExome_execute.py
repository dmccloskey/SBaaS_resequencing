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
        filename = 'chr%s.fa'%(species_I,release_I,chr_I)
        return filename;

