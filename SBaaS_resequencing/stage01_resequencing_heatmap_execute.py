import numpy
#sbaas
from .stage01_resequencing_heatmap_io import stage01_resequencing_heatmap_io
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
from .stage01_resequencing_gd_query import stage01_resequencing_gd_query
from .stage01_resequencing_gd_dependencies import stage01_resequencing_gd_dependencies
from .stage01_resequencing_lineage_query import stage01_resequencing_lineage_query
#sbaas models
from .stage01_resequencing_heatmap_postgresql_models import *
#resources
from SBaaS_statistics.heatmap import mutations_heatmap
from python_statistics.calculate_interface import calculate_interface
from python_statistics.calculate_heatmap import calculate_heatmap
from sequencing_analysis.genome_diff import genome_diff

class stage01_resequencing_heatmap_execute(stage01_resequencing_heatmap_io,
                                           stage01_resequencing_analysis_query,
                                           stage01_resequencing_gd_query,
                                           stage01_resequencing_lineage_query,
                                           stage01_resequencing_gd_dependencies):


    def execute_heatmap_lineage(self, analysis_id_I,
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete',
                                                 mutation_id_exclusion_list = []):
        '''Execute hierarchical cluster on row and column data'''
        
        calculateheatmap = calculate_heatmap();
        print('executing heatmap...');
        # get the analysis information
        experiment_ids,lineage_names = [],[];
        experiment_ids,lineage_names = self.get_experimentIDAndLineageName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # partition into variables:
        intermediates_lineage = [];
        mutation_data_lineage_all = [];
        rows_lineage = [];
        n_lineages = len(lineage_names)
        cnt_sample_names = 0;
        for lineage_name_cnt,lineage_name in enumerate(lineage_names):
            # get ALL intermediates by experiment_id and lineage name
            intermediates = [];
            intermediates = self.get_intermediates_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_ids[lineage_name_cnt],lineage_name);
            intermediates_lineage.append(intermediates);
            cnt_sample_names += len(intermediates)
            # get ALL mutation data by experiment_id and lineage name
            mutation_data = [];
            mutation_data = self.get_mutationData_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_ids[lineage_name_cnt],lineage_name);
            mutation_data_lineage_all.extend(mutation_data);
            # get ALL mutation frequencies by experiment_id and lineage name
            rows = [];
            rows = self.get_row_experimentIDAndLineageName_dataStage01ResequencingLineage(experiment_ids[lineage_name_cnt],lineage_name)
            rows_lineage.extend(rows);
        mutation_data_lineage_unique = list(set(mutation_data_lineage_all));
        mutation_data_lineage = [x for x in mutation_data_lineage_unique if not x in mutation_id_exclusion_list];
        min_inter = min(intermediates_lineage)
        max_inter = max(intermediates_lineage);
        # generate the frequency matrix data structure (mutation x intermediate)
        data_O = numpy.zeros((cnt_sample_names,len(mutation_data_lineage)));
        labels_O = {};
        lineages=[];
        col_cnt = 0;
        # order 2: groups each lineage by mutation (intermediate x mutation)
        for lineage_name_cnt,lineage_name in enumerate(lineage_names): #all lineages for intermediate j / mutation i
            for intermediate_cnt,intermediate in enumerate(intermediates_lineage[lineage_name_cnt]):
                if intermediate_cnt == min(intermediates_lineage[lineage_name_cnt]):
                    lineages.append(lineage_name+": "+"start"); # corresponding label from hierarchical clustering (in this case, arbitrary)
                elif intermediate_cnt == max(intermediates_lineage[lineage_name_cnt]):
                    lineages.append(lineage_name+": "+"end"); # corresponding label from hierarchical clustering (in this case, arbitrary)
                else:
                    lineages.append(lineage_name+": "+str(intermediate)); # corresponding label from hierarchical clustering (in this case, arbitrary)
                for mutation_cnt,mutation in enumerate(mutation_data_lineage): #all mutations i for intermediate j
                    for row in rows_lineage:
                        if row['mutation_id'] == mutation and row['intermediate'] == intermediate and row['lineage_name'] == lineage_name:
                            data_O[col_cnt,mutation_cnt] = row['mutation_frequency'];
                            #print col_cnt,mutation_cnt
                col_cnt+=1;
        # generate the clustering for the heatmap
        heatmap_O = [];
        dendrogram_col_O = {};
        dendrogram_row_O = {};
        heatmap_O,dendrogram_col_O,dendrogram_row_O = calculateheatmap.heatmap(data_O,lineages,mutation_data_lineage,
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I);
        # add data to to the database for the heatmap
        for d in heatmap_O:
            row = None;
            row = data_stage01_resequencing_heatmap(
                analysis_id_I,
                d['col_index'],
                d['row_index'],
                d['value'],
                d['col_leaves'],
                d['row_leaves'],
                d['col_label'],
                d['row_label'],
                d['col_pdist_metric'],
                d['row_pdist_metric'],
                d['col_linkage_method'],
                d['row_linkage_method'],
                'frequency',True, None);
            self.session.add(row);
        # add data to the database for the dendrograms
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_col_O['leaves'],
            dendrogram_col_O['icoord'],
            dendrogram_col_O['dcoord'],
            dendrogram_col_O['ivl'],
            dendrogram_col_O['colors'],
            dendrogram_col_O['pdist_metric'],
            dendrogram_col_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_row_O['leaves'],
            dendrogram_row_O['icoord'],
            dendrogram_row_O['dcoord'],
            dendrogram_row_O['ivl'],
            dendrogram_row_O['colors'],
            dendrogram_row_O['pdist_metric'],
            dendrogram_row_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        self.session.commit();
    def execute_heatmap_mutationsAnnotated(self, analysis_id_I,mutation_id_exclusion_list=[],frequency_threshold=0.1,max_position=4630000,
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete',
                order_sampleNameByMutationID_I=False,
                sample_names_I=[],
                mutationIDs_I=[],
                ):
        '''Execute hierarchical cluster on row and column data'''
        calculateheatmap = calculate_heatmap();
        mutationsheatmap =  mutations_heatmap();
        genomediff = genome_diff();

        print('executing heatmap...');
        # get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.get_experimentIDAndSampleName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        #mutations_all = [];
        mutation_data_O = [];
        for sample_name_cnt,sample_name in enumerate(sample_names):
            # query mutation data:
            mutations = [];
            mutations = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sample_name_cnt],sample_name);
            #mutations_all.extend(mutations);
            for mutation in mutations:
                if mutation['mutation_position'] > max_position:
                    continue;
                if mutation['mutation_frequency']<frequency_threshold:
                    continue;
                #if not mutation['mutation_genes']:
                #    mutation['mutation_genes'] = ['unknown'];
                # mutation id
                mutation_id = genomediff._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],mutation['mutation_position']);
                if mutation_id in mutation_id_exclusion_list:
                    continue;
                tmp = {};
                tmp.update(mutation);
                tmp.update({'mutation_id':mutation_id});
                mutation_data_O.append(tmp);
        heatmap_O = [];
        dendrogram_col_O = {};
        dendrogram_row_O = {};
        if order_sampleNameByMutationID_I:
            heatmap_O,dendrogram_col_O,dendrogram_row_O = calculateheatmap.make_heatmap(mutation_data_O,
                'sample_name','mutation_id','mutation_frequency',
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                filter_rows_I=sample_names_I,
                filter_columns_I=mutationIDs_I,
                order_rowsFromTemplate_I=sample_names_I,
                order_columnsFromTemplate_I=mutationIDs_I,);
        else:
            heatmap_O,dendrogram_col_O,dendrogram_row_O = calculateheatmap.make_heatmap(mutation_data_O,
                'mutation_id','sample_name','mutation_frequency',
                row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                filter_rows_I=mutationIDs_I,
                filter_columns_I=sample_names_I,
                order_rowsFromTemplate_I=mutationIDs_I,
                order_columnsFromTemplate_I=sample_names_I);
        ## generate the clustering for the heatmap
        #mutationsheatmap.mutations = mutations_all;
        #mutationsheatmap.sample_names = sample_names;
        #mutationsheatmap.make_heatmap(mutation_id_exclusion_list=mutation_id_exclusion_list,max_position=max_position,
        #        row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
        #        col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I)
        #heatmap_O = mutationsheatmap.heatmap;
        #dendrogram_col_O = mutationsheatmap.dendrogram_col;
        #dendrogram_row_O = mutationsheatmap.dendrogram_row;
        # add data to to the database for the heatmap
        for d in heatmap_O:
            row = None;
            row = data_stage01_resequencing_heatmap(
                analysis_id_I,
                d['col_index'],
                d['row_index'],
                d['value'],
                d['col_leaves'],
                d['row_leaves'],
                d['col_label'],
                d['row_label'],
                d['col_pdist_metric'],
                d['row_pdist_metric'],
                d['col_linkage_method'],
                d['row_linkage_method'],
                'frequency',True, None);
            self.session.add(row);
        # add data to the database for the dendrograms
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_col_O['leaves'],
            dendrogram_col_O['icoord'],
            dendrogram_col_O['dcoord'],
            dendrogram_col_O['ivl'],
            dendrogram_col_O['colors'],
            dendrogram_col_O['pdist_metric'],
            dendrogram_col_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        row = None;
        row = data_stage01_resequencing_dendrogram(
            analysis_id_I,
            dendrogram_row_O['leaves'],
            dendrogram_row_O['icoord'],
            dendrogram_row_O['dcoord'],
            dendrogram_row_O['ivl'],
            dendrogram_row_O['colors'],
            dendrogram_row_O['pdist_metric'],
            dendrogram_row_O['pdist_metric'],
            'frequency',True, None);
        self.session.add(row);
        self.session.commit();