import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_LIMS')
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_statistics')
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_resequencing')
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/sequencing_utilities')
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/sequencing_analysis')
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/io_utilities')
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/calculate_utilities')

# initialize the biologicalMaterial_geneReferences
from SBaaS_LIMS.lims_biologicalMaterial_io import lims_biologicalMaterial_io
limsio = lims_biologicalMaterial_io(session,engine,pg_settings.datadir_settings);
limsio.initialize_lims_biologicalMaterial();
limsio.import_biologicalMaterialGeneReferences_add('data/tests/analysis_resequencing/150527_MG1655_geneReference.csv');

'''import gd file'''
from SBaaS_resequencing.stage01_resequencing_gd_execute import stage01_resequencing_gd_execute
execute01 = stage01_resequencing_gd_execute(session,engine,pg_settings.datadir_settings);
execute01.initialize_dataStage01_resequencing_gd();
execute01.reset_dataStage01_resequencing_gd('ALEsKOs01');

'''data import'''
# import resequencing data from breseq
from io_utilities.base_importData import base_importData
input = base_importData();
input.read_csv('data/tests/analysis_resequencing/140823_Resequencing_ALEsKOs01_fileList01.csv');
fileList = input.data;
# read in each data file
for file in fileList:
    print('importing resequencing data for sample ' + file['sample_name'])
    execute01.import_resequencingData_add(file['filename'],file['experiment_id'],file['sample_name']);
input.clear_data();

# filter and annotate mutations
execute01.reset_dataStage01_filtered('ALEsKOs01');
execute01.execute_filterMutations_population('ALEsKOs01');
execute01.reset_dataStage01_mutationsAnnotated('ALEsKOs01');
execute01.execute_annotateFilteredMutations('ALEsKOs01',
        annotation_I='data/U00096.2.gb',
        annotation_ref_I = 'genbank',
        biologicalmaterial_id_I='MG1655',)
execute01.drop_dataStage01_resequencing_mutationsSeqChanges();
execute01.reset_dataStage01_mutationsSeqChanges('ALEsKOs01')
execute01.execute_mutateFilteredMutations('ALEsKOs01',
        sample_names_I = [
            ],
        annotation_I='data/U00096.2.gb',
        annotation_ref_I = 'genbank',
        sequence_I='data/U00096.2.fas',
        sequence_ref_I = 'fasta',
        IS_sequences_I='data/ecoli_IS_sequences.fasta',
        IS_sequences_ref_I = 'fasta',
        translation_table_I='Bacterial',)
#TODO: export all tables to .csv
#TODO: update all tables from .csv
#TODO: export to .js
execute01.export_dataStage01ResequencingMutationsAnnotated_js('evo04tpiAevo01');
execute01.export_dataStage01ResequencingMutationsAnnotatedLineage_js('evo04tpiAevo01');
execute01.export_dataStage01ResequencingMutationsSeqChanges_js('evo04tpiAevo01');
execute01.export_dataStage01ResequencingMutationsSeqChangesAndAnnotated_js('evo04tpiAevo01');

'''make the analysis table'''
from SBaaS_resequencing.stage01_resequencing_analysis_execute import stage01_resequencing_analysis_execute
exanalysis01 = stage01_resequencing_analysis_execute(session,engine,pg_settings.datadir_settings);
exanalysis01.drop_dataStage01_resequencing_analysis();
exanalysis01.initialize_dataStage01_resequencing_analysis();
exanalysis01.reset_dataStage01_resequencing_analysis('ALEsKOs01_evo04tpiA_0_11_heatmap');
exanalysis01.reset_dataStage01_resequencing_analysis('ALEsKOs01_evo04tpiA_11');
exanalysis01.reset_dataStage01_resequencing_analysis('evo04tpiAevo01');
exanalysis01.import_dataStage01ResequencingAnalysis_add('data/tests/analysis_resequencing/140823_Resequencing_ALEsKOs01_analysis01.csv');

'''analyze the lineages'''
from SBaaS_resequencing.stage01_resequencing_lineage_execute import stage01_resequencing_lineage_execute
execute01 = stage01_resequencing_lineage_execute(session,engine,pg_settings.datadir_settings);
execute01.drop_dataStage01_resequencing_lineage();
execute01.initialize_dataStage01_resequencing_lineage();
execute01.reset_dataStage01_resequencing_lineage('ALEsKOs01');
# analyze lineages
def strain_lineages():
    strain_lineages_O = {"evo04tpiAevo01":{0:"140401_0_OxicEvo04tpiAEcoliGlcM9_Broth-1",1:"140702_1_OxicEvo04tpiAEvo01J01EcoliGlcM9_Broth-1",2:"140702_3_OxicEvo04tpiAEvo01J03EcoliGlcM9_Broth-1",3:"140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1"},
                        };
    return strain_lineages_O;
execute01.execute_analyzeLineage_population('ALEsKOs01',
                                        strain_lineages());
execute01.execute_annotateMutations_lineage('ALEsKOs01');
#TODO: export all tables to .csv
#TODO: update all tables from .csv
#TODO: export to .js
execute01.export_dataStage01ResequencingLineage_js('evo04tpiAevo01');

'''analyze the endpoints'''
from SBaaS_resequencing.stage01_resequencing_endpoints_execute import stage01_resequencing_endpoints_execute
execute01 = stage01_resequencing_endpoints_execute(session,engine,pg_settings.datadir_settings);
execute01.drop_dataStage01_resequencing_endpoints();
execute01.initialize_dataStage01_resequencing_endpoints();
execute01.reset_dataStage01_resequencing_endpoints(
    #experiment_id_I='ALEsKOs01',
    analysis_id_I = 'ALEsKOs01_evo04tpiA_11'
    );
execute01.execute_analyzeEndpointReplicates_population('ALEsKOs01_evo04tpiA_11',
                                    #    'ALEsKOs01',
                                    #    {"evo04tpiA":["140807_11_OxicEvo04tpiAEvo01EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-1",
                                    #                "140807_11_OxicEvo04tpiAEvo03EPEcoliGlcM9_Broth-1","140807_11_OxicEvo04tpiAEvo04EPEcoliGlcM9_Broth-1"],
                                    #}
                                        );
execute01.execute_annotateMutations_endpoints('ALEsKOs01_evo04tpiA_11');
#TODO: export all tables to .csv
#TODO: update all tables from .csv
#TODO: export to .js

'''generate a heatmap'''
from SBaaS_resequencing.stage01_resequencing_heatmap_execute import stage01_resequencing_heatmap_execute
execute01 = stage01_resequencing_heatmap_execute(session,engine,pg_settings.datadir_settings);
execute01.drop_dataStage01_resequencing_heatmap();
execute01.initialize_dataStage01_resequencing_heatmap();
execute01.reset_dataStage01_resequencing_heatmap('ALEsKOs01_evo04tpiA_0_11_heatmap');
execute01.reset_dataStage01_resequencing_dendrogram('ALEsKOs01_evo04tpiA_0_11_heatmap');
execute01.execute_heatmap('ALEsKOs01_evo04tpiA_0_11_heatmap',
                mutation_id_exclusion_list=['MOB_insA-/-uspC_1977510',
                'SNP_ylbE_547694',
                'SNP_yifN_3957957',
                'DEL_corA_3999668',
                'MOB_tdk_1292255',
                'SNP_rpoB_4182566',
                'INS__4294403',
                'DEL_pyrE-/-rph_3813882',
                'SNP_wcaA_2130811']);
#TODO: export all tables to .csv
#TODO: update all tables from .csv
#TODO: export to .js
execute01.export_dataStage01ResequencingHeatmap_js('ALEsKOs01_evo04tpiA_0_11_heatmap');