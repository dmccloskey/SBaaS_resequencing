class stage01_resequencing_heatmap_dependencies():
    
    def filter_mutations(self,mutations_I=[],sample_names_I=[], mutation_id_exclusion_list=[],max_position=4000000,
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete',
                order_sampleNameByMutationID_I=False):
        '''Execute hierarchical cluster on row and column data'''

        print('executing heatmap...');

        from sequencing_analysis.genome_diff import genome_diff
        genomediff = genome_diff();

        # partition into variables:
        if mutations_I: mutation_data = mutations_I;
        else: mutation_data = self.mutations;
        if sample_names_I: sample_names = sample_names_I;
        else: sample_names = self.sample_names;
        mutation_data_O = [];
        mutation_ids_all = [];
        for end_cnt,mutation in enumerate(mutation_data):
            if int(mutation['mutation_position']) > max_position: #ignore positions great than 4000000
                continue;
            # mutation id
            mutation_id = '';
            mutation_id = genomediff._make_mutationID(mutation['mutation_genes'],mutation['mutation_type'],int(mutation['mutation_position']))
            tmp = {};
            tmp.update(mutation);
            tmp.update({'mutation_id':mutation_id});
            mutation_data_O.append(tmp);
            mutation_ids_all.append(mutation_id);
        mutation_ids_all_unique = list(set(mutation_ids_all));
        mutation_ids = [x for x in mutation_ids_all_unique if not x in mutation_id_exclusion_list];
