from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from sequencing_utilities.makegff import write_samfile_to_gff
from python_statistics.calculate_interface import calculate_interface
import pandas, numpy
from matplotlib.pyplot import subplot, fill_between, xlabel, xlim, \
    ylim, setp, savefig, figure

class stage01_resequencing_coverage_dependencies():
    #no def __init__
    def convert_bam2gff(self,bam_file):
        '''convert a bam file to a gff file'''

        filename = filename.replace('.bam','.gff');
        extract_strandsFromGff(bam_file,filename,separate_strand=False);
        print(bam_file + " converted to " + filename);
        # record the .gff filename
        return filename;

    def extract_strandsFromGff(self, gff_file, left, right, scale=True, downsample=0):
        """convert a gff file to a table of positions and reads

        Input:
        gff_file: gff file to read
        left: left position to start analysis
        right: right position to end analysis
        scale: reads will be normalized to have 100 max
        downsample: the number of positions to downsample to

        Output:
        plus: table [index,reads] for the plus strand
        minus: table [index,reads] for the minus strand
        """
        # sometimes the first line is a comment which pandas can't handle
        skiprows = 0
        with open(gff_file, "r") as infile:
            if infile.read(1) == "#":
                skiprows = 1
        table = pandas.read_table(gff_file, header=None,
            usecols=[0, 2, 3, 4, 5, 6], comment="#", skiprows=skiprows,
            names=["chromosome", "name", "leftpos", "rightpos", "reads", "strand"])
        table = table[(table.rightpos >= left) & (table.leftpos <= right)]
        # TODO - detect if chromsome_plus and chromosome_minus
        if len(table.chromosome.unique()) > 1:
            raise Exception("multiple chromosomes not supported")
        if (table.leftpos == table.rightpos).all():  # each line is one point
            table = table[["leftpos", "reads", "strand"]]
        table_plus = table[table.strand == "+"].set_index("leftpos")
        table_minus = table[table.strand == "-"].set_index("leftpos")
        # fill missing values with 0
        filler = pandas.Series([range(left, right + 1)], [range(left, right + 1)])
        table_plus["filler"] = 1
        table_minus["filler"] = 1
        table_plus.fillna(0)
        table_minus.fillna(0)
        # extract only the series we need
        plus = table_plus.reads
        minus = table_minus.reads.abs()  # in case stored negative
        if scale:
            plus *= 100. / plus.max()
            minus *= 100. / minus.max()
        # downsample
        collapse_factor = None;
        if downsample > 1:
            collapse_factor = int((right - left) / downsample)
        if collapse_factor and collapse_factor > 1:
            plus = plus.groupby(lambda x: x // collapse_factor).mean()
            plus.index *= collapse_factor
            minus = minus.groupby(lambda x: x // collapse_factor).mean()
            minus.index *= collapse_factor
        return plus,minus;

    def find_highCoverageRegions(self,plus,minus, coverage_min=1.5,coverage_max=5.0,
                points_min=200,consecutive_tol=10):
        '''Find regions of high coverage

        Input:
        plus: plus strand
        minus: minus strand
        coverage_min: minimum coverage of a high coverage region
        coverage_max: maximum coverage of a high coverage region
        points_min: minimum number of points of a high coverage region
        consecutive_tol: maximum number of consecutive points that do not meet the coverage_min/max criteria that can be included a high coverage region

        Output:
        '''
        
        # find indices that are within the min/max coverage
        plus_high = plus[(plus>=coverage_min*float(plus.mean())) & (plus<=coverage_max*float(plus.mean()))];
        minus_high = minus[(minus>=coverage_min*float(minus.mean())) & (minus<=coverage_max*float(minus.mean()))];
        # find indices that meet the minimum number of consecutive points and consecutive point count tolerance limit
        plus_high_regions = plus_high*0;
        minus_high_regions = minus_high*0;
        plus_high_region_summary = [];
        minus_high_region_summary = [];
        cnt = 0;
        for index,value in plus_high.iteritems():
            # initialize all tmp variables and iterators
            if cnt==0: 
                high_regions_tmp = plus_high*0;
                previous = index;
                consecutive_points = 0;
                start=index;
                cnt += 1;
                continue;
            # check for regions of high coverage that
            if index-previous<=consecutive_tol: # 1 satisfy the consecutive tol
                # case for all points but the last point
                # update current high region and iterate counters
                if cnt<len(plus_high)-1:
                    high_regions_tmp[index]=value;
                    consecutive_points += 1;
                    previous = index;
                # case for the last point
                # update all high regions (points_min satisfied)
                elif consecutive_points >= points_min: # 2 satisfy the consecutive points
                    plus_high_regions=self.record_highCoverageRegions(high_regions_tmp,plus_high_regions)
                    plus_high_region_summary.append({'start':start,'stop':index,'mean':high_regions_tmp[high_regions_tmp>0].mean()});    
            else:
                # update all high regions and reset (points_min satisfied)
                if consecutive_points >= points_min:
                    plus_high_regions=self.record_highCoverageRegions(high_regions_tmp,plus_high_regions)
                    plus_high_region_summary.append({'start':start,'stop':index,'mean':high_regions_tmp[high_regions_tmp>0].mean()});
                    previous = index;
                    consecutive_points = 0;
                    start=index;
                    high_regions_tmp = plus_high*0;
                    # reset variables and counters
                else:
                    high_regions_tmp = plus_high*0;
                    previous = index;
                    consecutive_points = 0;
                    start=index;
            # update the counter
            cnt += 1;
        cnt = 0;
        for index,value in minus_high.iteritems():
            # initialize all tmp variables and iterators
            if cnt==0: 
                high_regions_tmp = minus_high*0;
                previous = index;
                consecutive_points = 0;
                start=index;
                cnt += 1;
                continue;
            # check for regions of high coverage that
            if index-previous<=consecutive_tol: # 1 satisfy the consecutive tol
                # case for all points but the last point
                # update current high region and iterate counters
                if cnt<len(minus_high)-1:
                    high_regions_tmp[index]=value;
                    consecutive_points += 1;
                    previous = index;
                # case for the last point
                # update all high regions (points_min satisfied)
                elif consecutive_points >= points_min: # 2 satisfy the consecutive points
                    minus_high_regions=self.record_highCoverageRegions(high_regions_tmp,minus_high_regions)
                    minus_high_region_summary.append({'start':start,'stop':index,'mean':high_regions_tmp[high_regions_tmp>0].mean()});    
            else:
                # update all high regions and reset (points_min satisfied)
                if consecutive_points >= points_min:
                    minus_high_regions=self.record_highCoverageRegions(high_regions_tmp,minus_high_regions)
                    minus_high_region_summary.append({'start':start,'stop':index,'mean':high_regions_tmp[high_regions_tmp>0].mean()});
                    previous = index;
                    consecutive_points = 0;
                    start=index;
                    high_regions_tmp = minus_high*0;
                    # reset variables and counters
                else:
                    high_regions_tmp = minus_high*0;
                    previous = index;
                    consecutive_points = 0;
                    start=index;
            # update the counter
            cnt += 1;
        # filter out all 0 values
        plus_high_regions = plus_high_regions[plus_high_regions>0];
        minus_high_regions = minus_high_regions[minus_high_regions>0];
        # record the data

        return plus_high_region_summary,minus_high_region_summary,plus_high_regions, minus_high_regions

    def record_highCoverageRegions(self,high_region,high_regions):
        '''Record high coverage region index and reads to master list of all high regions indices and reads'''
        high_regions += high_region;
        return high_regions;
    
    def plot_strands(self,plus,minus,left,right,scale=True, output=None,
                  coverage_max=5.0, downsample=2000):
        '''Plot strand coverage using matplotlib

        Input:
        plus: table [index,reads] for the plus strand
        minus: table [index,reads] for the minus strand
        left: left position to start analysis
        right: right position to end analysis
        scale: reads will be normalized to have 100 max
        output: output file
        coverage_max: maximum read coverage to plot
        downsample: the number of positions to downsample to

        Output:
        plus: table [index,reads] for the plus strand
        minus: table [index,reads] for the minus strand'''

        ## fill missing values with 0
        #filler = pandas.Series([range(left, right + 1)])
        #plus = filler + plus;
        #minus = filler + minus;
        # scale
        if scale:
            plus *= 100. / plus.max()
            minus *= 100. / minus.max()
        # downsample
        collapse_factor = None;
        if downsample > 1:
            collapse_factor = int((right - left) / downsample)
        if collapse_factor and collapse_factor > 1:
            plus = plus.groupby(lambda x: x // collapse_factor).mean()
            plus.index *= collapse_factor
            minus = minus.groupby(lambda x: x // collapse_factor).mean()
            minus.index *= collapse_factor;
        # plot the figure:
        fig=figure()
        ax = subplot(1,1,1)
        fill_between(minus.index.values, 0, minus.values, color="orange", alpha=0.75)
        fill_between(plus.index.values, 0, plus.values, color="blue", alpha=0.5)
        xlim(left, right)
        if scale:
            ylim(0, 100)
        else:
            ylim(ymin=0)
        # hide extra text and labels
        ax.grid(axis="x")
        ax.ticklabel_format(axis="x", style="sci", scilimits=(1, 3))
        if output:
            savefig(output, transparent=True)

    def find_amplifications_fromGff(self,gff_file,
                strand_start, strand_stop,
                experiment_id_I = None,
                sample_name_I = None,
                scale_factor=True, downsample_factor=0,
                reads_min=1.5,reads_max=5.0,
                indices_min=200,consecutive_tol=10):
        """find amplifications from the gff file
        INPUT:
        strand_start = index of the start position
        strand_stop = index of the stop position
        scale_factor = boolean, if true, reads will be normalized to have 100 max
        downsample_factor = integer, factor to downsample the points to
        reads_min = minimum number of reads to identify an amplification
        reads_max = maximum number of reads to identify an amplification
        indices_min : minimum number of points of a high coverage region
        consecutive_tol: maximum number of consecutive points that do not meet the coverage_min/max criteria that can be included a high coverage region

        OPTION INPUT:
        experiment_id_I = tag for the experiment from which the sample came
        sample_name_I = tag for the sample name
        
        """
        data_O=[];
        experiment_id = experiment_id_I;
        sn = sample_name_I;
        # get the data_dir
        # extract the strands
        plus,minus=self.extract_strandsFromGff(gff_file,strand_start, strand_stop, scale=scale_factor, downsample=downsample_factor)
        # find high coverage regions
        plus_high_region_indices,minus_high_region_indices,plus_high_regions, minus_high_regions = self.find_highCoverageRegions(plus,minus,coverage_min=reads_min,coverage_max=reads_max,points_min=indices_min,consecutive_tol=consecutive_tol);
        # record high coverage regions
        # + strand
        iter = 0;
        for index,reads in plus_high_regions.iteritems():
            if index > plus_high_region_indices[iter]['stop']:
                iter+=1;
            data_O.append({
            #'analysis_id':analysis_id,
            'experiment_id':experiment_id,
            'sample_name':sn,
            'genome_chromosome':1, #default
            'genome_strand':'+',
            'genome_index':int(index),
            'strand_start':strand_start,
            'strand_stop':strand_stop,
            'reads':float(reads),
            'reads_min':reads_min,
            'reads_max':reads_max,
            'indices_min':indices_min,
            'consecutive_tol':consecutive_tol,
            'scale_factor':scale_factor,
            'downsample_factor':downsample_factor,
            'amplification_start':int(plus_high_region_indices[iter]['start']),
            'amplification_stop':int(plus_high_region_indices[iter]['stop']),
            'used_':True,
            'comment_':None
                });
        # - strand
        iter = 0;
        for index,reads in minus_high_regions.iteritems():
            if index > minus_high_region_indices[iter]['stop']:
                iter+=1;
            data_O.append({
            #'analysis_id':analysis_id,
            'experiment_id':experiment_id,
            'sample_name':sn,
            'genome_chromosome':1, #default
            'genome_strand':'-',
            'genome_index':int(index),
            'strand_start':strand_start,
            'strand_stop':strand_stop,
            'reads':float(reads),
            'reads_min':reads_min,
            'reads_max':reads_max,
            'indices_min':indices_min,
            'consecutive_tol':consecutive_tol,
            'scale_factor':scale_factor,
            'downsample_factor':downsample_factor,
            'amplification_start':int(minus_high_region_indices[iter]['start']),
            'amplification_stop':int(minus_high_region_indices[iter]['stop']),
            'used_':True,
            'comment_':None
                });
        return data_O;

    def findAndCalculate_amplificationStats_fromGff(self,gff_file,
                strand_start, strand_stop,
                experiment_id_I = None,
                sample_name_I = None,
                scale_factor=True, downsample_factor=0,
                reads_min=1.5,reads_max=5.0,
                indices_min=200,consecutive_tol=10):
        """find amplifications from the gff file and calculate their statistics

        INPUT:
        strand_start = index of the start position
        strand_stop = index of the stop position
        scale_factor = boolean, if true, reads will be normalized to have 100 max
        downsample_factor = integer, factor to downsample the points to
        reads_min = minimum number of reads to identify an amplification
        reads_max = maximum number of reads to identify an amplification
        indices_min : minimum number of points of a high coverage region
        consecutive_tol: maximum number of consecutive points that do not meet the coverage_min/max criteria that can be included a high coverage region

        OPTION INPUT:
        experiment_id_I = tag for the experiment from which the sample came
        sample_name_I = tag for the sample name
        
        """
        data_O=[];
        stats_O=[];
        experiment_id = experiment_id_I;
        sn = sample_name_I;
        calculate = calculate_interface();
        # get the data_dir
        # extract the strands
        plus,minus = self.extract_strandsFromGff(gff_file,strand_start, strand_stop, scale=scale_factor, downsample=0)
        # find high coverage regions
        plus_high_region_indices,minus_high_region_indices,plus_high_regions, minus_high_regions = self.find_highCoverageRegions(plus,minus,coverage_min=reads_min,coverage_max=reads_max,points_min=indices_min,consecutive_tol=consecutive_tol);
        
        # record the means for later use
        plus_mean,minus_mean = plus.mean(),minus.mean();
        plus_min,minus_min = plus.min(),minus.min();
        plus_max,minus_max = plus.max(),minus.max();
        # calculate stats on the high coverage regions
        # + strand
        for row_cnt,row in enumerate(plus_high_region_indices):
            plus_region = plus_high_regions[(plus_high_regions.index>=row['start']) & (plus_high_regions.index<=row['stop'])]
            # calculate using scipy
            data_ave_O, data_var_O, data_lb_O, data_ub_O = None, None, None, None;
            data_ave_O, data_var_O, data_lb_O, data_ub_O = calculate.calculate_ave_var(plus_region.values,confidence_I = 0.95);
            # calculate the interquartile range
            min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
            min_O, max_O, median_O, iq_1_O, iq_3_O=calculate.calculate_interquartiles(plus_region.values);
            # record data
            stats_O.append({
                #'analysis_id':analysis_id,
                'experiment_id':experiment_id,
                'sample_name':sn,
                'genome_chromosome':1,
                'genome_strand':'plus',
                'strand_start':strand_start,
                'strand_stop':strand_stop,
                'reads_min':min_O,
                'reads_max':max_O,
                'reads_lb':data_lb_O,
                'reads_ub':data_ub_O,
                'reads_iq1':iq_1_O,
                'reads_iq3':iq_3_O,
                'reads_median':median_O,
                'reads_mean':data_ave_O,
                'reads_var':data_var_O,
                'reads_n':len(plus_region.values),
                'amplification_start':int(row['start']),
                'amplification_stop':int(row['stop']),
                'used_':True,
                'comment_':None
                })
            # downsample
            collapse_factor = None;
            if downsample_factor > 1:
                collapse_factor = int((row['stop'] - row['start']) / downsample_factor)
            if collapse_factor and collapse_factor > 1:
                plus_region = plus_region.groupby(lambda x: x // collapse_factor).mean()
                plus_region.index *= collapse_factor
            # add mean to index before and after the amplification start and stop, respectively (for visualization)
            if downsample_factor > 1 and row_cnt==0:
                #plus_region[strand_start]=plus_mean;
                #plus_region[strand_stop]=plus_mean;
                data_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id,
                    'sample_name':sn,
                    'genome_chromosome':1, #default
                    'genome_strand':'plus_mean',
                    #'genome_index':int(strand_start),
                    'genome_index':int(row['start']-1),
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads':plus_mean,
                    'reads_min':reads_min,
                    'reads_max':reads_max,
                    'indices_min':indices_min,
                    'consecutive_tol':consecutive_tol,
                    'scale_factor':scale_factor,
                    'downsample_factor':downsample_factor,
                    'amplification_start':strand_start,
                    'amplification_stop':strand_stop,
                    'used_':True,
                    'comment_':'mean reads of the plus strand'
                    });
            if downsample_factor > 1 and row_cnt==len(plus_high_region_indices)-1:
                data_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id,
                    'sample_name':sn,
                    'genome_chromosome':1, #default
                    'genome_strand':'plus_mean',
                    #'genome_index':int(strand_stop),
                    'genome_index':int(row['stop']+1),
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads':plus_mean,
                    'reads_min':reads_min,
                    'reads_max':reads_max,
                    'indices_min':indices_min,
                    'consecutive_tol':consecutive_tol,
                    'scale_factor':scale_factor,
                    'downsample_factor':downsample_factor,
                    'amplification_start':strand_start,
                    'amplification_stop':strand_stop,
                    'used_':True,
                    'comment_':'mean reads of the plus strand'
                    });
            ## add zeros to strand start and stop, respectively (for visualization)
            #if downsample_factor > 1:
            #    plus_region[row['start']-1]=plus_mean;
            #    plus_region[row['stop']+1]=plus_mean;
            # record high coverage regions
            for index,reads in plus_region.iteritems():
                data_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id,
                    'sample_name':sn,
                    'genome_chromosome':1, #default
                    'genome_strand':'plus',
                    'genome_index':int(index),
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads':float(reads),
                    'reads_min':reads_min,
                    'reads_max':reads_max,
                    'indices_min':indices_min,
                    'consecutive_tol':consecutive_tol,
                    'scale_factor':scale_factor,
                    'downsample_factor':downsample_factor,
                    'amplification_start':int(row['start']),
                    'amplification_stop':int(row['stop']),
                    'used_':True,
                    'comment_':None
                });
        # - strand
        for row_cnt,row in enumerate(minus_high_region_indices):
            minus_region = minus_high_regions[(minus_high_regions.index>=row['start']) & (minus_high_regions.index<=row['stop'])]
            # calculate using scipy
            data_ave_O, data_var_O, data_lb_O, data_ub_O = None, None, None, None;
            data_ave_O, data_var_O, data_lb_O, data_ub_O = calculate.calculate_ave_var(minus_region.values,confidence_I = 0.95);
            # calculate the interquartile range
            min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
            min_O, max_O, median_O, iq_1_O, iq_3_O=calculate.calculate_interquartiles(minus_region.values);
            # record data
            stats_O.append({
                #'analysis_id':analysis_id,
                'experiment_id':experiment_id,
                'sample_name':sn,
                'genome_chromosome':1,
                'genome_strand':'minus',
                'strand_start':strand_start,
                'strand_stop':strand_stop,
                'reads_min':min_O,
                'reads_max':max_O,
                'reads_lb':data_lb_O,
                'reads_ub':data_ub_O,
                'reads_iq1':iq_1_O,
                'reads_iq3':iq_3_O,
                'reads_median':median_O,
                'reads_mean':data_ave_O,
                'reads_var':data_var_O,
                'reads_n':len(minus_region.values),
                'amplification_start':int(row['start']),
                'amplification_stop':int(row['stop']),
                'used_':True,
                'comment_':None
                })
            # downsample
            collapse_factor = None;
            if downsample_factor > 1:
                collapse_factor = int((row['stop'] - row['start']) / downsample_factor)
            if collapse_factor and collapse_factor > 1:
                minus_region = minus_region.groupby(lambda x: x // collapse_factor).mean()
                minus_region.index *= collapse_factor
            # add mean to index before and after the amplification start and stop, respectively (for visualization)
            if downsample_factor > 1 and row_cnt==0:
                #minus_region[strand_start]=minus_mean;
                #minus_region[strand_stop]=minus_mean;
                data_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id,
                    'sample_name':sn,
                    'genome_chromosome':1, #default
                    'genome_strand':'minus_mean',
                    #'genome_index':int(strand_start),
                    'genome_index':int(row['start']-1),
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads':minus_mean,
                    'reads_min':reads_min,
                    'reads_max':reads_max,
                    'indices_min':indices_min,
                    'consecutive_tol':consecutive_tol,
                    'scale_factor':scale_factor,
                    'downsample_factor':downsample_factor,
                    'amplification_start':strand_start,
                    'amplification_stop':strand_stop,
                    'used_':True,
                    'comment_':'mean reads of the minus strand'
                    });
            if downsample_factor > 1 and row_cnt==len(minus_high_region_indices)-1:
                data_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id,
                    'sample_name':sn,
                    'genome_chromosome':1, #default
                    'genome_strand':'minus_mean',
                    #'genome_index':int(strand_stop),
                    'genome_index':int(row['stop']+1),
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads':minus_mean,
                    'reads_min':reads_min,
                    'reads_max':reads_max,
                    'indices_min':indices_min,
                    'consecutive_tol':consecutive_tol,
                    'scale_factor':scale_factor,
                    'downsample_factor':downsample_factor,
                    'amplification_start':strand_start,
                    'amplification_stop':strand_stop,
                    'used_':True,
                    'comment_':'mean reads of the minus strand'
                    });
            ## add zeros to strand start and stop, respectively (for visualization)
            #if downsample_factor > 1:
            #    minus_region[row['start']-1]=minus_mean;
            #    minus_region[row['stop']+1]=minus_mean;
            # record high coverage regions
            for index,reads in minus_region.iteritems():
                data_O.append({
                    #'analysis_id':analysis_id,
                    'experiment_id':experiment_id,
                    'sample_name':sn,
                    'genome_chromosome':1, #default
                    'genome_strand':'minus',
                    'genome_index':int(index),
                    'strand_start':strand_start,
                    'strand_stop':strand_stop,
                    'reads':float(reads),
                    'reads_min':reads_min,
                    'reads_max':reads_max,
                    'indices_min':indices_min,
                    'consecutive_tol':consecutive_tol,
                    'scale_factor':scale_factor,
                    'downsample_factor':downsample_factor,
                    'amplification_start':int(row['start']),
                    'amplification_stop':int(row['stop']),
                    'used_':True,
                    'comment_':None});
        #record the data
        return data_O, stats_O;

    def extract_coverage_fromGff(self,gff_file, 
         strand_start,strand_stop,scale_factor=True,downsample_factor=2000,
         experiment_id_I=None, sample_name_I=None):
        """extract coverage (genome position and reads) from .gff
        INPUT:
        strand_start = index of the start position
        strand_stop = index of the stop position
        scale_factor = boolean, if true, reads will be normalized to have 100 max
        downsample_factor = integer, factor to downsample the points to
     
        OPTION INPUT:
        experiment_id_I = tag for the experiment from which the sample came
        sample_name_I = tag for the sample name
        
        """
        filename = gff_file;
        experiment_id = experiment_id_I;
        sample_name = sample_name_I;
        # parse the gff file into pandas dataframes
        plus,minus = self.extract_strandsFromGff(gff_file,strand_start, strand_stop, scale=scale_factor, downsample=downsample_factor)
        # split into seperate data structures based on the destined table add
        coverage_data = [];
        if not plus.empty:
            for index,reads in plus.iteritems():
                coverage_data.append({
                                #'analysis_id':analysis_id,
                                'experiment_id':experiment_id,
                                'sample_name':sample_name,
                                'data_dir':filename,
                                'genome_chromosome':1, #default
                                'genome_strand':'plus',
                                'genome_index':int(index),
                                'strand_start':strand_start,
                                'strand_stop':strand_stop,
                                'reads':float(reads),
                                'scale_factor':scale_factor,
                                'downsample_factor':downsample_factor,
                                'used_':True,
                                'comment_':None});
        if not minus.empty:
            for index,reads in minus.iteritems():
                coverage_data.append({
                                #'analysis_id':analysis_id,
                                'experiment_id':experiment_id,
                                'sample_name':sample_name,
                                'data_dir':filename,
                                'genome_chromosome':1, #default
                                'genome_strand':'minus',
                                'genome_index':int(index),
                                'strand_start':strand_start,
                                'strand_stop':strand_stop,
                                'reads':float(reads),
                                'scale_factor':scale_factor,
                                'downsample_factor':downsample_factor,
                                'used_':True,
                                'comment_':None});
        # add data to the database:
        return coverage_data;

    def calculate_coverageStats_fromGff(self,gff_file, 
         strand_start,strand_stop,scale_factor=True,downsample_factor=2000,
         experiment_id_I=None, sample_name_I=None):
        """extract coverage (genome position and reads) from .gff
        INPUT:
        strand_start = index of the start position
        strand_stop = index of the stop position
        scale_factor = boolean, if true, reads will be normalized to have 100 max
        downsample_factor = integer, factor to downsample the points to
     
        OPTION INPUT:
        experiment_id_I = tag for the experiment from which the sample came
        sample_name_I = tag for the sample name
        
        """
        calculate = calculate_interface();

        experiment_id = experiment_id_I;
        sn = sample_name_I;
        # parse the gff file into pandas dataframes
        plus,minus = self.extract_strandsFromGff(gff_file,strand_start, strand_stop, scale=scale_factor, downsample=downsample_factor)
        # split into seperate data structures based on the destined table add
        coverageStats_data = [];
        # plus strand
        # calculate using scipy
        data_ave_O, data_var_O, data_lb_O, data_ub_O = None, None, None, None;
        data_ave_O, data_var_O, data_lb_O, data_ub_O = calculate.calculate_ave_var(plus.values,confidence_I = 0.95);
        # calculate the interquartile range
        min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
        min_O, max_O, median_O, iq_1_O, iq_3_O=calculate.calculate_interquartiles(plus.values);
        # record data
        coverageStats_data.append({
            #'analysis_id':analysis_id,
            'experiment_id':experiment_id,
            'sample_name':sn,
            'genome_chromosome':1,
            'genome_strand':'plus',
            'strand_start':strand_start,
            'strand_stop':strand_stop,
            'reads_min':int(min_O),
            'reads_max':int(max_O),
            'reads_lb':data_lb_O,
            'reads_ub':data_ub_O,
            'reads_iq1':iq_1_O,
            'reads_iq3':iq_3_O,
            'reads_median':median_O,
            'reads_mean':data_ave_O,
            'reads_var':data_var_O,
            'reads_n':len(plus.values),
            'used_':True,
            'comment_':None});
        # minus strand
        # calculate using scipy
        data_ave_O, data_var_O, data_lb_O, data_ub_O = None, None, None, None;
        data_ave_O, data_var_O, data_lb_O, data_ub_O = calculate.calculate_ave_var(minus.values,confidence_I = 0.95);
        # calculate the interquartile range
        min_O, max_O, median_O, iq_1_O, iq_3_O = None, None, None, None, None;
        min_O, max_O, median_O, iq_1_O, iq_3_O=calculate.calculate_interquartiles(minus.values);
        # record data
        coverageStats_data.append({
            #'analysis_id':analysis_id,
            'experiment_id':experiment_id,
            'sample_name':sn,
            'genome_chromosome':1,
            'genome_strand':'minus',
            'strand_start':strand_start,
            'strand_stop':strand_stop,
            'reads_min':int(min_O),
            'reads_max':int(max_O),
            'reads_lb':data_lb_O,
            'reads_ub':data_ub_O,
            'reads_iq1':iq_1_O,
            'reads_iq3':iq_3_O,
            'reads_median':median_O,
            'reads_mean':data_ave_O,
            'reads_var':data_var_O,
            'reads_n':len(minus.values),
            'used_':True,
            'comment_':None});
        # record the data
        return coverageStats_data;