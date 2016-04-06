#sbaas
from .stage01_resequencing_endpoints_query import stage01_resequencing_endpoints_query
from SBaaS_base.sbaas_template_io import sbaas_template_io

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_analysis.genome_diff import genome_diff
from listDict.listDict import listDict
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable

class stage01_resequencing_endpoints_io(stage01_resequencing_endpoints_query,sbaas_template_io):

    def import_dataStage01ResequencingEndpoints_add(self, filename):
        '''
        table adds
        '''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01ResequencingEndpoints(data.data);
        data.clear_data();

    def import_dataStage01ResequencingEndpoints_update(self, filename):
        '''
        table adds
        '''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01ResequencingEndpoints(data.data);
        data.clear_data();

    def export_dataStage01ResequencingEndpointLineages_js(self,analysis_id_I,
                        query_I={},
                        data_dir_I='tmp'):
        '''
        Pie chart or bar chart of mutation counts
        INPUT:
        analysis_id_I = string,
        query_I = additional query deliminators
        '''

        data_O = self.getGroupAndCount_analysisIDAndMutationTypeAndMutationPositionAndMutationGenes_analysisID_dataStage01ResequencingEndpointLineages(
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);

        #add in the mutationID
        genomediff = genome_diff();
        for d in data_O:
            d['mutation_id'] = genomediff._make_mutationID(
                d['mutation_genes'],d['mutation_type'],d['mutation_position']
                );
            if d['mutation_genes']:
                d['mutation_genes']=";".join([x for x in d['mutation_genes'] if x is not None]);
            else: d['mutation_genes']=d['mutation_genes'];
        
        # make the tile objects  
        #data1 = filter menu and table    
        data1_keys = ['analysis_id',
                      'mutation_type',
                      'mutation_position',
                      'mutation_genes',
                      'count_1',
                      'mutation_id'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {
            'xdata':'mutation_id',
            'ydata':'count_1',
            'serieslabel':'analysis_id',
            'featureslabel':'mutation_id',
            'tooltiplabel':'mutation_id',
            };     
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=data_O,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=None,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            svgtype='verticalbarschart2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data1_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0], #calculated on the fly
            svgfilters=None,
            svgtileheader='Mutation counts',
            tablefilters=None,
            tableheaders=None
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());
    def export_dataStage01ResequencingEndpointLineages_genesPerLineage_js(self,analysis_id_I,
                        query_I={},
                        data_dir_I='tmp'):
        '''
        Pie chart or bar chart of mutation counts
        INPUT:
        analysis_id_I = string,
        query_I = additional query deliminators
        '''

        data_O = self.getGroupAndCount_analysisIDAndLineageNameAndMutationGenes_analysisID_dataStage01ResequencingEndpointLineages(
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
        #add in the mutationID
        genomediff = genome_diff();
        for d in data_O:
            d['mutation_id'] = genomediff._make_mutationID(
                d['mutation_genes'],d['mutation_type'],d['mutation_position']
                );
            if d['mutation_genes']:
                d['mutation_genes']=";".join([x for x in d['mutation_genes'] if x is not None]);
            else: d['mutation_genes']=d['mutation_genes'];
        
        # make the tile objects  
        #data1 = filter menu and table    
        data1_keys = ['analysis_id',
                      'lineage_name',
                      'mutation_genes',
                      'count_1',
                    ];
        data1_nestkeys = ['lineage_name'];
        data1_keymap = {
            'xdata':'mutation_genes',
            'ydata':'count_1',
            'serieslabel':'mutation_genes',
            'featureslabel':'mutation_genes',
            'tooltiplabel':'lineage_name',
            };     
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=data_O,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=None,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            svgtype='verticalbarschart2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data1_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0], #calculated on the fly
            svgfilters=None,
            svgtileheader='Mutation counts',
            tablefilters=None,
            tableheaders=None
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());

    def export_dataStage01ResequencingEndpoints_js(self,analysis_id_I,
                        query_I={},
                        data_dir_I='tmp'):
        '''
        Pie chart or bar chart of mutation counts
        '''

        data_O = self.getGroupAndCount_analysisIDAndMutationTypeAndMutationPositionAndMutationGenes_analysisID_dataStage01ResequencingEndpoints(
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
        
        #add in the mutationID
        genomediff = genome_diff();
        for d in data_O:
            d['mutation_id'] = genomediff._make_mutationID(
                d['mutation_genes'],d['mutation_type'],d['mutation_position']
                );
            if d['mutation_genes']:
                d['mutation_genes']=";".join([x for x in d['mutation_genes'] if x is not None]);
            else: d['mutation_genes']=d['mutation_genes'];
        
        # make the tile objects  
        #data1 = filter menu and table    
        data1_keys = ['analysis_id',
                      'mutation_type',
                      'mutation_position',
                      'mutation_genes',
                      'count_1',
                      'mutation_id'
                    ];
        data1_nestkeys = ['mutation_id'];
        data1_keymap = {
            'xdata':'mutation_id',
            'ydata':'count_1',
            'serieslabel':'analysis_id',
            'featureslabel':'mutation_id',
            'tooltiplabel':'mutation_id',
            };     
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=data_O,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=None,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            svgtype='verticalbarschart2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data1_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0], #calculated on the fly
            svgfilters=None,
            svgtileheader='Mutation counts',
            tablefilters=None,
            tableheaders=None
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());

    def export_dataStage01ResequencingEndpoints_genesPerSample_js(self,analysis_id_I,
                        query_I={},
                        data_dir_I='tmp'):
        '''
        Pie chart or bar chart of mutation counts
        '''

        data_O = self.getGroupAndCount_analysisIDAndSampleNameAndMutationGenes_analysisID_dataStage01ResequencingEndpoints(
                analysis_id_I,
                column_name_I = 'analysis_id',
                aggregate_function_I='count',
                aggregate_label_I='count_1',
                query_I=query_I,
                output_O='listDict',
                dictColumn_I=None);
        #add in the mutationID
        genomediff = genome_diff();
        for d in data_O:
            d['mutation_id'] = genomediff._make_mutationID(
                d['mutation_genes'],d['mutation_type'],d['mutation_position']
                );
            if d['mutation_genes']:
                d['mutation_genes']=";".join([x for x in d['mutation_genes'] if x is not None]);
            else: d['mutation_genes']=d['mutation_genes'];
        
        # make the tile objects  
        #data1 = filter menu and table    
        data1_keys = ['analysis_id',
                      'sample_name',
                      'mutation_genes',
                      'count_1',
                    ];
        data1_nestkeys = ['mutation_genes'];
        data1_keymap = {
            'xdata':'sample_name',
            'ydata':'count_1',
            'serieslabel':'sample_name',
            'featureslabel':'mutation_genes',
            'tooltiplabel':'sample_name',
            };     
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
            data_filtermenu=data_O,
            data_filtermenu_keys=data1_keys,
            data_filtermenu_nestkeys=data1_nestkeys,
            data_filtermenu_keymap=data1_keymap,
            data_svg_keys=None,
            data_svg_nestkeys=None,
            data_svg_keymap=None,
            data_table_keys=None,
            data_table_nestkeys=None,
            data_table_keymap=None,
            data_svg=None,
            data_table=None,
            svgtype='verticalbarschart2d_01',
            tabletype='responsivetable_01',
            svgx1axislabel='',
            svgy1axislabel='',
            tablekeymap = [data1_keymap],
            svgkeymap = [data1_keymap],
            formtile2datamap=[0],
            tabletile2datamap=[0],
            svgtile2datamap=[0], #calculated on the fly
            svgfilters=None,
            svgtileheader='Mutation counts',
            tablefilters=None,
            tableheaders=None
            );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());