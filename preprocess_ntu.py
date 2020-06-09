#import files for ntuRGBD-D dataset

import os
import sys
import argparse
import csv
import numpy as np
import h5py
from data.utils import *
from data.format.nturgbd.body import BodyFileReader


#class for splitting data for the ntu dataset
class Data_split_ntu(object):
    def __init__(self, input_folder):      
        self._input_folder_ntu = input_folder
        self._items = []
        self._stats_context = DataStatisticsContext()

    def load_data_ntu(self):
        files = os.listdir(self._input_folder)
        index = 0
        self._items.clear()
        for item in files:
            item_path = os.path.join(self._input_folder, item)
            if not os.path.isfile(item_path):
                continue
            settings = self._parse_filename(item)            
            if self._filter_data(item_path, settings):
                subject_id = settings[2]
                activity_id = settings[4]
                self._items.append([os.path.abspath(item_path), activity_id, subject_id])

            if (index % 100) == 0:
                print("Process {} items.".format(index+1))
            index += 1
        return self._items

        #now, the file names for the ntu dataset are in different format. So this function corrects it.
    def correct_filename_ntu(self, filename):
        #the regular expression library is used to correect filenames
        import re
        name = os.path.splitext(filename)[0].split()[0]
        result = list(filter(None, re.split('[a-z]+', name, flags=re.IGNORECASE)))
        return list(map(int, result))

    def filter_ntu(self, item_path, settings):
        camera_id = settings[1]        
        replication_id = settings[3]
        activity_id = settings[4]
        if (activity_id > 49) or (replication_id != 1):
            return False 
        frames = BodyFileReader(item_path)
        if len(frames) >= 60:
            for frame in frames:
                if len(frame) == 0:
                    return False
            return True
        return False

    def split_data_ntu(self, items):
        item_count = len(items)
        indices = np.arange(item_count)
        np.random.shuffle(indices)
        train_count = int(0.8 * item_count)
        test_count  = item_count - train_count
        train = []
        test  = []
        for i in range(train_count):
            train.append(items[indices[i]])
        for i in range(train_count, train_count + test_count):
            test.append(items[indices[i]])
        return train, test


    def write_csv_ntu(self, items, file_path):
        if sys.version_info[0] < 3:
            with open(file_path, 'wb') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for item in items:
                    writer.writerow(item)
        else:
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for item in items:
                    writer.writerow(item

	def compute_statistics_ntu(self):
	        with BodyDataStatisticsPass1(self._stats_context) as stats:
	            for item in self._items:
	                frames = BodyFileReader(item[0])
	                for frame in frames:
	                    stats.add(frame[0].as_numpy())
	        with BodyDataStatisticsPass2(self._stats_context) as stats:
	            for item in self._items:
	                frames = BodyFileReader(item[0])
	                for frame in frames:
	                    stats.add(frame[0].as_numpy())
	        return self._stats_context


def main(input_folder, output_folder):
# it iterates over the given list of clips and labels, then converts them to train and test data
	data_ntu = data_split_ntu(input_folder)
    items_ntu = data_split_ntu.load_data_ntu()
    print("{} items loaded for NTURGB-D dataset".format(len(items))
    
    #trin and test data for ntu
    train_ntu, test_ntu = data_split_ntu.split_data(items)
    context_ntu = data_split_ntu.compute_statistics_ntu()

#check the conditions and make the csv file based on that 
    if len(train_ntu) > 0:
        data_split_ntu.write_to_csv(train_ntu, os.path.join(output_folder, 'train_ntu.csv'))
    if len(test_ntu) > 0:
        data_split_ntu.write_to_csv(test_ntu, os.path.join(output_folder, 'test_ntu.csv'))

 	if __name__ == "__main__":
    parser_ntu = argparse.ArgumentParser()
    parser_ntu.add_argument("-i",
                        "--input_folder",
                        type = str,
                        help = "Input folder ",
                        required = True)

    parser_ntu.add_argument("-o",
                        "--output_folder",
                        type = str,
                        help = "Output folder for the generated training and test text files.",
                        required = True)

    args = parser_ntu.parse_args()
    main(args.input_folder, args.output_folder)