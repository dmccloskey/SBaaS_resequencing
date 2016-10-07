from .stage01_resequencing_omniExpressExome_query import stage01_resequencing_omniExpressExome_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_resequencing_omniExpressExome_io(stage01_resequencing_omniExpressExome_query,
                                    sbaas_template_io #abstract io methods
                                    ):
    def import_omniExpressExome_txt(
        self, filename_I):
        ''' '''
        data_O=[];
        with open(filename_I,'r') as f:
            headers_bool = True;
            columns_bool = False;
            rows_bool = False;
            for line in f:
                line = line.replace('\n','');
                if headers_bool:
                    if line == '[Data]':
                        headers_bool = False;
                        columns_bool = True;
                        continue;
                elif columns_bool:
                    keys = line.split('\t');
                    keys = [s.replace(' - ','_').replace(' ','_') for s in keys];
                    columns_bool = False;
                    rows_bool = True;
                    continue;
                elif rows_bool:
                    row = line.split('\t');
                    row_dict = {keys[i]:row[i] for i in range(len(keys))}
                    data_O.append(row_dict);
        return data_O;

    def import_dataStage01ResequencingOmniExpressExome_add(
        self,
        filename_I,
        table_I='data_stage01_resequencing_OmniExpressExome'):
        '''
        import data from txt file and add to
        data_stage01_resequencing_OmniExpressExome_annotations or
        data_stage01_resequencing_OmniExpressExome_annotations
        INPUT:
        filename_I = .txt filename
        table_I = string
        '''
        data = self.import_omniExpressExome_txt(filename_I);
        self.add_rows_table(table_I,data);