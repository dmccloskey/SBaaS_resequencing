class stage01_resequencing_endpoints_dependencies():
    #no def __init__

    def _extract_uniqueMutations(self,analyzed_strain1_mutations,analyzed_strain2_mutations_all,strain1_mutations,endpoint_name):
        '''Extract out unique mutations'''
        data_O = [];
        for analyzed_strain1_mutation in analyzed_strain1_mutations:
            isUnique_bool = True;
            isConserved_cnt = 0;
            for analyzed_strain2_mutations_cnt,analyzed_strain2_mutations in enumerate(analyzed_strain2_mutations_all):
                for analyzed_strain2_mutation in analyzed_strain2_mutations:
                    if analyzed_strain1_mutation == analyzed_strain2_mutation:
                        isUnique_bool = False;
                        isConserved_cnt += 1;
            if isUnique_bool:
                for strain1_mutation_cnt,strain1_mutation in enumerate(strain1_mutations):
                    if (strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])==analyzed_strain1_mutation:
                        data_tmp = {};
                        data_tmp['experiment_id'] = strain1_mutation['experiment_id'];
                        data_tmp['sample_name'] = strain1_mutation['sample_name'];
                        frequency = 1.0;
                        if 'frequency' in strain1_mutation['mutation_data']: frequency = strain1_mutation['mutation_data']['frequency'];
                        data_tmp['mutation_frequency'] = frequency
                        data_tmp['mutation_position'] = strain1_mutation['mutation_data']['position']
                        data_tmp['mutation_type'] = strain1_mutation['mutation_data']['type']
                        data_tmp['endpoint_name'] = endpoint_name;
                        data_tmp['mutation_data'] = strain1_mutation['mutation_data'];
                        data_tmp['isUnique'] = True;
                        data_O.append(data_tmp);
        return data_O;
    def _extract_uniqueLineageMutations(self,analyzed_strain1_mutations,analyzed_strain2_mutations_all,strain1_mutations,endpoint_name,lineage_name):
        '''Extract out unique mutations'''
        data_O = [];
        for analyzed_strain1_mutation in analyzed_strain1_mutations:
            isUnique_bool = True;
            isConserved_cnt = 0;
            for analyzed_strain2_mutations_cnt,analyzed_strain2_mutations in enumerate(analyzed_strain2_mutations_all):
                for analyzed_strain2_mutation in analyzed_strain2_mutations:
                    if analyzed_strain1_mutation == analyzed_strain2_mutation:
                        isUnique_bool = False;
                        isConserved_cnt += 1;
            if isUnique_bool:
                for strain1_mutation_cnt,strain1_mutation in enumerate(strain1_mutations):
                    if (strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])==analyzed_strain1_mutation:
                        data_tmp = {};
                        data_tmp['experiment_id'] = strain1_mutation['experiment_id'];
                        data_tmp['lineage_name'] = lineage_name;
                        data_tmp['sample_name'] = strain1_mutation['sample_name'];
                        frequency = 1.0;
                        if 'frequency' in strain1_mutation['mutation_data']: frequency = strain1_mutation['mutation_data']['frequency'];
                        data_tmp['mutation_frequency'] = frequency
                        data_tmp['mutation_position'] = strain1_mutation['mutation_data']['position']
                        data_tmp['mutation_type'] = strain1_mutation['mutation_data']['type']
                        data_tmp['endpoint_name'] = endpoint_name;
                        data_tmp['mutation_data'] = strain1_mutation['mutation_data'];
                        data_tmp['isUnique'] = True;
                        data_O.append(data_tmp);
        return data_O;
    def _extract_commonMutations(self,matched_mutations,
                        analyzed_strain1_mutations,
                        analyzed_strain2_mutations,
                        strain1_mutations,strain2_mutations,
                        strain1,
                        strain2_cnt,
                        endpoint_name):
        '''extract out mutations that are in common between strains'''
        data_O = [];
        for strain1_mutation_cnt,strain1_mutation in enumerate(strain1_mutations):
            print('strain1 mutation type/position ' + strain1_mutation['mutation_data']['type'] + '/' + str(strain1_mutation['mutation_data']['position']));
            if strain2_cnt == 0: # record strain 1 mutations only once for all strain 2 mutations
                analyzed_strain1_mutations.append((strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position']));
            for strain2_mutation_cnt,strain2_mutation in enumerate(strain2_mutations):
                print('strain2 mutation type/position ' + strain2_mutation['mutation_data']['type'] + '/' + str(strain2_mutation['mutation_data']['position']));
                if strain2_mutation_cnt == 0 and \
                    (strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position']) not in matched_mutations:
                    matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] = 0;
                # find the mutations that are common to strain1 and strain2
                # filter by mutation type-specific criteria
                match = {};
                if strain1_mutation['mutation_data']['type'] == 'SNP':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['new_seq']==strain2_mutation['mutation_data']['new_seq']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'SUB':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size'] and \
                        strain1_mutation['mutation_data']['new_seq']==strain2_mutation['mutation_data']['new_seq']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'DEL':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'INS':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['new_seq']==strain2_mutation['mutation_data']['new_seq']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'MOB':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['repeat_name']==strain2_mutation['mutation_data']['repeat_name'] and \
                        strain1_mutation['mutation_data']['strand']==strain2_mutation['mutation_data']['strand'] and \
                        strain1_mutation['mutation_data']['duplication_size']==strain2_mutation['mutation_data']['duplication_size']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'AMP':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size'] and \
                        strain1_mutation['mutation_data']['new_copy_number']==strain2_mutation['mutation_data']['new_copy_number']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'CON':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size'] and \
                        strain1_mutation['mutation_data']['region']==strain2_mutation['mutation_data']['region']:
                        match = strain1_mutation;
                elif strain1_mutation['mutation_data']['type'] == 'INV':
                    if strain1_mutation['mutation_data']['type']==strain2_mutation['mutation_data']['type'] and \
                        strain1_mutation['mutation_data']['position']==strain2_mutation['mutation_data']['position'] and \
                        strain1_mutation['mutation_data']['size']==strain2_mutation['mutation_data']['size']:
                        match = strain1_mutation;
                else:
                    print('unknown mutation type');
                if match and \
                        matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] == 0:
                    # check that the mutation combination and pairs of strains have not already been analyzed
                    data_tmp = {};
                    data_tmp['experiment_id'] = match['experiment_id'];
                    data_tmp['sample_name'] = match['sample_name'];
                    frequency = 1.0;
                    if 'frequency' in match['mutation_data']: frequency = match['mutation_data']['frequency'];
                    data_tmp['mutation_frequency'] = frequency
                    data_tmp['mutation_position'] = match['mutation_data']['position']
                    data_tmp['mutation_type'] = match['mutation_data']['type']
                    data_tmp['endpoint_name'] = endpoint_name;
                    data_tmp['mutation_data'] = match['mutation_data'];
                    data_tmp['isUnique'] = False;
                    data_O.append(data_tmp);
                    matched_mutations[(strain1,strain1_mutation['mutation_data']['type'],strain1_mutation['mutation_data']['position'])] += 1;
                if strain1_mutation_cnt == 0: # record strain 2 mutations only once for all strain 1 mutations
                    analyzed_strain2_mutations.append((strain2_mutation['mutation_data']['type'],strain2_mutation['mutation_data']['position']));
        return matched_mutations,analyzed_strain1_mutations,analyzed_strain2_mutations,data_O;
    def _extract_commonLineageMutations(self,matched_mutations,
                        analyzed_lineage1_mutations,
                        analyzed_lineage2_mutations,
                        lineage1_mutations,lineage2_mutations,
                        lineage1,
                        lineage2_cnt,
                        endpoint_name):
        '''extract out mutations that are in common between lineages'''
        data_O = [];
        for lineage1_mutation_cnt,lineage1_mutation in enumerate(lineage1_mutations):
            print('lineage1 mutation type/position ' + lineage1_mutation['mutation_data']['type'] + '/' + str(lineage1_mutation['mutation_data']['position']));
            if lineage2_cnt == 0: # record lineage 1 mutations only once for all lineage 2 mutations
                analyzed_lineage1_mutations.append((lineage1_mutation['mutation_data']['type'],lineage1_mutation['mutation_data']['position']));
            for lineage2_mutation_cnt,lineage2_mutation in enumerate(lineage2_mutations):
                print('lineage2 mutation type/position ' + lineage2_mutation['mutation_data']['type'] + '/' + str(lineage2_mutation['mutation_data']['position']));
                if lineage2_mutation_cnt == 0 and \
                    (lineage1,lineage1_mutation['mutation_data']['type'],lineage1_mutation['mutation_data']['position']) not in matched_mutations:
                    matched_mutations[(lineage1,lineage1_mutation['mutation_data']['type'],lineage1_mutation['mutation_data']['position'])] = 0;
                # find the mutations that are common to lineage1 and lineage2
                match = self._match_mutations(lineage1_mutation,lineage2_mutation);
                if match and \
                        matched_mutations[(lineage1,lineage1_mutation['mutation_data']['type'],lineage1_mutation['mutation_data']['position'])] == 0:
                    # check that the mutation combination and pairs of lineages have not already been analyzed
                    data_tmp = {};
                    data_tmp['experiment_id'] = match['experiment_id'];
                    data_tmp['lineage_name'] = lineage1;
                    data_tmp['sample_name'] = match['sample_name'];
                    frequency = 1.0;
                    if 'frequency' in match['mutation_data']: frequency = match['mutation_data']['frequency'];
                    data_tmp['mutation_frequency'] = frequency
                    data_tmp['mutation_position'] = match['mutation_data']['position']
                    data_tmp['mutation_type'] = match['mutation_data']['type']
                    data_tmp['endpoint_name'] = endpoint_name;
                    data_tmp['mutation_data'] = match['mutation_data'];
                    data_tmp['isUnique'] = False;
                    data_O.append(data_tmp);
                    matched_mutations[(lineage1,lineage1_mutation['mutation_data']['type'],lineage1_mutation['mutation_data']['position'])] += 1;
                if lineage1_mutation_cnt == 0: # record lineage 2 mutations only once for all lineage 1 mutations
                    analyzed_lineage2_mutations.append((lineage2_mutation['mutation_data']['type'],lineage2_mutation['mutation_data']['position']));
        return matched_mutations,analyzed_lineage1_mutations,analyzed_lineage2_mutations,data_O;

    def _match_mutations(self,mutations1_I,mutations2_I):
        '''
        Determine if two mutations are a matched
        INPUT:
        mutations1_I = {} describing specific mutations
        mutations2_I = {}, same as mutations1_I for comparison #2
        OUTPUT:
        match = {}, describing the specific mutation that was matched
        '''
        # filter by mutation type-specific criteria
        match = {};
        if mutations1_I['mutation_data']['type'] == 'SNP':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['new_seq']==mutations2_I['mutation_data']['new_seq']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'SUB':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['size']==mutations2_I['mutation_data']['size'] and \
                mutations1_I['mutation_data']['new_seq']==mutations2_I['mutation_data']['new_seq']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'DEL':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['size']==mutations2_I['mutation_data']['size']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'INS':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['new_seq']==mutations2_I['mutation_data']['new_seq']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'MOB':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['repeat_name']==mutations2_I['mutation_data']['repeat_name'] and \
                mutations1_I['mutation_data']['strand']==mutations2_I['mutation_data']['strand'] and \
                mutations1_I['mutation_data']['duplication_size']==mutations2_I['mutation_data']['duplication_size']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'AMP':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['size']==mutations2_I['mutation_data']['size'] and \
                mutations1_I['mutation_data']['new_copy_number']==mutations2_I['mutation_data']['new_copy_number']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'CON':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['size']==mutations2_I['mutation_data']['size'] and \
                mutations1_I['mutation_data']['region']==mutations2_I['mutation_data']['region']:
                match = mutations1_I;
        elif mutations1_I['mutation_data']['type'] == 'INV':
            if mutations1_I['mutation_data']['type']==mutations2_I['mutation_data']['type'] and \
                mutations1_I['mutation_data']['position']==mutations2_I['mutation_data']['position'] and \
                mutations1_I['mutation_data']['size']==mutations2_I['mutation_data']['size']:
                match = mutations1_I;
        else:
            print('unknown mutation type');
        return match;