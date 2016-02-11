

class stage01_resequencing_lineage_dependencies():
    #no def __init__

    def _extract_mutationsLineage(self,lineage_name,end_mutations,intermediate_mutations,intermediate,end_point):
        """extract out mutation lineages based on the end-point mutation"""
        data_O = [];
        for end_cnt,end_mutation in enumerate(end_mutations):
            print('end mutation type/position ' + end_mutation['mutation_data']['type'] + '/' + str(end_mutation['mutation_data']['position']));
            for inter_cnt,intermediate_mutation in enumerate(intermediate_mutations):
                print('intermediate mutation type/position ' + intermediate_mutation['mutation_data']['type'] + '/' + str(intermediate_mutation['mutation_data']['position']));
                if intermediate == 0 and inter_cnt == 0:
                    #copy end_point data (only once per strain lineage)
                    data_tmp = {};
                    data_tmp['experiment_id'] = end_mutation['experiment_id'];
                    data_tmp['sample_name'] = end_mutation['sample_name'];
                    data_tmp['intermediate'] = end_point;
                    frequency = 1.0;
                    if 'frequency' in end_mutation['mutation_data']: frequency = end_mutation['mutation_data']['frequency'];
                    data_tmp['mutation_frequency'] = frequency
                    data_tmp['mutation_position'] = end_mutation['mutation_data']['position']
                    data_tmp['mutation_type'] = end_mutation['mutation_data']['type']
                    data_tmp['lineage_name'] = lineage_name;
                    data_tmp['mutation_data'] = end_mutation['mutation_data'];
                    data_O.append(data_tmp);
                # find the mutation in the intermediates
                # filter by mutation type-specific criteria
                match = {};
                if end_mutation['mutation_data']['type'] == 'SNP':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['new_seq']==intermediate_mutation['mutation_data']['new_seq']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'SUB':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size'] and \
                        end_mutation['mutation_data']['new_seq']==intermediate_mutation['mutation_data']['new_seq']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'DEL':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'INS':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['new_seq']==intermediate_mutation['mutation_data']['new_seq']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'MOB':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['repeat_name']==intermediate_mutation['mutation_data']['repeat_name'] and \
                        end_mutation['mutation_data']['strand']==intermediate_mutation['mutation_data']['strand'] and \
                        end_mutation['mutation_data']['duplication_size']==intermediate_mutation['mutation_data']['duplication_size']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'AMP':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size'] and \
                        end_mutation['mutation_data']['new_copy_number']==intermediate_mutation['mutation_data']['new_copy_number']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'CON':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size'] and \
                        end_mutation['mutation_data']['region']==intermediate_mutation['mutation_data']['region']:
                        match = intermediate_mutation;
                elif end_mutation['mutation_data']['type'] == 'INV':
                    if end_mutation['mutation_data']['type']==intermediate_mutation['mutation_data']['type'] and \
                        end_mutation['mutation_data']['position']==intermediate_mutation['mutation_data']['position'] and \
                        end_mutation['mutation_data']['size']==intermediate_mutation['mutation_data']['size']:
                        match = intermediate_mutation;
                else:
                    print('unknown mutation type');
                if match:
                    data_tmp = {};
                    data_tmp['experiment_id'] = match['experiment_id'];
                    data_tmp['sample_name'] = match['sample_name'];
                    data_tmp['intermediate'] = intermediate;
                    frequency = 1.0;
                    if 'frequency' in match['mutation_data']: frequency = match['mutation_data']['frequency'];
                    data_tmp['mutation_frequency'] = frequency
                    data_tmp['mutation_position'] = match['mutation_data']['position']
                    data_tmp['mutation_type'] = match['mutation_data']['type']
                    data_tmp['lineage_name'] = lineage_name;
                    data_tmp['mutation_data'] = match['mutation_data'];
                    data_O.append(data_tmp);
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