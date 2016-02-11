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

'''make the analysis table'''
from SBaaS_resequencing.stage01_resequencing_analysis_execute import stage01_resequencing_analysis_execute
exanalysis01 = stage01_resequencing_analysis_execute(session,engine,pg_settings.datadir_settings);
exanalysis01.initialize_dataStage01_resequencing_analysis();
exanalysis01.reset_dataStage01_resequencing_analysis('ALEsKOs01_evo04ptsHIcrr_11');
exanalysis01.import_dataStage01ResequencingAnalysis_add('data/tests/analysis_resequencing/140823_Resequencing_ALEsKOs01_analysis02.csv');

'''Analyze resequencing coverage'''
from SBaaS_resequencing.stage01_resequencing_coverage_execute import stage01_resequencing_coverage_execute
ex01 = stage01_resequencing_coverage_execute(session,engine,pg_settings.datadir_settings);
ex01.initialize_dataStage01_resequencing_coverage();

'''data import'''
# reset imported coverage data
ex01.reset_dataStage01_resequencing_coverage(experiment_id_I='ALEsKOs01',
        sample_names_I=['140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1'
    ]
        )
# import the driver file
from io_utilities.base_importData import base_importData
iobase = base_importData();
iobase.read_csv('data/tests/analysis_resequencing/140823_Resequencing_ALEsKOs01_coverage01.csv');
fileList = iobase.data;
# read in each data file
for file in fileList:
    print('importing coverage data for sample ' + file['sample_name']);
    ex01.import_resequencingCoverageData_add(file['filename'],file['experiment_id'],file['sample_name'],file['strand_start'],file['strand_stop'],file['scale_factor'],file['downsample_factor']);
iobase.clear_data();
# calculate the coverage statistics
ex01.execute_coverageStats_fromGff('ALEsKOs01',
    0, 4640000,
    sample_names_I = [
    '140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1',
    ],
    scale_factor=False,downsample_factor=0)
#TODO: import coverage from .csv
#TODO: import coverage stats from .csv
#TODO: export coverage to .csv
#TODO: export coverage stats to .csv
ex01.export_dataStage01ResequencingCoverage_js('ALEsKOs01_evo04ptsHIcrr_11');

# find amplifications
ex01.reset_dataStage01_resequencing_amplifications('ALEsKOs01',
    sample_names_I = [
    '140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1'
    ]
    )
ex01.execute_findAmplificationsAndCalculateStats_fromGff(
    #analysis_id_I,
    'ALEsKOs01',
    0, 4640000,
    sample_names_I = [
    '140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1',
    ],
    scale_factor=True, downsample_factor=200,reads_min=1.25,reads_max=4.0, indices_min=5000,consecutive_tol=50
    );
# annotate amplifications
ex01.execute_annotateAmplifications(
        'ALEsKOs01',
    sample_names_I = [
    '140807_11_OxicEvo04ptsHIcrrEvo04EPEcoliGlcM9_Broth-1',
    ],
    ref_genome_I='data/U00096.2.gb'
        );
#TODO: import amplifications from .csv
#TODO: import amplifications stats from .csv
#TODO: import amplifications analysis from .csv
#TODO: export amplifications to .csv
#TODO: export amplifications stats to .csv
#TODO: export amplifications analysis to .csv
ex01.export_dataStage01ResequencingAmplifications_js('ALEsKOs01_evo04ptsHIcrr_11');