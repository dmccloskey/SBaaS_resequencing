#sbaas
from .stage01_resequencing_histogram_io import stage01_resequencing_histogram_io
from .stage01_resequencing_histogram_dependencies import stage01_resequencing_histogram_dependencies
from .stage01_resequencing_mutations_query import stage01_resequencing_mutations_query
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
#sbaas models
from .stage01_resequencing_histogram_postgresql_models import *
#resources
from sequencing_analysis.genome_annotations import genome_annotations
from python_statistics.calculate_histogram import calculate_histogram

class stage01_resequencing_histogram_execute(
            stage01_resequencing_histogram_io,
            stage01_resequencing_histogram_dependencies
            ):
    def execute_binFeatures(self,analysis_id_I,features_I=[],n_bins_I=[]):
        '''bin features of continuous data
        INPUT:
        analysis_id_I = string,
        features_I = [] of string, e.g. ['mutation_position','mutation_frequency']
        n_bins_I = int, the number of bins per feature (if bins is empty, bins will be calculated)

        OUTPUT:
        '''
        data_O = [];
        calculatehistogram = calculate_histogram();

        resequencing_mutations_query = stage01_resequencing_mutations_query(self.session,self.engine,self.settings)
        resequencing_analysis_query = stage01_resequencing_analysis_query(self.session,self.engine,self.settings);

        #get the analysis information
        experiment_ids,sample_names = [],[];
        experiment_ids,sample_names = resequencing_analysis_query.get_experimentIDAndSampleName_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        #bin each feature
        for features_cnt,features in enumerate(features_I):
            n_bins = 50;
            calc_bins_I = True;
            if n_bins_I and n_bins_I[features_cnt]:
                n_bins = n_bins_I[features_cnt];
                calc_bins_I = False;
            if features == 'mutation_position':
                data_hist = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = resequencing_mutations_query.get_AllMutationPositions_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_hist.extend(data_tmp);
                #make the bins for the histogram
                x_O,dx_O,y_O = calculatehistogram.histogram(data_I=data_hist,n_bins_I=n_bins,calc_bins_I=calc_bins_I);
                tmp = self.record_histogram(analysis_id_I,features,'',x_O,dx_O,y_O);
                data_O.extend(tmp);
            
            #elif features == 'mutation_chromosome':
            #    data_hist = [];
            #    #get all the data for the analysis
            #    for sn_cnt,sn in enumerate(sample_names):
            #        data_tmp = [];
            #        data_tmp = resequencing_mutations_query.get_AllMutationChromosomes_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
            #        if data_tmp:
            #            data_hist.extend(data_tmp);
            #    #make the bins for the histogram
            #    x_O,dx_O,y_O = calculatehistogram.histogram(data_I=data_hist,n_bins_I=n_bins,calc_bins_I=calc_bins_I);
            #    tmp = self.record_histogram(analysis_id_I,features,'',x_O,dx_O,y_O);
            #    data_O.extend(tmp);
            
            #elif features == 'mutation_chromosomeAndPosition':
            #    data_hist = [];
            #    #get all the data for the analysis
            #    for sn_cnt,sn in enumerate(sample_names):
            #        data_tmp = [];
            #        data_tmp = resequencing_mutations_query.get_AllMutationChromosomesAndPositions_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
            #        if data_tmp:
            #            data_hist.extend(data_tmp);
            #    #make the bins for the histogram
            #    x_O,dx_O,y_O = calculatehistogram.histogram(data_I=data_hist,n_bins_I=n_bins,calc_bins_I=calc_bins_I);
            #    tmp = self.record_histogram(analysis_id_I,features,'',x_O,dx_O,y_O);
            #    data_O.extend(tmp);
                    
            elif features == 'mutation_frequency':
                data_hist = [];
                #get all the data for the analysis
                for sn_cnt,sn in enumerate(sample_names):
                    data_tmp = [];
                    data_tmp = resequencing_mutations_query.get_AllMutationFrequencies_experimentIDAndSampleName_dataStage01ResequencingMutationsAnnotated(experiment_ids[sn_cnt],sn);
                    if data_tmp:
                        data_hist.extend(data_tmp);
                #make the bins for the histogram
                x_O,dx_O,y_O = calculatehistogram.histogram(data_I=data_hist,n_bins_I=n_bins,calc_bins_I=calc_bins_I);
                tmp = self.record_histogram(analysis_id_I,features,'',x_O,dx_O,y_O);
                data_O.extend(tmp);
            else:
                print('feature not recongnized');
        #add the data to the database
        self.add_dataStage01ResequencingHistogram(data_O);