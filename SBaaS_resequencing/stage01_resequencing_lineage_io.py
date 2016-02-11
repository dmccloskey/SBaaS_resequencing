#system
import json
#sbaas
from .stage01_resequencing_lineage_query import stage01_resequencing_lineage_query
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
from .stage01_resequencing_lineage_dependencies import stage01_resequencing_lineage_dependencies
from SBaaS_base.sbaas_template_io import sbaas_template_io
#sbaas models
from .stage01_resequencing_lineage_postgresql_models import *

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_resequencing_lineage_io(stage01_resequencing_lineage_query,
                                      stage01_resequencing_analysis_query,
                                      stage01_resequencing_lineage_dependencies,
                                      sbaas_template_io):
    

    def import_dataStage01ResequencingLineage_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingLineage(data.data);
        data.clear_data();

    def import_dataStage01ResequencingLineage_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingLineage(data.data);
        data.clear_data();

    def export_dataStage01ResequencingLineage_js(self,analysis_id_I,mutation_id_exclusion_list=[],data_dir_I="tmp"):
        '''export data_stage01_resequencing_lineage to js file'''

        #(self,analysis_id_I,mutation_id_exclusion_list=[],data_dir_I="tmp")
        
        print('exportingdataStage01ResequencingLineage...')
        # get the analysis information
        #analysis_info = {};
        #analysis_info = self.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        intermediates,time_points,experiment_ids,sample_names,lineage_names = self.convert_timePoints2Intermediates(time_points,experiment_ids,sample_names,lineage_names);
        # get the lineage information
        lineage_data = [];
        lineage_data = self.get_rowsIO_lineageName_dataStage01ResequencingLineage(lineage_names[0]);
        #for lineage in lineage_names:
        #    lineage_data_tmp = [];
        #    lineage_data_tmp = self.get_rowsIO_lineageName_dataStage01ResequencingLineage(lineage);
        #    lineage_data.extend(lineage_data_tmp);
        mutation_ids = [x['mutation_id'] for x in lineage_data];
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in lineage_data:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    #tmp['mutation_id']=mutation['mutation_id']
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=mutation['mutation_genes'];
                    #tmp['mutation_position']=mutation['mutation_position'];
                    #tmp['mutation_annotations']=mutation['mutation_annotations'];
                    #tmp['mutation_locations']=mutation['mutation_locations'];
                    #tmp['mutation_links']=mutation['mutation_links'];
                    #tmp['mutation_type']=mutation['mutation_type'];
                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];
                    tmp['mutation_type']=mutation['mutation_type'];
                    tmp['used_']=True;
                    tmp['comment_']=None;
                    mutation_ids_uniqueInfo.append(tmp);          
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in lineage_data:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        break;
                data_O.append(tmp);
        # dump chart parameters to a js files
        data1_keys = [
                    #'experiment_id',
                    #'lineage_name',
                    'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    #'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"intermediate","svgy1axislabel":"frequency",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,1],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_resequencing_lineage' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);