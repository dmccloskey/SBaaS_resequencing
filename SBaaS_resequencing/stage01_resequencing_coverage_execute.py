from copy import copy
#sbaas lims
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#sbaas
from .stage01_resequencing_coverage_io import stage01_resequencing_coverage_io
from .stage01_resequencing_gd_query import stage01_resequencing_gd_query
from .stage01_resequencing_analysis_query import stage01_resequencing_analysis_query
#sbaas models
from .stage01_resequencing_coverage_postgresql_models import *
#resources
from sequencing_analysis.genome_annotations import genome_annotations
from sequencing_analysis.gff_coverage import gff_coverage
from python_statistics.calculate_interface import calculate_interface

class stage01_resequencing_coverage_execute(stage01_resequencing_coverage_io,
                                           lims_biologicalMaterial_query,
                                           stage01_resequencing_gd_query,
                                           stage01_resequencing_analysis_query):
    def execute_coverageStats_fromGff(self,
                    #analysis_id_I,
                    experiment_id_I,
                    strand_start,strand_stop,scale_factor=True,downsample_factor=0,
                    sample_names_I=[]):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''
        #OPTION1
        gffcoverage = gff_coverage();

        ## get the analysis_info
        #analysis_rows = [];
        #analysis_rows = self.get_rows_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);

        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingCoverage(experiment_id_I);
        # get the data
        data_O = [];
        for sn in sample_names:
            # get the filename
            filename = None;
            filename = self.get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(experiment_id_I,sn);
            #OPTION1
            # calculate the coverage statistics
            gffcoverage.calculate_coverageStats_fromGff(filename[0], 
                strand_start,strand_stop,scale_factor=scale_factor,downsample_factor=downsample_factor,
                experiment_id_I=experiment_id_I, sample_name_I=sn);
            data_O.extend(copy(gffcoverage.coverageStats));
            gffcoverage.clear_data();
            ##OPTION2
            ## calculate the coverage statistics
            #coverateStats = [];
            #coverageStats = calculate_interface_coverageStats_fromGff(filename[0], 
            #    strand_start,strand_stop,scale_factor=scale_factor,downsample_factor=downsample_factor,
            #    experiment_id_I=experiment_id_I, sample_name_I=sn);
            #data_O.extend(coverageStats);
        #add data to the database
        self.add_dataStage01ResequencingCoverageStats(data_O); 
        
    #todo: template for amplification stats
    def execute_coverageStats_fromTable(self,analysis_id_I):
        '''Calculate coverage statistics'''
        # get the analysis_info
        analysis_rows = [];

        # get the data
        data_O = [];
        for cnt,analysis in analysis_rows:
            # get the sample_names
            experiment_id = analysis['experiment_id'];
            sn = analysis['sample_name'];
            # get chromosomes
            chromosomes = [];

            for chromosome in chromosomes:
                # get strands
                strands = []

                for strand in strands:
                    # get the indices/reads and other information
                    start,stop = None,None;
                    
                    data_indices,data_reads = [],[];

                    # calculate the descriptive statistics
                    data_TTest = {};
                    data_TTest = self.r_calc.calculate_oneSampleTTest(data_reads, alternative_I = "two.sided", mu_I = 0, paired_I="FALSE", var_equal_I = "TRUE", ci_level_I = 0.95, padjusted_method_I = "bonferroni");
                    # calculate the interquartile range
                    min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
                    min_O, max_O, median_O, iq_1_O, iq_3_O=calculate_interface.calculate_interquartiles(data_reads);
                    # record data for
                    data_O.append({
                        'analysis_id':analysis_id,
                        'experiment_id':experiment_id,
                        'sample_name':sn,
                        'genome_chromosome':chromosome,
                        'genome_strand':strand,
                        'strand_start':start,
                        'strand_stop':stop,
                        'reads_min':min_O,
                        'reads_max':max_O,
                        'reads_lb':data_TTest['ci_lb'],
                        'reads_ub':data_TTest['ci_ub'],
                        'reads_iq1':iq_1_O,
                        'reads_iq3':iq_3_O,
                        'reads_median':median_O,
                        'reads_mean':data_TTest['mean'],
                        'reads_var':data_TTest['var'],
                        'reads_n':len(data_reads)
                        })
        self.add_dataStage01ResequencingCoverageStats(data_O);

    def execute_findAmplifications_fromGff(self,
                #analysis_id_I,
                experiment_id_I,
                strand_start, strand_stop,
                sample_names_I = [],
                scale_factor=True, downsample_factor=0,reads_min=1.5,reads_max=5.0, indices_min=200,consecutive_tol=10):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''

        #from sequencing_utilities.coverage import extract_strandsFromGff,find_highCoverageRegions

        # get the data
        data_O = [];
        #OPTION1
        gffcoverage = gff_coverage();

        # get the sample_names
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingCoverage(experiment_id_I);
        #for cnt,analysis in analysis_rows:
        #    # get the sample_names and experiment_ids
        #    experiment_id = analysis['experiment_id'];
        #    sn = analysis['sample_name'];
        #    filename = analysis['data_dir']
        for cnt,sn in enumerate(sample_names):
            # get the data_dir
            filename = [];
            filename = self.get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(experiment_id_I,sn);
            #OPTION1
            gffcoverage.find_amplifications_fromGff(filename[0],strand_start, strand_stop, experiment_id, sn, scale=scale_factor, downsample=downsample_factor)
            data_O.extend(copy(gffcoverage.amplifications))
            gffcoverage.clear_data();
            #OPTION2
            #amplifications = [];
            #amplifications = self.find_amplifications_fromGff(filename[0],strand_start, strand_stop, experiment_id, sn, scale=scale_factor, downsample=downsample_factor)
            #data_O.extend(amplifications)

        # add data to the DB
        self.add_dataStage01ResequencingAmplifications(data_O);
    def execute_amplificationStats_fromTable(self,
                #analysis_id_I,
                experiment_id_I,
                sample_names_I=[]):
        '''Calculate coverage statistics'''

        # get the data
        data_O = [];

        ## get the analysis_info
        #analysis_rows = [];
        ## query information from amplification table

        #for cnt,analysis in analysis_rows:
        #    # get the sample_names
        #    experiment_id = analysis['experiment_id'];
        #    sn = analysis['sample_name'];

        # get the sample_names
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingAmplifications(experiment_id_I);
        for cnt,sn in enumerate(sample_names):
            # get chromosomes
            chromosomes = [];
            chromosomes = self.get_chromosomes_experimentIDAndSampleName_dataStage01ResequencingAmplifications(experiment_id_I,sn);
            for chromosome in chromosomes:
                # get strands
                strands = []
                strands = self.get_strands_experimentIDAndSampleNameAndChromosome_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome);
                # remove visualization regions
                strands = [s for s in strands if not 'mean' in s];
                for strand in strands:
                    # get the start and stop of the indices
                    genomic_starts,genomic_stops = [],[]
                    genomic_starts,genomic_stops = self.get_startAndStops_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    # get the start and stop regions
                    starts,stops = [],[]
                    starts,stops = self.get_amplificationRegions_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    # get the indices/reads and other information
                    for start_cnt,start in enumerate(starts):
                        data_indices,data_reads = [],[];
                        data_indices,data_reads = self.get_genomeIndexAndReads_experimentIDAndSampleNameAndChromosomeAndStrandAndAmplificationRegions_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand,start,stops[start_cnt]);
                        # calculate using scipy
                        data_ave_O, data_var_O, data_lb_O, data_ub_O = calculate_interface.calculate_ave_var(data_reads,confidence_I = 0.95);
                        # calculate the interquartile range
                        min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
                        min_O, max_O, median_O, iq_1_O, iq_3_O=calculate_interface.calculate_interquartiles(data_reads);
                        # record data for
                        data_O.append({
                            #'analysis_id':analysis_id,
                            'experiment_id':experiment_id_I,
                            'sample_name':sn,
                            'genome_chromosome':chromosome,
                            'genome_strand':strand,
                            'strand_start':genomic_starts[0],
                            'strand_stop':genomic_stops[0],
                            'reads_min':min_O,
                            'reads_max':max_O,
                            #'reads_lb':data_TTest['ci_lb'],
                            #'reads_ub':data_TTest['ci_ub'],
                            'reads_lb':data_lb_O,
                            'reads_ub':data_ub_O,
                            'reads_iq1':iq_1_O,
                            'reads_iq3':iq_3_O,
                            'reads_median':median_O,
                            #'reads_mean':data_TTest['mean'],
                            #'reads_var':data_TTest['var'],
                            'reads_mean':data_ave_O,
                            'reads_var':data_var_O,
                            'reads_n':len(data_reads),
                            'amplification_start':start,
                            'amplification_stop':stops[start_cnt],
                            'used_':True,
                            'comment_':None
                            })
        # add data to the DB
        self.add_dataStage01ResequencingAmplificationStats(data_O);
    def execute_findAmplificationsAndCalculateStats_fromGff(self,
                #analysis_id_I,
                experiment_id_I,
                strand_start, strand_stop,
                sample_names_I = [],
                scale_factor=True, downsample_factor=2000,reads_min=1.5,reads_max=5.0, indices_min=200,consecutive_tol=10):
        '''Calculate coverage statistics from gff file
        NOTE: multiple chromosomes not yet supported in sequencing_utilities'''

        # get the data
        data_O = [];
        stats_O = [];
        #OPTION1
        gffcoverage = gff_coverage();

        ## get the analysis_info
        #analysis_rows = [];
        # query information from coverage table

        # get the sample_names
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingCoverage(experiment_id_I);
        #for cnt,analysis in analysis_rows:
        #    # get the sample_names and experiment_ids
        #    experiment_id = analysis['experiment_id'];
        #    sn = analysis['sample_name'];
        #    filename = analysis['data_dir']
        for cnt,sn in enumerate(sample_names):
            # get the data_dir
            filename = [];
            filename = self.get_dataDirs_experimentIDAndSampleName_dataStage01ResequencingCoverage(experiment_id_I,sn);
            #OPTION1
            # find amplifications and calculate stats
            gffcoverage.findAndCalculate_amplificationStats_fromGff(filename[0],strand_start, strand_stop, experiment_id_I=experiment_id, sample_name_I=sn, indices_min = indices_min, consecutive_tol = consecutive_tol, scale_factor=scale_factor, downsample_factor=downsample_factor)
            data_O.extend(copy(gffcoverage.amplifications));
            stats_O.extend(copy(gffcoverage.amplificationStats));
            gffcoverage.clear_data();
            ##OPTION2
            ## find amplifications and calculate stats
            #amplifications,amplificationStats=[],[];
            #amplifications,amplificationStats = self.findAndCalculate_amplificationStats_fromGff(filename[0],strand_start, strand_stop, experiment_id_I=experiment_id, sample_name_I=sn, indices_min = indices_min, consecutive_tol = consecutive_tol, scale_factor=scale_factor, downsample_factor=downsample_factor)
            #data_O.extend(amplifications);
            #stats_O.extend(amplificationStats);
        # add data to the DB
        self.add_dataStage01ResequencingAmplifications(data_O);
        self.add_dataStage01ResequencingAmplificationStats(stats_O);
    def execute_annotateAmplifications(self,experiment_id_I,sample_names_I=[],ref_genome_I='data/U00096.2.gb',ref_I = 'genbank',biologicalmaterial_id_I='MG1655'):
        '''Annotate mutations for date_stage01_resequencing_endpoints
        based on position, reference genome, and reference genome biologicalmaterial_id'''
        
        genomeannotation = genome_annotations(annotation_I=ref_genome_I,annotation_ref_I=ref_I);

        print('Executing annotateAmplifications...')
        data_O = [];
        experiment_id = experiment_id_I;
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_names = self.get_sampleNames_experimentID_dataStage01ResequencingAmplifications(experiment_id);
        for cnt,sn in enumerate(sample_names):
            print('annotating amplifications for sample_name ' + sn);
            # get chromosomes
            chromosomes = [];
            chromosomes = self.get_chromosomes_experimentIDAndSampleName_dataStage01ResequencingAmplifications(experiment_id_I,sn);
            for chromosome in chromosomes:
                # get strands
                strands = []
                strands = self.get_strands_experimentIDAndSampleNameAndChromosome_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome);
                # remove visualization regions
                strands = [s for s in strands if not 'mean' in s];
                for strand in strands:
                    # get the start and stop of the indices
                    genomic_starts,genomic_stops = [],[]
                    genomic_starts,genomic_stops = self.get_startAndStops_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    # get the start and stop regions
                    starts,stops = [],[]
                    starts,stops = self.get_amplificationRegions_experimentIDAndSampleNameAndChromosomeAndStrand_dataStage01ResequencingAmplifications(experiment_id_I,sn,chromosome,strand);
                    for start_cnt,start in enumerate(starts):
                        # annotate each mutation based on the position
                        annotations = [];
                        annotations = genomeannotation._find_genesInRegion(start,stops[start_cnt])
                        for annotation in annotations:
                            # record the data
                            tmp = {
                                'experiment_id':experiment_id,
                                'sample_name':sn,
                                'genome_chromosome':chromosome,
                                'genome_strand':strand,
                                'strand_start':genomic_starts[0],
                                'strand_stop':genomic_stops[0],
                                'amplification_start':start,
                                'amplification_stop':stops[start_cnt],
                                'used_':True,
                                'comment_':None};
                            tmp['feature_genes'] = annotation['gene']
                            tmp['feature_locations'] = annotation['location']
                            tmp['feature_annotations'] = annotation['product']
                            tmp['feature_start'] = annotation['start'];
                            tmp['feature_stop'] = annotation['stop'];
                            tmp['feature_types'] = annotation['type']
                            # generate a link to ecogene for the genes
                            tmp['feature_links'] = [];
                            for bnumber in annotation['locus_tag']:
                                if bnumber:
                                    ecogenes = [];
                                    ecogenes = self.get_ecogeneAccessionNumber_biologicalmaterialIDAndOrderedLocusName_biologicalMaterialGeneReferences(biologicalmaterial_id_I,bnumber);
                                    if ecogenes:
                                        ecogene = ecogenes[0];
                                        ecogene_link = genomeannotation._generate_httplink2gene_ecogene(ecogene['ecogene_accession_number']);
                                        tmp['feature_links'].append(ecogene_link)
                                    else: print('no ecogene_accession_number found for ordered_locus_location ' + bnumber);
                            data_O.append(tmp);
        # update rows in the database
        self.add_dataStage01ResequencingAmplificationAnnotations(data_O);