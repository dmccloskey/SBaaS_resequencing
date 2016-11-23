﻿import sys
# sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
# filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
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

#data_dir = 'F:/Users/dmccloskey-sbrg/Dropbox (UCSD SBRG)/BloodProject/'
#oee01.import_dataStage01ResequencingOmniExpressExome_add(
#    filename_I = data_dir + 'Test_FinalReport.txt',
#    table_I = 'data_stage01_resequencing_omniExpressExome'
#    )
#oee01.import_dataStage01ResequencingOmniExpressExome_add(
#    filename_I = data_dir + 'additional_snp_Palsson_FinalReport.txt',
#    table_I = 'data_stage01_resequencing_omniExpressExome'
#    )
#oee01.import_dataStage01ResequencingOmniExpressExome_add(
#    filename_I = data_dir + 'HumanOmniExpressExome-8-v1-2-B.csv',
#    table_I = 'data_stage01_resequencing_omniExpressExome_annotations'
#    )


##ADD TO COUNT METHODS...
##Query the fraction of mutations in BioCyc parent classes
#make the mutations table
from SBaaS_resequencing.stage01_resequencing_mutations_execute import stage01_resequencing_mutations_execute
mut01 = stage01_resequencing_mutations_execute(session,engine,pg_settings.datadir_settings);
mut01.initialize_supportedTables()
mut01.initialize_tables();
#query all of the resequencing data
sample_names = '140807_11_OxicEvo04Evo01EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04Evo02EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04gndEvo01EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04gndEvo02EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04gndEvo03EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo01EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo02EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo03EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo04EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo05EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo06EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04pgiEvo08EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04ptsHIcrrEvo01EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04ptsHIcrrEvo02EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04ptsHIcrrEvo03EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04sdhCBEvo01EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04sdhCBEvo02EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04sdhCBEvo03EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1,\
140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1';
#parent_classes_fractions = mut01.calculate_distributionOfMutationsInBioCycParentClasses(
#    experiment_id_I = 'ALEsKOs01',
#    sample_names_I = sample_names,
#    parent_classes_I=[],
#    database_I='ECOLI',
#    names_I=[]);
##export the data to disk
#from io_utilities.base_exportData import base_exportData
#iobase = base_exportData(parent_classes_fractions);
#iobase.write_dict2json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_parent_classes_fractions.json');
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_parent_classes_fractions.csv');

##ADD TO COUNT METHODS...
#mutation_locations_fractions = mut01.calculate_fractionOfMutationLocations(
#    experiment_id_I = 'ALEsKOs01',
#    sample_names_I = sample_names,);
##export the data to disk
#from io_utilities.base_exportData import base_exportData
#iobase = base_exportData(parent_classes_fractions);
#iobase.write_dict2json(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_parent_classes_fractions.json');
#iobase.write_dict2csv(
#    pg_settings.datadir_settings['workspace_data']+\
#    '/_output/ALEsKOs01_0_11_parent_classes_fractions.csv');
