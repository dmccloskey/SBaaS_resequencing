from .stage01_resequencing_omniExpressExome_query import stage01_resequencing_omniExpressExome_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_resequencing_omniExpressExome_io(stage01_resequencing_omniExpressExome_query,
                                    sbaas_template_io #abstract io methods
                                    ):
    def import_omniExpressExome_txt_v1(
        self,
        filename_I
        ):
        '''
        Read in omniExpressExome text file
        INPUT:
        filename_I = string
        check_headers_I = boolean
        keys_I = string
        start_line_I = integer, start line to itereate through
        n_lines_I = integer, maximum number of lines to iterate through
        OUTPUT:
        '''
        keys_O=[];
        data_O=[];
        headers_bool = True;
        columns_bool = False;
        rows_bool = False;
        with open(filename_I,'r') as f:
            for i,line in enumerate(f):
                line = line.replace('\n','');
                if headers_bool:
                    if line == '[Data]':
                        headers_bool = False;
                        columns_bool = True;
                        continue;
                elif columns_bool:
                    keys = line.split('\t');
                    keys_O = [s.replace(' - ','_').replace(' ','_') for s in keys];
                    columns_bool = False;
                    rows_bool = True;
                    continue;
                elif rows_bool:
                    row = line.split('\t');
                    row_dict = {keys_O[i]:row[i] for i in range(len(keys_O))}
                    data_O.append(row_dict);
        return data_O,keys_O;
    def import_omniExpressExome_txt_v2(
        self,
        filename_I,
        check_headers_I = True,
        keys_I=[],
        start_line_I = 0,
        n_lines_I = 10000,
        ):
        '''
        Read in omniExpressExome text file
        INPUT:
        filename_I = string
        check_headers_I = boolean
        keys_I = string
        start_line_I = integer, start line to itereate through
        n_lines_I = integer, maximum number of lines to iterate through
        OUTPUT:
        '''
        keys_O=[];
        data_O=[];
        if not check_headers_I and keys_I:
            headers_bool = False;
            columns_bool = False;
            rows_bool = True;
            keys_O = keys_I;
        else:
            headers_bool = True;
            columns_bool = False;
            rows_bool = False;
        with open(filename_I,'r') as f:
            #skip lines up to the start_line_I
            for i in range(start_line_I):
                next(f);
            for i,line in enumerate(f):
                #break when the maximum span is reached
                if i>=n_lines_I:
                    break;
                line = line.replace('\n','');
                if headers_bool:
                    if line == '[Data]':
                        headers_bool = False;
                        columns_bool = True;
                        continue;
                elif columns_bool:
                    keys = line.split('\t');
                    keys_O = [s.replace(' - ','_').replace(' ','_') for s in keys];
                    columns_bool = False;
                    rows_bool = True;
                    continue;
                elif rows_bool:
                    row = line.split('\t');
                    row_dict = {keys_O[i]:row[i] for i in range(len(keys_O))}
                    data_O.append(row_dict);
        return data_O,keys_O;

    def import_dataStage01ResequencingOmniExpressExome_add(
        self,
        filename_I,
        table_I='data_stage01_resequencing_OmniExpressExome',
        n_lines_I = 10000,
        header_tag_I = '[Data]',
        deliminator_I = '\t'):
        '''
        import data from txt file and add to
        data_stage01_resequencing_OmniExpressExome_annotations or
        data_stage01_resequencing_OmniExpressExome_annotations
        INPUT:
        filename_I = .txt filename
        table_I = string
        '''
        ##SPLIT 3:
        #variable definitions
        headers_bool = True;
        columns_bool = False;
        rows_bool = False;
        cnt = 0;
        data_O=[];
        keys_O=[];
        
        #main loop:
        #NOTE: not implemented as individual functions to optimize speed and memory
        with open(filename_I,'r') as f:
            for i,line in enumerate(f):
                #break when the maximum span is reached
                if cnt>=n_lines_I and data_O:
                    self.add_rows_table(table_I,data_O);
                    data_O=[];
                    cnt = 0;
                else:
                    cnt+=1;
                line = line.replace('\n','');
                if headers_bool:
                    header = line.split(deliminator_I);
                    if header[0] == header_tag_I:
                        headers_bool = False;
                        columns_bool = True;
                        continue;
                elif columns_bool:
                    keys = line.split(deliminator_I);
                    keys_O = [s.replace(' - ','_').replace(' ','_') for s in keys];
                    columns_bool = False;
                    rows_bool = True;
                    continue;
                elif rows_bool:
                    row = line.split(deliminator_I);
                    row_dict = {keys_O[i]:row[i] for i in range(len(keys_O))}
                    data_O.append(row_dict);

        ##SPLIT 2:
        #for i in range(100000):
        #    if i==0:
        #        check_headers=True;
        #        keys = [];
        #    else:
        #        check_headers=False
        #    start_line = i*n_lines_I;
        #    data,keys = self.import_omniExpressExome_txt_v2(filename_I,
        #        check_headers_I = check_headers,
        #        keys_I=keys,
        #        start_line_I = start_line,
        #        n_lines_I = n_lines_I);
        #    if data:
        #        self.add_rows_table(table_I,data);
        #    else:
        #        break;

        ##SPLIT 1:
        #data = self.import_omniExpressExome_txt_v1(filename_I);
        #self.add_rows_table(table_I,data);