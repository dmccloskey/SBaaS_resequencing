#system
import json
#sbaas
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
from .stage01_resequencing_coverage_query import stage01_resequencing_coverage_query
from .stage01_resequencing_coverage_dependencies import stage01_resequencing_coverage_dependencies
#sbaas models
from .stage01_resequencing_coverage_postgresql_models import *
from SBaaS_base.sbaas_template_io import sbaas_template_io

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_analysis.gff_coverage import gff_coverage
from ddt_python.ddt_container import ddt_container

class stage01_resequencing_coverage_io(
    stage01_resequencing_coverage_query,
    stage01_resequencing_coverage_dependencies,
    stage01_resequencing_analysis_query,
    sbaas_template_io
    ):
    def import_resequencingCoverageData_add(self, filename, 
                                            #analysis_id,
                                            experiment_id, sample_name,strand_start,strand_stop,scale_factor=True,downsample_factor=2000):
        '''table adds
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''
        #OPTION1
        gffcoverage = gff_coverage();
        
        coverage_data = [];
        if '.bam' in filename:
            #TODO convert .bam to .gff using makegff.py from sequencing_utilities
            print('conversion of .bam to .gff not yet supported');
            exit(2);
            #filename_bam = filename;
            #filename = filename.replace('.bam','.gff');
            #extract_strandsFromGff(filename_bam,filename,separate_strand=False);      
        # convert strings to float and int
        strand_start, strand_stop, scale_factor, downsample_factor = int(strand_start), int(strand_stop), bool(scale_factor), float(downsample_factor);   
        #OPTION1
        # parse the gff file
        gffcoverage.extract_coverage_fromGff(filename, strand_start, strand_stop, scale_factor=scale_factor, downsample_factor=downsample_factor,experiment_id_I = experiment_id,sample_name_I=sample_name);
        coverage_data = gffcoverage.coverage;    
        ##OPTION2  
        ## parse the gff file
        #coverage_data = [];
        #coverage_data = self.extract_coverage_fromGff(filename, strand_start, strand_stop, scale_factor=scale_factor, downsample_factor=downsample_factor,experiment_id_I = experiment_id,sample_name_I=sample_name);
        # add data to the database:
        self.add_dataStage01ResequencingCoverage(coverage_data);

    def export_dataStage01ResequencingAmplifications_js(self,analysis_id_I,data_dir_I="tmp"):
        """export amplifications and statistics to js file"""

        # get the analysis info
        #analysis_info = {};
        #analysis_info = self.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names,lineage_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        #get the data for the analysis
        data1_O = [];
        data2_O = [];
        data3_O = [];
        for sn_cnt,sn in enumerate(sample_names):
            data1_tmp = [];
            data1_tmp = self.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplifications_visualization(experiment_ids[sn_cnt],sn);
            data1_O.extend(data1_tmp);
            data2_tmp = [];
            data2_tmp = self.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationStats(experiment_ids[sn_cnt],sn);
            data2_O.extend(data2_tmp);
            data3_tmp = [];
            data3_tmp = self.get_rows_experimentIDAndSampleName_dataStage01ResequencingAmplificationAnnotations(experiment_ids[sn_cnt],sn);
            data3_O.extend(data3_tmp);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'sample_name',
                    'genome_chromosome',
                    'genome_strand',
                    'amplification_start',
                    'amplification_stop',
                    'sample_name_strand',
                    ]
        data1_nestkeys = [
                        #'sample_name',
                        'genome_strand'
                        ];
        data1_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'sample_name_strand',#custom for vis
                        #'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        data2_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                #'reads_min',
                #'reads_max',
                #'reads_lb',
                #'reads_ub',
                #'reads_iq1',
                #'reads_iq3',
                #'reads_median',
                #'reads_mean',
                #'reads_var',
                #'reads_n',
                'amplification_start',
                'amplification_stop',
                    ]
        data2_nestkeys = ['sample_name'];
        data2_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        data3_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                'feature_annotations',
                'feature_genes',
                'feature_locations',
                'feature_links',
                'feature_start',
                'feature_stop',
                'feature_types',
                'amplification_start',
                'amplification_stop',
                    ]
        data3_nestkeys = ['sample_name'];
        data3_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        # make the data object
        dataobject_O = [{"data":data1_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data2_O,"datakeys":data2_keys,"datanestkeys":data2_nestkeys},
                        {"data":data3_O,"datakeys":data3_keys,"datanestkeys":data3_nestkeys}
                        ];
        # make the tile parameter objects
        # linked set #1
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"index","svgy1axislabel":"reads",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1',
                            "svgx1axistickformat":".2e",
                            "svgx1axisticktextattr":{"transform":"matrix(0,1,-1,0,16,6)",
                                                     #"transform":'rotate(90)',"transform":'translate(0,10)'
                                                     },
                            "svgx1axisticktextstyle":{"text-anchor":"start"}
                            };
        svgtileparameters_O = {'tileheader':'Amplifications','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        # linked set #2
        formtileparameters2_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters2_O = {'htmlid':'filtermenuform2',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit2','text':'submit'},"formresetbuttonidtext":{'id':'reset2','text':'reset'},"formupdatebuttonidtext":{'id':'update2','text':'update'}};
        formtileparameters2_O.update(formparameters2_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu2','tableresetbuttonid':'reset2','tablesubmitbuttonid':'submit2'};
        tabletileparameters_O = {'tileheader':'Amplification statistics','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        # linked set #3
        formtileparameters3_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu3",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters3_O = {'htmlid':'filtermenuform3',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit3','text':'submit'},"formresetbuttonidtext":{'id':'reset3','text':'reset'},"formupdatebuttonidtext":{'id':'update3','text':'update'}};
        formtileparameters3_O.update(formparameters3_O);
        tableparameters2_O = {"tabletype":'responsivetable_01',
                    'tableid':'table2',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu3','tableresetbuttonid':'reset3','tablesubmitbuttonid':'submit3'};
        tabletileparameters2_O = {'tileheader':'Amplification annotations','tiletype':'table','tileid':"tile4",'rowid':"row3",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters2_O.update(tableparameters2_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,formtileparameters2_O,tabletileparameters_O,formtileparameters3_O,tabletileparameters2_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,0],"tile3":[1],"tile4":[2],"filtermenu2":[1],"filtermenu3":[2]};
        filtermenuobject_O = [{"filtermenuid":"filtermenu1","filtermenuhtmlid":"filtermenuform1",
                "filtermenusubmitbuttonid":"submit1","filtermenuresetbuttonid":"reset1",
                "filtermenuupdatebuttonid":"update1"},{"filtermenuid":"filtermenu2","filtermenuhtmlid":"filtermenuform2",
                "filtermenusubmitbuttonid":"submit2","filtermenuresetbuttonid":"reset2",
                "filtermenuupdatebuttonid":"update2"},{"filtermenuid":"filtermenu3","filtermenuhtmlid":"filtermenuform3",
                "filtermenusubmitbuttonid":"submit3","filtermenuresetbuttonid":"reset3",
                "filtermenuupdatebuttonid":"update3"}];
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = filtermenuobject_O);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());

    def export_dataStage01ResequencingCoverage_js(self,analysis_id_I,data_dir_I="tmp"):
        """export heatmap to js file"""

        # get the analysis info
        #analysis_info = {};
        #analysis_info = self.get_analysis_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names,lineage_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        #get the data for the analysis
        data1_O = [];
        data2_O = [];
        for sn_cnt,sn in enumerate(sample_names):
            data1_tmp = [];
            data1_tmp = self.get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverage_visualization(experiment_ids[sn_cnt],sn);
            data1_O.extend(data1_tmp);
            data2_tmp = [];
            data2_tmp = self.get_rows_experimentIDAndSampleName_dataStage01ResequencingCoverageStats(experiment_ids[sn_cnt],sn);
            data2_O.extend(data2_tmp);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'sample_name',
                    'genome_chromosome',
                    'genome_strand',
                    'sample_name_strand'
                    ]
        data1_nestkeys = [
                        #'sample_name',
                        'genome_strand'
                        ];
        data1_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'sample_name_strand',#custom for vis
                        'featureslabel':'reads'};
        data2_keys = ['experiment_id',
                'sample_name',
                'genome_chromosome',
                'genome_strand',
                #'strand_start',
                #'strand_stop',
                #'reads_min',
                #'reads_max',
                #'reads_lb',
                #'reads_ub',
                #'reads_iq1',
                #'reads_iq3',
                #'reads_median',
                #'reads_mean',
                #'reads_var',
                #'reads_n',
                'amplification_start',
                'amplification_stop',
                'used_',
                'comment_'
                    ]
        data2_nestkeys = ['sample_name'];
        data2_keymap = {'xdata':'genome_index',
                        'ydata':'reads',
                        'serieslabel':'genome_strand',
                        'featureslabel':'reads'};
        # make the data object
        dataobject_O = [{"data":data1_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data2_O,"datakeys":data2_keys,"datanestkeys":data2_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"index","svgy1axislabel":"reads",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1',
                            "svgx1axistickformat":".2e",
                            "svgx1axisticktextattr":{"transform":"matrix(0,1,-1,0,16,6)",
                                                     #"transform":'rotate(90)',"transform":'translate(0,10)'
                                                     },
                            "svgx1axisticktextstyle":{"text-anchor":"start"}
                            };
        svgtileparameters_O = {'tileheader':'Resequencing coverage','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Resequencing coverage statistics','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,0],"tile3":[1]};
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
