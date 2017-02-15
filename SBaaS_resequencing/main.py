import sys
#sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_labtop.ini';
filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_remote.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_resequencing')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_models')
sys.path.append(pg_settings.datadir_settings['github']+'/sequencing_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/sequencing_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')

from SBaaS_resequencing.stage01_resequencing_gd_execute import stage01_resequencing_gd_execute
exgd01 = stage01_resequencing_gd_execute(session,engine,pg_settings.datadir_settings);
exgd01.initialize_supportedTables()
exgd01.initialize_tables();
##exgd01.execute_mapGeneName2ModelReaction_mutationsAnnotated(
##            experiment_id='ALEsKOs01',
##            filename_O='ALEsKOs01_mutationsAnnotated_modelReactions.csv',
##            biologicalmaterial_id_I = 'MG1655',
##            model_id_I = 'iJO1366',
##            sample_names_I=[],
##            gene_names_I=[]);
#mutation_id_base01 = ['MOB_insA-/-uspC_1977510',
#                    'SNP_ylbE_547694',
#                    'SNP_yifN_3957957',
#                    'DEL_corA_3999668',
#                    'MOB_tdk_1292255',
#                    'SNP_rpoB_4182566',
#                    'INS_unknown_4294403',
#                    #'INS__4294403',
#                    'DEL_pyrE-/-rph_3813882',
#                    'SNP_wcaA_2130811']
#exgd01.export_dataStage01ResequencingMutationsAnnotated_js(
#    analysis_id_I='ALEsKOs01_evo04pgi_0_11_heatmap',
#    mutation_id_exclusion_list=mutation_id_base01);
#exgd01.execute_mutateFilteredMutations('ALEsKOs01',
#    annotation_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.gb',
#    annotation_ref_I = 'genbank',
#    sequence_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.fas',
#    sequence_ref_I = 'fasta',
#    IS_sequences_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/ecoli_IS_sequences.fasta',
#    IS_sequences_ref_I = 'fasta',
#    codonUsageTable_I = pg_settings.datadir_settings['workspace_data']+'/_input/160409_Resequencing_EColiCodonUsageTable.csv',
#    translation_table_I='Bacterial',);
#exgd01.execute_mutateFilteredMutations('ALEsKOs01',
#         annotation_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.gb',
#         annotation_ref_I = 'genbank',
#         sequence_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.fas',
#         sequence_ref_I = 'fasta',
#        IS_sequences_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/ecoli_IS_sequences.fasta',
#        IS_sequences_ref_I = 'fasta',
#         translation_table_I='Bacterial',);

from SBaaS_resequencing.stage01_resequencing_omniExpressExome_execute import stage01_resequencing_omniExpressExome_execute
oee01 = stage01_resequencing_omniExpressExome_execute(session,engine,pg_settings.datadir_settings);
oee01.initialize_supportedTables()
oee01.initialize_tables();

#import time as time

#st = time.time();
#result = oee01.getJoin_rows_experimentIDs_dataStage01ResequecingOmniExpressExomeAndAnnotations(
#        experiment_ids_I='BloodProject01')
#elapsed_time = time.time() - st;
#print("Elapsed time: %.2fs" % elapsed_time)

from io_utilities.import_webData import import_webData
from io_utilities.base_exportData import base_exportData
from io_utilities.base_importData import base_importData
i_webData = import_webData();
o_data = base_exportData();
i_data = base_importData();
import gzip

chromosomes = '1'.split(',')
#0,XY do not have a annotation file
species = 'Homo_sapiens'
release = '87'
server = "ftp.ensembl.org"
ext = "/pub/release-87/genbank/homo_sapiens/"
data_dir = 'C:/Users/dmccloskey/Downloads/'

for chr_I in chromosomes:
    #make the filename
    filename_i = oee01.make_annotationFilename(
        species_I= species,
        release_I= release,
        chr_I= chr_I)
    compressedFilename_i = '%s.gz'%filename_i;
    ##print(server+ext+compressedFilename_i)
    #read the file name from ftp
    file = i_webData.get_ftp(server,ext,compressedFilename_i)
    #export the file to disk
    filename_o = data_dir+filename_i;
    o_data.add_data(gzip.decompress(file.read()))
    o_data.write_binaryFile(filename_o,length=131072);
    o_data.clear_data();
    file.close();

##TODO: add to template notebook
#from SBaaS_resequencing.stage01_resequencing_count_execute import stage01_resequencing_count_execute
#count01 = stage01_resequencing_count_execute(session,engine,pg_settings.datadir_settings);
#count01.initialize_supportedTables()
#count01.initialize_tables();
#count01.execute_countElementsInFeatures(
#    analysis_id_I='ALEsKOs01_11',
#    features_I=['parent_classes'])