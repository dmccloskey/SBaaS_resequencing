

#sbaas
from .stage01_resequencing_count_io import stage01_resequencing_count_io
from .stage01_resequencing_count_dependencies import stage01_resequencing_count_dependencies
from .stage01_resequencing_mutations_query import stage01_resequencing_mutations_query
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
#sbaas models
from .stage01_resequencing_count_postgresql_models import *
#resources
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_count import calculate_count

class stage01_resequencing_count_execute(
            stage01_resequencing_count_io,
            stage01_resequencing_mutations_query,
            stage01_resequencing_analysis_query,
            stage01_resequencing_count_dependencies,
            ):

    def execute_countElementsInFeatures(self,analysis_id_I,features_I=[]):
        '''count unique features of discrete or categorical data
        INPUT:
        analysis_id_I = string,
        features_I = [] of string, e.g. ['mutation_class','mutation_position','mutation_type','mutation_genes','mutation_locations','mutation_id']

        OUTPUT:
        '''
        data_O = [];
        calculatecount = calculate_count();
        #get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = self.get_experimentIDAndSampleName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        #bin each feature
        for features_cnt,features in enumerate(features_I):
            if features == 'mutation_class':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_allMutationClasses_experimentIDAndSampleName_dataStage01ResequencingMutationsSeqChanges(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_count.extend(data_tmp);
                #count the elements of each feature
                elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_count);
                data_O.extend(self.record_count(analysis_id_I,features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_position':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationPositions_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_count.extend(data_tmp);
                #count the elements of each feature
                elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_count);
                data_O.extend(self.record_count(analysis_id_I,features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_type':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationTypes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_count.extend(data_tmp);
                #count the elements of each feature
                elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_count);
                data_O.extend(self.record_count(analysis_id_I,features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_genes':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationGenes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_count.extend(data_tmp);
                #count the elements of each feature
                elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_count);
                data_O.extend(self.record_count(analysis_id_I,features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_locations':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationLocations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_count.extend(data_tmp);
                #count the elements of each feature
                elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_count);
                data_O.extend(self.record_count(analysis_id_I,features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_id':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationIDs_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_count.extend(data_tmp);
                #count the elements of each feature
                elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_count);
                data_O.extend(self.record_count(analysis_id_I,features,'',elements_unqiue,elements_count,elements_count_fraction));
            else:
                print('feature not recongnized');
        #add the data to the database
        self.add_dataStage01ResequencingCount(data_O);

    def execute_countElementsInFeaturesPerSample(self,analysis_id_I,features_I=[]):
        '''count unique features of discrete or categorical data per sample
        INPUT:
        analysis_id_I = string,
        features_I = [] of string, e.g. ['mutation_class','mutation_position','mutation_type','mutation_genes','mutation_locations','mutation_id']
        OUTPUT:
        '''
        data_O = [];
        calculatecount = calculate_count();
        # get the analysis information
        experiment_ids = []
        lineage_names = []
        sample_names = []
        time_points = []
        experiment_ids,lineage_names,sample_names,time_points = self.get_experimentIDAndLineageNameAndSampleNameAndTimePoint_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        #order by time_points and convert to intermediates
        intermediates,time_points,experiment_ids,sample_names,lineage_names = self.convert_timePoints2Intermediates(time_points,experiment_ids,sample_names,lineage_names)
        #bin each feature
        for features_cnt,features in enumerate(features_I):
            if features == 'mutation_class':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_allMutationClasses_experimentIDAndSampleName_dataStage01ResequencingMutationsSeqChanges(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        #count the elements of each feature
                        elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_tmp);
                        data_O.extend(self.record_countPerSample(analysis_id_I,experiment_ids[sn_cnt],lineage_names[sn_cnt],sn,time_points[sn_cnt],features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_position':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationPositions_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        #count the elements of each feature
                        elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_tmp);
                        data_O.extend(self.record_countPerSample(analysis_id_I,experiment_ids[sn_cnt],lineage_names[sn_cnt],sn,time_points[sn_cnt],features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_type':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationTypes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        #count the elements of each feature
                        elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_tmp);
                        data_O.extend(self.record_countPerSample(analysis_id_I,experiment_ids[sn_cnt],lineage_names[sn_cnt],sn,time_points[sn_cnt],features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            elif features == 'mutation_genes':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationGenes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        #count the elements of each feature
                        elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_tmp);
                        data_O.extend(self.record_countPerSample(analysis_id_I,experiment_ids[sn_cnt],lineage_names[sn_cnt],sn,time_points[sn_cnt],features,'',elements_unqiue,elements_count,elements_count_fraction));  
            elif features == 'mutation_locations':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationLocations_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        #count the elements of each feature
                        elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_tmp);
                        data_O.extend(self.record_countPerSample(analysis_id_I,experiment_ids[sn_cnt],lineage_names[sn_cnt],sn,time_points[sn_cnt],features,'',elements_unqiue,elements_count,elements_count_fraction));  
            elif features == 'mutation_id':
                data_count = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = self.get_AllMutationIDs_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        #count the elements of each feature
                        elements_unqiue,elements_count,elements_count_fraction = calculatecount.count_elements(data_tmp);
                        data_O.extend(self.record_countPerSample(analysis_id_I,experiment_ids[sn_cnt],lineage_names[sn_cnt],sn,time_points[sn_cnt],features,'',elements_unqiue,elements_count,elements_count_fraction)); 
            else:
                print('feature not recongnized');
        #add the data to the database
        self.add_dataStage01ResequencingCountPerSample(data_O);