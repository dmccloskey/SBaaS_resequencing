#sbaas
from .stage01_resequencing_count_query import stage01_resequencing_count_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
#sbaas models
from .stage01_resequencing_count_postgresql_models import *
#sbaas lims
#biologicalMaterial_geneReference

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container import ddt_container

class stage01_resequencing_count_io(stage01_resequencing_count_query,sbaas_template_io):

    def import_dataStage01ResequencingCount_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingCount(data.data);
        data.clear_data();

    def import_dataStage01ResequencingCount_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingCount(data.data);
        data.clear_data();

    def export_dataStage01ResequencingCount_js(self,analysis_id_I,single_plot_I=False,data_dir_I="tmp"):
        '''export data_stage01_resequencing_count to js file
        Visualization: vertical bar plots of counts for each feature
        '''
        
        #get the table data
        data_table_O = [];
        data_table_O = self.get_rows_analysisID_dataStage01ResequencingCount(analysis_id_I);
        #get the data as a dictionary for each feature
        data_dict_O = {};
        data_dict_O = self.get_rowsAsFeaturesDict_analysisID_dataStage01ResequencingCount(analysis_id_I);
        
        # initialize the ddt objects
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};
        
        # visualization parameters
        data1_keys = ['feature_id',
                      'feature_units',
                      ];
        data1_nestkeys = [ #controls the x axis groupings
            #'element_id'
            'feature_id'
            ];
        data1_keymap = {
                #'xdata':'element_id',
                'xdata':'feature_id',
                'ydata':'fraction',
                'tooltipdata':'frequency',
                #'serieslabel':'feature_id',
                'serieslabel':'element_id',
                'featureslabel':'element_id',
                'ydatalb':None,
                'ydataub':None};

        # make the tile parameter objects
        # tile 0: form
        formtileparameters_O = {
            'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"};
        formparameters_O = {
            'htmlid':'filtermenuform1',
            'htmltype':'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}
            };
        formtileparameters_O.update(formparameters_O);

        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(formtileparameters_O);
        tile2datamap_O.update({"filtermenu1":[0]});

        # tile 1-n features: count
        if not single_plot_I:
            rowcnt = 1;
            colcnt = 1;
            cnt = 0;
            for k,v in data_dict_O.items():
                if len(v)>20: svgtype = 'verticalbarschart2d_01';
                else: svgtype = 'verticalpieschart2d_01';
                svgtype = 'verticalpieschart2d_01';
                svgtileid = "tilesvg"+str(cnt);
                svgid = 'svg'+str(cnt);
                iter=cnt+1; #start at 1
                if (cnt % 2 == 0): 
                    rowcnt = rowcnt+1;#even 
                    colcnt = 1;
                else:
                    colcnt = colcnt+1;
                # make the svg object
                svgparameters1_O = {
                    "svgtype":svgtype,
                    "svgkeymap":[data1_keymap],
                    'svgid':'svg'+str(cnt),
                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":350,
                    "svgheight":250,
                    "svgy1axislabel":"fraction"            
                        };
                svgtileparameters1_O = {
                    'tileheader':'Count',
                    'tiletype':'svg',
                    'tileid':svgtileid,
                    'rowid':"row"+str(rowcnt),
                    'colid':"col"+str(colcnt),
                    'tileclass':"panel panel-default",
                    'rowclass':"row",
                    'colclass':"col-sm-6"};
                dataobject_O.append({"data":v,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
                svgtileparameters1_O.update(svgparameters1_O);
                parametersobject_O.append(svgtileparameters1_O);
                tile2datamap_O.update({svgtileid:[iter]});
                cnt+=1;
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svgparameters1_O = {
                #"svgtype":'verticalpieschart2d_01',
                "svgtype":'verticalbarschart2d_01',
                "svgkeymap":[data1_keymap],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":350,
                "svgheight":250,
                "svgy1axislabel":"fraction"            
                    };
            svgtileparameters1_O = {
                'tileheader':'Count',
                'tiletype':'svg',
                'tileid':svgtileid,
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"};
            svgtileparameters1_O.update(svgparameters1_O);
            parametersobject_O.append(svgparameters1_O);
            tile2datamap_O.update({svgtileid:[1]});
            
        # make the table object
        tableparameters1_O = {
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableclass":"table  table-condensed table-hover",
    		'tableformtileid':'tile1',
            };
        tabletileparameters1_O = {
            'tileheader':'Count',
            'tiletype':'table',
            'tileid':"tabletile1",
            'rowid':"row"+str(rowcnt+1),
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"
            };
        tabletileparameters1_O.update(tableparameters1_O);

        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(tabletileparameters1_O);
        tile2datamap_O.update({"tabletile1":[0]})

        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());

    def export_dataStage01ResequencingCountPerSample_js(self,analysis_id_I,single_plot_I=False,data_dir_I="tmp"):
        '''export data_stage01_resequencing_countPerSample to js file
        Visualization: vertical bar plots of counts for each feature
        '''
        
        #get the table data
        data_table_O = [];
        data_table_O = self.get_rows_analysisID_dataStage01ResequencingCountPerSample(analysis_id_I);
        #get the data as a dictionary for each feature
        data_dict_O = {};
        data_dict_O = self.get_rowsAsFeaturesDict_analysisID_dataStage01ResequencingCountPerSample(analysis_id_I);
        
        # initialize the ddt objects
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};
        
        # visualization parameters
        data1_keys = [
                    'experiment_id',
                    'lineage_name',
                    'sample_name',
                    'time_point',
                    'feature_id',
                    'feature_units',
                      ];
        data1_nestkeys = [ #controls the x axis groupings
            #'element_id'
            'sample_name'
            ];
        data1_keymap = {
                #'xdata':'element_id',
                'xdata':'feature_id',
                #'ydata':'fraction',
                'ydata':'frequency',
                'tooltipdata':'frequency',
                #'serieslabel':'feature_id',
                'serieslabel':'element_id',
                'featureslabel':'element_id',
                'ydatalb':None,
                'ydataub':None};

        # make the tile parameter objects
        # tile 0: form
        formtileparameters_O = {
            'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"};
        formparameters_O = {
            'htmlid':'filtermenuform1',
            'htmltype':'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}
            };
        formtileparameters_O.update(formparameters_O);

        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(formtileparameters_O);
        tile2datamap_O.update({"filtermenu1":[0]});

        # tile 1-n features: count
        if not single_plot_I:
            rowcnt = 1;
            colcnt = 1;
            cnt = 0;
            for k,v in data_dict_O.items():
                if len(v)>20: svgtype = 'verticalbarschart2d_01';
                else: svgtype = 'verticalpieschart2d_01';
                svgtype = 'verticalpieschart2d_01';
                svgtileid = "tilesvg"+str(cnt);
                svgid = 'svg'+str(cnt);
                iter=cnt+1; #start at 1
                if (cnt % 2 == 0): 
                    rowcnt = rowcnt+1;#even 
                    colcnt = 1;
                else:
                    colcnt = colcnt+1;
                # make the svg object
                svgparameters1_O = {
                    "svgtype":svgtype,
                    "svgkeymap":[data1_keymap],
                    'svgid':'svg'+str(cnt),
                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "svgwidth":350,
                    "svgheight":250,
                    "svgy1axislabel":"frequency"            
                        };
                svgtileparameters1_O = {
                    'tileheader':'Count',
                    'tiletype':'svg',
                    'tileid':svgtileid,
                    'rowid':"row"+str(rowcnt),
                    'colid':"col"+str(colcnt),
                    'tileclass':"panel panel-default",
                    'rowclass':"row",
                    'colclass':"col-sm-6"};
                dataobject_O.append({"data":v,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
                svgtileparameters1_O.update(svgparameters1_O);
                parametersobject_O.append(svgtileparameters1_O);
                tile2datamap_O.update({svgtileid:[iter]});
                cnt+=1;
        else:
            cnt = 0;
            svgtileid = "tilesvg"+str(cnt);
            svgid = 'svg'+str(cnt);
            rowcnt = 2;
            colcnt = 1;
            # make the svg object
            svgparameters1_O = {
                #"svgtype":'verticalpieschart2d_01',
                "svgtype":'verticalbarschart2d_01',
                "svgkeymap":[data1_keymap],
                'svgid':'svg'+str(cnt),
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":350,
                "svgheight":250,
                "svgy1axislabel":"fraction"            
                    };
            svgtileparameters1_O = {
                'tileheader':'Count',
                'tiletype':'svg',
                'tileid':svgtileid,
                'rowid':"row"+str(rowcnt),
                'colid':"col"+str(colcnt),
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-6"};
            svgtileparameters1_O.update(svgparameters1_O);
            parametersobject_O.append(svgparameters1_O);
            tile2datamap_O.update({svgtileid:[1]});
            
        # make the table object
        tableparameters1_O = {
            "tabletype":'responsivetable_01',
            'tableid':'table1',
            "tablefilters":None,
            "tableclass":"table  table-condensed table-hover",
    		'tableformtileid':'tile1',
            };
        tabletileparameters1_O = {
            'tileheader':'Count',
            'tiletype':'table',
            'tileid':"tabletile1",
            'rowid':"row"+str(rowcnt+1),
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-12"
            };
        tabletileparameters1_O.update(tableparameters1_O);

        dataobject_O.append({"data":data_table_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        parametersobject_O.append(tabletileparameters1_O);
        tile2datamap_O.update({"tabletile1":[0]})

        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());