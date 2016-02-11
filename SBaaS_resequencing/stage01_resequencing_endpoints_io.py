#sbaas
from .stage01_resequencing_endpoints_query import stage01_resequencing_endpoints_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
#sbaas models
from .stage01_resequencing_endpoints_postgresql_models import *
#sbaas lims
#biologicalMaterial_geneReference

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_resequencing_endpoints_io(stage01_resequencing_endpoints_query,sbaas_template_io):

    def import_dataStage01ResequencingEndpoints_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingEndpoints(data.data);
        data.clear_data();

    def import_dataStage01ResequencingEndpoints_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingEndpoints(data.data);
        data.clear_data();