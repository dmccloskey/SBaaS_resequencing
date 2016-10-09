#system
from copy import copy
import json
#sbaas
from .stage01_resequencing_mutations_query import stage01_resequencing_mutations_query
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
from ddt_python.ddt_container import ddt_container
#sbaas models
from .stage01_resequencing_mutations_postgresql_models import *
#sbaas lims
#biologicalMaterial_geneReference

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_analysis.genome_diff import genome_diff
from ddt_python.ddt_container import ddt_container

class stage01_resequencing_mutations_io(stage01_resequencing_mutations_query,
                                 sbaas_template_io):
    
    def export_dataStage01ResequencingMutationsSeqChangesAndAnnotated_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,max_position=4630000,data_dir_I="tmp"):
        '''export join of data_stage01_resequencing_mutationsSeqChanges and data_stage01_resequencing_mutationsAnnotated to js file'''
        
        genomediff = genome_diff();
        print('exportingdataStage01ResequencingMutationsSeqChanges...')
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        ## convert time_point to intermediates
        #time_points_int = [int(x) for x in time_points];
        #intermediates,time_points,experiment_ids,sample_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names))))
        #intermediates = [i for i,x in enumerate(intermediates)];
        mutation_data_O = [];
        mutation_ids = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsSeqChangesAndAnnotated(experiment_ids[sample_name_cnt],sample_name);
            if not mutations: continue;
            for end_cnt,mutation in enumerate(mutations):
                if mutation['mutation_position'] > max_position: #ignore positions great than 4000000
                    continue;
                if mutation['mutation_frequency']<frequency_threshold:
                    continue;
                # mutation id
                mutation_id = genomediff._make_mutationID2(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position'],mutation['dna_feature_ref'],mutation['dna_feature_new']);
                #mutation_id = self._make_mutationID2(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids.append(mutation_id);
        # screen out mutations
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in mutation_data_O:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    
                    tmp['experiment_id']=mutation['experiment_id'];
                    tmp['sample_name']=mutation['sample_name'];
                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_type']=mutation['mutation_type'];

                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];

                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    
                    tmp['dna_sequence_ref']=mutation['dna_sequence_ref'];
                    tmp['dna_sequence_new']=mutation['dna_sequence_new'];
                    tmp['rna_sequence_ref']=mutation['rna_sequence_ref'];
                    tmp['rna_sequence_new']=mutation['rna_sequence_new'];
                    tmp['peptide_sequence_ref']=mutation['peptide_sequence_ref'];
                    tmp['peptide_sequence_new']=mutation['peptide_sequence_new'];

                    if mutation['mutation_class']:
                        tmp['mutation_class']=";".join([x for x in mutation['mutation_class'] if x is not None]);
                    else: tmp['mutation_class']=mutation['mutation_class'];
                    if mutation['dna_features_region']:
                        tmp['dna_features_region']=";".join([x for x in mutation['dna_features_region'] if x is not None]);
                    else: tmp['dna_features_region']=mutation['dna_features_region'];
                    if mutation['rna_features_region']:
                        tmp['rna_features_region']=";".join([x for x in mutation['rna_features_region'] if x is not None]);
                    else: tmp['rna_features_region']=mutation['rna_features_region'];
                    if mutation['peptide_features_region']:
                        tmp['peptide_features_region']=";".join([x for x in mutation['peptide_features_region'] if x is not None]);
                    else: tmp['peptide_features_region']=mutation['peptide_features_region'];

                    tmp['dna_feature_position']=mutation['dna_feature_position'];
                    tmp['dna_feature_ref']=mutation['dna_feature_ref'];
                    tmp['dna_feature_new']=mutation['dna_feature_new'];
                    tmp['rna_feature_position']=mutation['rna_feature_position'];
                    tmp['rna_feature_ref']=mutation['rna_feature_ref'];
                    tmp['rna_feature_new']=mutation['rna_feature_new'];
                    tmp['peptide_feature_position']=mutation['peptide_feature_position'];
                    tmp['peptide_feature_ref']=mutation['peptide_feature_ref'];
                    tmp['peptide_feature_new']=mutation['peptide_feature_new'];
                    
                    tmp['mutation_data']=json.dumps(mutation['mutation_data']);
                    tmp['used_']=mutation['used_'];
                    tmp['comment_']=mutation['comment_'];
                    mutation_ids_uniqueInfo.append(tmp);
                    break;
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['time_point']=time_points[sample_name_cnt]
                #tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['dna_sequence_ref'] = mutation_id['dna_sequence_ref'];
                tmp['dna_sequence_new'] = mutation_id['dna_sequence_new'];
                tmp['rna_sequence_ref'] = mutation_id['rna_sequence_ref'];
                tmp['rna_sequence_new'] = mutation_id['rna_sequence_new'];
                tmp['peptide_sequence_ref'] = mutation_id['peptide_sequence_ref'];
                tmp['peptide_sequence_new'] = mutation_id['peptide_sequence_new'];
                tmp['mutation_class'] = mutation_id['mutation_class'];
                tmp['dna_feature_position'] = mutation_id['dna_feature_position']
                tmp['dna_feature_ref'] = mutation_id['dna_feature_ref']
                tmp['dna_feature_new'] = mutation_id['dna_feature_new']
                tmp['rna_feature_position'] = mutation_id['rna_feature_position']
                tmp['rna_feature_ref'] = mutation_id['rna_feature_ref']
                tmp['rna_feature_new'] = mutation_id['rna_feature_new']
                tmp['peptide_feature_position'] = mutation_id['peptide_feature_position']
                tmp['peptide_feature_ref'] = mutation_id['peptide_feature_ref']
                tmp['peptide_feature_new'] = mutation_id['peptide_feature_new']
                tmp['dna_features_region'] = mutation_id['dna_features_region']
                tmp['rna_features_region'] = mutation_id['rna_features_region']
                tmp['peptide_features_region'] = mutation_id['peptide_features_region']
                tmp['mutation_data'] = mutation_id['mutation_data']
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in mutation_data_O:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        data_O.append(tmp);
                        break;
        # dump chart parameters to a js files
        data1_keys = [
                    'experiment_id',
                    'sample_name',
                    'time_point',
                    'mutation_id',
                    'mutation_type',
                    'mutation_position',
                    'mutation_genes',
                    'mutation_locations',
                    'mutation_class'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {'xdata':'time_point',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Population mutation frequency", "chart1x1axislabel":"jump_time_point","chart1y1axislabel":"frequency"}
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    'ntablerows':100000.0,
                    "tableheaders":['experiment_id',
                                    'sample_name',
                                    'mutation_frequency',
                                    'mutation_type',
                                    'mutation_position',
                                    'mutation_genes',
                                    'mutation_locations',
                                    'mutation_class',
                                    'mutation_annotations',
                                    'mutation_links',
                                    'dna_feature_position',
                                    'dna_feature_ref',
                                    'dna_feature_new',
                                    'rna_feature_position',
                                    'rna_feature_ref',
                                    'rna_feature_new',
                                    'peptide_feature_position',
                                    'peptide_feature_ref',
                                    'peptide_feature_new',
                                    'dna_sequence_ref',
                                    'dna_sequence_new',
                                    'rna_sequence_ref',
                                    'rna_sequence_new',
                                    'peptide_sequence_ref',
                                    'peptide_sequence_new',
                                    'dna_features_region',
                                    'rna_features_region',
                                    'peptide_features_region',
                                    'mutation_data',
                                    'used_',
                                    'comment_'],
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Mutation sequence analysis','tiletype':'table','tileid':"tile2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0]};
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());            
    def export_dataStage01ResequencingMutationsAnnotated_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,max_position=4630000,data_dir_I="tmp"):
        '''export data_stage01_resequencing_mutationsAnnotated to js file
        Visualization: Table of the annotated mutations
        '''
        
        print('exportingdataStage01ResequencingMutationsAnnotated...')
        
        genomediff = genome_diff();
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        ## convert time_point to intermediates
        #time_points_int = [int(x) for x in time_points];
        #intermediates,time_points,experiment_ids,sample_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names))))
        #intermediates = [i for i,x in enumerate(intermediates)];
        mutation_data_O = [];
        mutation_ids = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sample_name_cnt],sample_name);
            for end_cnt,mutation in enumerate(mutations):
                if mutation['mutation_position'] > max_position: #ignore positions great than 4000000
                    continue;
                if mutation['mutation_frequency']<frequency_threshold:
                    continue;
                # mutation id
                mutation_id = genomediff._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                #mutation_id = self._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids.append(mutation_id);
        # screen out mutations
        mutation_ids_screened = [x for x in mutation_ids if x not in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in mutation_data_O:
                if mutation_id == mutation['mutation_id']:
                    tmp = {};
                    #tmp['mutation_id']=mutation['mutation_id'].replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=str(mutation['mutation_genes']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_position']=str(mutation['mutation_position']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_annotations']=str(mutation['mutation_annotations']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_locations']=str(mutation['mutation_locations']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_links']=str(mutation['mutation_links']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');
                    #tmp['mutation_type']=str(mutation['mutation_type']).replace(',',';').replace("'",';').replace("u",'').replace("[",'').replace("]",'');

                    #tmp['mutation_id']=mutation['mutation_id'];
                    #tmp['mutation_frequency']=mutation['mutation_frequency'];
                    #tmp['mutation_genes']=mutation['mutation_genes'];
                    #tmp['mutation_position']=mutation['mutation_position'];
                    #tmp['mutation_annotations']=mutation['mutation_annotations'];
                    #tmp['mutation_locations']=mutation['mutation_locations'];
                    #tmp['mutation_links']=mutation['mutation_links'];
                    #tmp['mutation_type']=mutation['mutation_type'];

                    tmp['mutation_id']=mutation['mutation_id'];
                    tmp['mutation_frequency']=mutation['mutation_frequency'];
                    if mutation['mutation_annotations']:
                        tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                    else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                    if mutation['mutation_links']:
                        tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                    else: tmp['mutation_links']=mutation['mutation_links'];

                    if mutation['mutation_genes']:
                        tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                    else: tmp['mutation_genes']=mutation['mutation_genes'];
                    if mutation['mutation_position']:
                        tmp['mutation_position']=mutation['mutation_position'];
                    else: tmp['mutation_position']=mutation['mutation_position'];
                    if mutation['mutation_locations']:
                        tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                    else: tmp['mutation_locations']=mutation['mutation_locations'];
                    tmp['mutation_type']=mutation['mutation_type'];
                    tmp['mutation_data']=json.dumps(mutation['mutation_data']);
                    tmp['used_']=mutation['used_'];
                    tmp['comment_']=mutation['comment_'];
                    mutation_ids_uniqueInfo.append(tmp);     
                    break;    
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['time_point']=time_points[sample_name_cnt]
                #tmp['intermediate']=intermediates[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_frequency']=0.0;  
                tmp['mutation_genes']=mutation_id['mutation_genes'];
                tmp['mutation_position']=mutation_id['mutation_position'];
                tmp['mutation_annotations']=mutation_id['mutation_annotations'];
                tmp['mutation_locations']=mutation_id['mutation_locations'];
                tmp['mutation_links']=mutation_id['mutation_links'];
                tmp['mutation_type']=mutation_id['mutation_type'];
                tmp['mutation_data']=mutation_id['mutation_data'];
                tmp['used_']=mutation_id['used_'];
                tmp['comment_']=mutation_id['comment_'];
                for mutation in mutation_data_O:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        data_O.append(tmp);
                        break;
        # dump chart parameters to a js files
        data1_keys = [
                    #'experiment_id',
                    'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Population mutation frequency", "chart1x1axislabel":"jump_time_point","chart1y1axislabel":"frequency"}
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Population mutation frequency','tiletype':'table','tileid':"tile2",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0]};
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects()); 
    def export_dataStage01ResequencingMutationsAnnotated_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,max_position=4630000,data_dir_I="tmp"):
        '''export data_stage01_resequencing_mutationsAnnotated to js file
        Visualization: treemap of the mutations
        '''
        
        print('exportingdataStage01ResequencingMutationsAnnotated...')
        
        genomediff = genome_diff();
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        mutation_data_O = [];
        mutation_ids = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sample_name_cnt],sample_name);
            for end_cnt,mutation in enumerate(mutations):
                if mutation['mutation_position'] > max_position:
                    continue;
                if mutation['mutation_frequency']<frequency_threshold:
                    continue;
                if not mutation['mutation_genes']:
                    mutation['mutation_genes'] = ['unknown'];
                # mutation id
                mutation_id = genomediff._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                if mutation_id in mutation_id_exclusion_list:
                    continue;
                tmp = {};
                tmp['analysis_id']=analysis_id_I;
                tmp['time_point']=time_points[sample_name_cnt]
                tmp['experiment_id']=experiment_ids[sample_name_cnt]
                tmp['sample_name']=sample_name
                tmp['mutation_id']=mutation_id;
                if mutation['mutation_annotations']:
                    tmp['mutation_annotations']=";".join([x for x in mutation['mutation_annotations'] if x is not None]);
                else: tmp['mutation_annotations']=mutation['mutation_annotations'];
                if mutation['mutation_links']:
                    tmp['mutation_links']=";".join([x for x in mutation['mutation_links'] if x is not None]);
                else: tmp['mutation_links']=mutation['mutation_links'];
                if mutation['mutation_genes']:
                    tmp['mutation_genes']=";".join([x for x in mutation['mutation_genes'] if x is not None]);
                else: tmp['mutation_genes']=mutation['mutation_genes'];
                if mutation['mutation_position']:
                    tmp['mutation_position']=mutation['mutation_position'];
                else: tmp['mutation_position']=mutation['mutation_position'];
                if mutation['mutation_locations']:
                    tmp['mutation_locations']=";".join([x for x in mutation['mutation_locations'] if x is not None]);
                else: tmp['mutation_locations']=mutation['mutation_locations'];
                tmp.update(mutation);
                mutation_data_O.append(tmp);

        # dump chart parameters to a js files
        data1_keys = [
                    'experiment_id',
                    'sample_name',
                    'mutation_id',
                    #'mutation_frequency',
                    'mutation_type',
                    'mutation_position',
                    #'mutation_data',
                    'mutation_annotations',
                    'mutation_genes',
                    #'mutation_links',
                    'mutation_locations'
                    ];
        data1_nestkeys = ['analysis_id',
                          'mutation_genes',
                          'mutation_position',
                          'mutation_type',
                          #'sample_name'
                          ];
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        # make the data object
        dataobject_O = [{"data":mutation_data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":mutation_data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}
                        ];
        # make the tile parameter objects
        # tile 0: form
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        # tile 1: treelayout2d_01
        svgparameters_O = {"svgtype":'treelayout2d_01',
                           "svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 100, 'right': 100, 'bottom': 100, 'left': 100 },
                            "svgwidth":1000,
                            "svgheight":1000,
                            "svgduration":750,
                            "datalastchild":'sample_name'
                            };
        svgtileparameters_O = {
                'tileheader':'Mutations annotated',
                'tiletype':'svg',
                'tileid':"tile1",
                'rowid':"row2",
                'colid':"col1",
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-12"
                };
        svgtileparameters_O.update(svgparameters_O);

        # tile 2: table
        tableparameters_O = {
                    "tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    };
        tabletileparameters_O = {
                    'tileheader':'Mutations annotated',
                    'tiletype':'table',
                    'tileid':"tile2",
                    'rowid':"row3",
                    'colid':"col1",
                    'tileclass':"panel panel-default",
                    'rowclass':"row",
                    'colclass':"col-sm-12"
                    };
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile1":[0],"tile2":[1]}; #pass two identical data objects to the treemap and table
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
    def export_dataStage01ResequencingMutationsAnnotatedLineageArea_js(self,analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,max_position=4630000,data_dir_I="tmp"):
        '''export data_stage01_resequencing_mutationsAnnotated to js file
        Visualization: scatterlineplot of mutation frequency across jump time
        '''
        
        genomediff = genome_diff();
        print('exportingdataStage01ResequencingMutationsAnnotated...')
        # get the analysis information
        experiment_ids,sample_names,time_points = [],[],[];
        experiment_ids,sample_names,time_points = self.get_experimentIDAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # convert time_point to intermediates
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points,experiment_ids,sample_names = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names))))
        intermediates = [i for i,x in enumerate(intermediates)];
        mutation_data_O = [];
        mutation_ids = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sample_name_cnt],sample_name);
            for end_cnt,mutation in enumerate(mutations):
                if mutation['mutation_position'] > max_position: #ignore positions great than 4000000
                    continue;
                if mutation['mutation_frequency']<frequency_threshold:
                    continue;
                # mutation id
                mutation_id = genomediff._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                #mutation_id = self._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
                mutation_ids.append(mutation_id);
        # screen out mutations
        mutation_ids_screened = [x for x in mutation_ids if not x in mutation_id_exclusion_list];
        mutation_ids_unique = list(set(mutation_ids_screened));
        # get mutation information for all unique mutations
        mutation_ids_uniqueInfo = [];
        for mutation_id in mutation_ids_unique:
            for mutation in mutation_data_O:
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
                    tmp['used_']=mutation['used_'];
                    tmp['comment_']=mutation['comment_'];
                    mutation_ids_uniqueInfo.append(tmp);   
                    break;       
        data_O = [];
        # add in 0.0 frequency for mutations that are not found
        for sample_name_cnt,sample_name in enumerate(sample_names):
            for mutation_id in mutation_ids_uniqueInfo:
                tmp = {};
                tmp_fitted = {};
                tmp['mutation_id']=mutation_id['mutation_id']
                tmp['time_point']=time_points[sample_name_cnt]
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
                for mutation in mutation_data_O:
                    if sample_name == mutation['sample_name'] and mutation_id['mutation_id'] == mutation['mutation_id']:
                        tmp['mutation_frequency']=mutation['mutation_frequency'];
                        tmp['comment_']=mutation['comment_'];
                        break;
                data_O.append(tmp);
        # dump chart parameters to a js files
        data1_keys = [
                    #'experiment_id',
                    #'sample_name',
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
        data1_nestkeys = ['mutation_id']; #horizontalareaplot2d_01
        #data1_nestkeys = ['intermediate']; #verticalbarschart2d_01
        data1_keymap = {'xdata':'intermediate',
                        'ydata':'mutation_frequency',
                        'serieslabel':'mutation_id',
                        'featureslabel':''};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Population mutation frequency", "chart1x1axislabel":"jump_time_point","chart1y1axislabel":"frequency"}
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {
            #"svgtype":'verticalbarschart2d_01',
            "svgtype":'horizontalareaplot2d_01',
            "svgkeymap":[data1_keymap,data1_keymap],
            'svgid':'svg1',
            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
            "svgwidth":500,"svgheight":350,
            "svgstackoffset":"extend",
            "svgx1axislabel":"jump_time_point","svgy1axislabel":"frequency",
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
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file

        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_resequencing_mutationsAnnotated' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
    def export_mapGeneName2ModelReaction_csv(self,rows_I,
                                             filename_O):
        """return the model reaction rows whose enzymes are produced by a given gene
        INPUT:
        rows_I = rows from data_stage02_physiology_modelReactions
        OUTPUT:
        filename_O = name of output file
                    rows from data_stage02_physiology_modelReactions in a .csv file
        """
        if rows_I:
            io = base_exportData(rows_I);
            io.write_dict2csv(filename_O);
        else:
            print('no rows found');
