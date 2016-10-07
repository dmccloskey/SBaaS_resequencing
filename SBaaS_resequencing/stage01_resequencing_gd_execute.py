'''resequencing class'''
from copy import copy
#sbaas
from .stage01_resequencing_gd_io import stage01_resequencing_gd_io
#sbaas models
from .stage01_resequencing_gd_postgresql_models import *
#resources
from sequencing_analysis.genome_diff import genome_diff
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_interface import calculate_interface

class stage01_resequencing_gd_execute(stage01_resequencing_gd_io):
    
    #Analysis
    def execute_filterMutations_population(self,experiment_id,p_value_criteria=0.01,quality_criteria=6.0,frequency_criteria=0.1,sample_names_I=None):
        '''Filter mutations that do not meet the desired criteria
        INPUT:
        experiment_id = string
        p_value_criteria = float, minimum breseq p-value
        quality_criteria = float, minimum breseq quality score
        frequency_criteria = float, minimum breseq frequency of mutation in the population
        sample_names_I = [] of strings, specific sample names to use in the experiment
        '''

        print('Executing filterMutations_population...')
        data_O = [];
        # query sample names from the experiment
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingMetadata(experiment_id);
        for sn in sample_names:
            print('Filtering mutations for sample_name ' + sn);
            #query mutation data filtered by frequency
            data_mutations_list = [];
            data_mutations_list = self.get_mutations_experimentIDAndSampleName_dataStage01ResequencingMutations(experiment_id,sn,frequency_criteria=frequency_criteria);
            for data_mutations in data_mutations_list:
                print('Filtering mutations for mutation id ' + str(data_mutations['mutation_id']));
                #query data filtered by evidence-specific criteria
                data_evidence_list = [];
                for pid in data_mutations['parent_ids']:
                    print('Filtering mutations for parent id ' + str(pid));
                    data_evidence_dict = {};
                    data_evidence_dict = self.get_evidence_experimentIDAndSampleNameAndParentID_dataStage01ResequencingEvidence(experiment_id,sn,pid,
                                                    p_value_criteria=p_value_criteria,quality_criteria=quality_criteria,frequency_criteria=frequency_criteria);
                    data_evidence_list.append(data_evidence_dict);
                if data_evidence_list[0]: #check that filtered evidence was found
                    data_O.append(data_mutations);
        #add data to the database table
        self.add_dataStage01ResequencingMutationsFiltered(data_O);
