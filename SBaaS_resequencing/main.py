import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
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

from SBaaS_resequencing.stage01_resequencing_gd_execute import stage01_resequencing_gd_execute
exgd01 = stage01_resequencing_gd_execute(session,engine,pg_settings.datadir_settings);
exgd01.initialize_dataStage01_resequencing_gd();
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

#make the histogram table
from SBaaS_resequencing.stage01_resequencing_histogram_execute import stage01_resequencing_histogram_execute
hist01 = stage01_resequencing_histogram_execute(session,engine,pg_settings.datadir_settings);
hist01.initialize_dataStage01_resequencing_histogram();

#make the count table
from SBaaS_resequencing.stage01_resequencing_count_execute import stage01_resequencing_count_execute
count01 = stage01_resequencing_count_execute(session,engine,pg_settings.datadir_settings);
count01.initialize_dataStage01_resequencing_count();

#make the heatmap table
from SBaaS_resequencing.stage01_resequencing_heatmap_execute import stage01_resequencing_heatmap_execute
hmap01 = stage01_resequencing_heatmap_execute(session,engine,pg_settings.datadir_settings);
hmap01.initialize_dataStage01_resequencing_heatmap();

#make the gd table
from SBaaS_resequencing.stage01_resequencing_gd_execute import stage01_resequencing_gd_execute
gd01 = stage01_resequencing_gd_execute(session,engine,pg_settings.datadir_settings);
gd01.initialize_dataStage01_resequencing_gd();

#make the endpoints table
from SBaaS_resequencing.stage01_resequencing_endpoints_execute import stage01_resequencing_endpoints_execute
endpoints01 = stage01_resequencing_endpoints_execute(session,engine,pg_settings.datadir_settings);
endpoints01.initialize_supportedTables()
endpoints01.initialize_tables();

analysis_ids = [
    #'ALEsKOs01_1-2-11_evo04pgiEv01',
    'ALEsKOs01_1-2-3-11_evo04pgi',
    ];
features_histogram = ['mutation_position','mutation_frequency'];
n_bins_histogram = [
    500, # 0-4640000
    9, # 0.1-1.0
    ];
features_count = ['mutation_position','mutation_type','mutation_genes','mutation_locations','mutation_id','mutation_class'];
mutation_id_base01 = ['MOB_insA-/-uspC_1977510',
                    'SNP_ylbE_547694',
                    'SNP_yifN_3957957',
                    'DEL_corA_3999668',
                    'MOB_tdk_1292255',
                    'SNP_rpoB_4182566',
                    'INS__4294403',
                    'DEL_pyrE-/-rph_3813882',
                    'SNP_wcaA_2130811']
for analysis in analysis_ids:
    print('running analysis ' + analysis);
    ##endpoint lineages
    #endpoints01.reset_dataStage01_resequencing_endpointLineages(analysis_id_I = analysis);
    #endpoints01.execute_analyzeLineageReplicates_population(analysis);
    #endpoints01.execute_annotateMutations_endpointLineages(
    #    analysis_id_I = analysis,
    #    ref_genome_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.gb',
    #    ref_I = 'genbank',
    #    biologicalmaterial_id_I='MG1655')
#    #generate the histograms
#    hist01.reset_dataStage01_resequencing_histogram(analysis_id_I=analysis);
#    hist01.execute_binFeatures(
#        analysis_id_I=analysis,
#        features_I = features_histogram,
#        n_bins_I = n_bins_histogram,
#        );
#    #generate the counts
#    count01.reset_dataStage01_resequencing_count(analysis_id_I=analysis);
#    count01.execute_countElementsInFeatures(
#        analysis_id_I=analysis,
#        features_I = features_count,
#        );
#    #generate the counts per sample
#    count01.reset_dataStage01_resequencing_countPerSample(analysis_id_I=analysis);
#    count01.execute_countElementsInFeaturesPerSample(
#        analysis_id_I=analysis,
#        features_I = features_count,
#        );
    #make a heatmap
    #hmap01.reset_dataStage01_resequencing_heatmap(analysis);
    #hmap01.reset_dataStage01_resequencing_dendrogram(analysis);
    #hmap01.execute_heatmap_mutationsAnnotated(analysis,mutation_id_exclusion_list = mutation_id_base01);

#hist01.export_dataStage01ResequencingHistogram_js('ALEsKOs01_11');
#count01.export_dataStage01ResequencingCount_js('ALEsKOs01_1-2-11_evo04pgiEv01');
#count01.export_dataStage01ResequencingCountPerSample_js('ALEsKOs01_1-2-11_evo04pgiEv01');
#gd01.export_dataStage01ResequencingMutationsAnnotatedLineageArea_js('ALEsKOs01_1-2-11_evo04pgiEv01');

#exgd01.execute_mutateFilteredMutations('ALEsKOs01',
#         annotation_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.gb',
#         annotation_ref_I = 'genbank',
#         sequence_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/U00096.2.fas',
#         sequence_ref_I = 'fasta',
#        IS_sequences_I='C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_resequencing/SBaaS_resequencing/data/ecoli_IS_sequences.fasta',
#        IS_sequences_ref_I = 'fasta',
#         translation_table_I='Bacterial',);

#endpoints01.export_dataStage01ResequencingEndpointLineages_js('ALEsKOs01_1-2-3-11_evo04pgi');
#endpoints01.export_dataStage01ResequencingEndpointLineages_genesPerLineage_js('ALEsKOs01_1-2-3-11_evo04pgi');
endpoints01.export_dataStage01ResequencingEndpoints_js('ALEsKOs01_11_evo04pgi');
#endpoints01.export_dataStage01ResequencingEndpoints_genesPerSample_js('ALEsKOs01_11_evo04pgi');
