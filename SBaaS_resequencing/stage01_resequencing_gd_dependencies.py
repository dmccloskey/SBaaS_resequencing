#Resources
from sequencing_utilities import gdparse

class stage01_resequencing_gd_dependencies():
    #no def __init__
    
    def format_mutationData(self,mutationData_I):
        """converts '{}' to {}"""
        for mutationData in mutationData_I:
            if 'mutation_data' in mutationData and type(mutationData['mutation_data'])==type('string'):
                mutationData['mutation_data'] = eval(mutationData['mutation_data']);
            if 'mutation_genes' in mutationData and type(mutationData['mutation_genes'])==type('string'):
                mutationData['mutation_genes'] = eval(mutationData['mutation_genes']);
            if 'mutation_locations' in mutationData and type(mutationData['mutation_locations'])==type('string'):
                mutationData['mutation_locations'] = eval(mutationData['mutation_locations']);
            if 'mutation_annotations' in mutationData and type(mutationData['mutation_annotations'])==type('string'):
                mutationData['mutation_annotations'] = eval(mutationData['mutation_annotations']);
            if 'mutation_frequency' in mutationData and type(mutationData['mutation_frequency'])==type('string'):
                mutationData['mutation_frequency'] = eval(mutationData['mutation_frequency']);
            if 'mutation_position' in mutationData and type(mutationData['mutation_position'])==type('string'):
                mutationData['mutation_position'] = eval(mutationData['mutation_position']);
        return mutationData_I;

    def import_gd(self, filename, experiment_id='', sample_name=''):
        """import and parse .gd file
        INPUT:
        filename = string, directory and filename of the .gd file

        OPTIONAL INPUT:
        the following are optional for analyzing a single sample,
        but required when analyzing multiple samples

        experiment_id = string, name of the experiment that generated the sample
        sample_name = string, name of the sample

        """
        gd = gdparse.GDParser(file_handle=open(filename, 'r'))
        # extract out ids
        mutation_ids = [];
        mutation_ids = list(gd.data['mutation'].keys())
        parent_ids = [];
        for mid in mutation_ids:
            parents = [];
            parents = gd.data['mutation'][mid]['parent_ids'];
            parent_ids.extend(parents);
        # split into seperate data structures based on the destined table add
        metadata_data = [];
        mutation_data = [];
        evidence_data = [];
        validation_data = [];
        if gd.metadata:
            metadata_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'genome_diff':gd.metadata['GENOME_DIFF'],
                                 'refseq':gd.metadata['REFSEQ'],
                                 'readseq':gd.metadata['READSEQ'],
                                 'author':gd.metadata['AUTHOR']});
        if gd.data['mutation']:
            for mid in mutation_ids:
                mutation_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'mutation_id':mid,
                                 'parent_ids':gd.data['mutation'][mid]['parent_ids'],
                                 'mutation_data':gd.data['mutation'][mid]});
                                 #'mutation_data':json.dumps(gd.data['mutation'][mid])});
        if gd.data['evidence']:
            for pid in parent_ids:
                evidence_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'parent_id':pid,
                                 'evidence_data':gd.data['evidence'][pid]});
                                 #'evidence_data':json.dumps(gd.data['evidence'][pid])});
        if gd.data['validation']:
            for mid in mutation_ids:
                validation_data.append({'experiment_id':experiment_id,
                                 'sample_name':sample_name,
                                 'validation_id':mid,
                                 'validation_data':gd.data['validation'][mid]});
                                 #'validation_data':json.dumps(gd.data['validation'][mid])});
        # add data to the database:
        return metadata_data, mutation_data, evidence_data, validation_data;

    def _make_mutationID(self,mutation_genes,mutation_type,mutation_position):
        '''return a unique mutation id string'''
        mutation_genes_str = '';
        for gene in mutation_genes:
            mutation_genes_str = mutation_genes_str + gene + '-/-'
        mutation_genes_str = mutation_genes_str[:-3];
        mutation_id = mutation_type + '_' + mutation_genes_str + '_' + str(mutation_position);
        return mutation_id;

    def _make_mutationID2(self,mutation_genes,mutation_type,mutation_position,nt_ref,nt_new):
        '''return a unique mutation id string'''
        mutation_genes_str = '';
        for gene in mutation_genes:
            mutation_genes_str = mutation_genes_str + gene + '-/-'
        mutation_genes_str = mutation_genes_str[:-3];
        mutation_id = mutation_type + '_' + mutation_genes_str + '_' + nt_ref + str(mutation_position) + nt_new;
        return mutation_id;

    def _filter_evidenceByPValueAndQualityAndFrequency(self,data_I,p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1):
        """return data this is above the p-value, quality, and frequency criteria"""
        
        data_filtered = [];
        data_filtered_dict = {};
        for d in data_I:
            if d['evidence_data']['type'] == 'RA':
                #population only
                if 'quality' in d['evidence_data'] and \
                    'bias_p_value' in d['evidence_data'] and \
                    'fisher_strand_p_value' in d['evidence_data'] and \
                    'frequency' in d['evidence_data'] and \
                    d['evidence_data']['frequency'] >= frequency_criteria and \
                    d['evidence_data']['quality'] >= quality_criteria and \
                    d['evidence_data']['bias_p_value'] <= p_value_criteria and \
                    d['evidence_data']['fisher_strand_p_value'] <= p_value_criteria:
                    data_filtered_dict = d;
                    data_filtered.append(d);
                #population and isolate
                elif 'quality' in d['evidence_data'] and \
                    'frequency' in d['evidence_data'] and \
                    d['evidence_data']['frequency'] >= frequency_criteria and \
                    d['evidence_data']['quality'] >= quality_criteria:
                    data_filtered_dict = d;
                    data_filtered.append(d);
            elif d['evidence_data']['type'] == 'JC':
                data_filtered_dict = d;
                data_filtered.append(d);
            elif d['evidence_data']['type'] == 'MC':
                data_filtered_dict = d;
                data_filtered.append(d);
            elif d['evidence_data']['type'] == 'UN':
                data_filtered_dict = d;
                data_filtered.append(d);
            else:
                print('mutation evidence of type ' + d['evidence_data']['type'] +\
                    ' has not yet been included in the filter criteria');
        return data_filtered;