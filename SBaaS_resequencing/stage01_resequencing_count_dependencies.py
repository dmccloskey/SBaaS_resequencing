class stage01_resequencing_count_dependencies():
    def record_count(self,analysis_id,feature_id,feature_units,element_ids,element_counts,elements_count_fraction):
        '''make the count listDict
        INPUT:
        OUTPUT:
        '''
        data_O = [];
        for i,e in enumerate(element_ids):
            tmp = {
                'analysis_id':analysis_id,
                'feature_id':feature_id,
                'feature_units':feature_units,
                'element_id':e,
                'frequency':int(element_counts[i]),
                'fraction':elements_count_fraction[i],
                'used_':True,
                'comment_':None};
            data_O.append(tmp);
        return data_O;
    def convert_timePoints2Intermediates(self,time_points,experiment_ids,sample_names,lineage_names):
        '''convert jump time-points to intermediates
        INPUT:
        OUTPUT:
        '''
        time_points_int = [int(x) for x in time_points];
        intermediates,time_points_O,experiment_ids_O,sample_names_O,lineage_names_O = (list(t) for t in zip(*sorted(zip(time_points_int,time_points,experiment_ids,sample_names,lineage_names))))
        intermediates_O = [i for i,x in enumerate(intermediates)];
        return intermediates_O,time_points_O,experiment_ids_O,sample_names_O,lineage_names_O;
    
    def record_countPerSample(self,analysis_id,
            experiment_id,lineage_name,sample_name,time_point,
            feature_id,feature_units,element_ids,element_counts,elements_count_fraction):
        '''make the count listDict
        INPUT:
        OUTPUT:
        '''
        data_O = [];
        for i,e in enumerate(element_ids):
            tmp = {
                'analysis_id':analysis_id,
                'experiment_id':experiment_id,
                'lineage_name':lineage_name,
                'sample_name':sample_name,
                'time_point':time_point,
                'feature_id':feature_id,
                'feature_units':feature_units,
                'element_id':e,
                'frequency':int(element_counts[i]),
                'fraction':elements_count_fraction[i],
                'used_':True,
                'comment_':None};
            data_O.append(tmp);
        return data_O;