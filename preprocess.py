
# importing all the libraries 
#also importing the files and labels for human 3.6  from data folder
import os
import sys
import argparse
import csv
import numpy as np
import h5py
from data.utils import *
from data.format.human36m.body import BodyFileReader, get_labels


# A class to split the training data S1-S11 and generate a CSV file
class Data_split_human36(object):
    def __init__(self, input_folder):

    #Here, the input_folder contains the path of the folder where all the clips are stored
        self._input_folder_human36 = input_folder
        self._items = []
        self._stats_context = DataStatisticsContext() # it is a class which gives the pointer to the data statistics


# A function to load all the files as a python list including the labesls as well

    def load_data_human36(self):
        
        labels = get_labels() # to obtain the labels
        sub_folders = os.listdir(self._input_folder)
        index = 0
        self._items.clear() # for clear screen
        for folder in sub_folders:
            folder_path = os.path.join(self._input_folder, folder) # associating the subfolders to the folders 
            if not os.path.isdir(folder_path):
                continue
            
            subject_id = int(folder[1:])
            files = os.listdir(folder_path)
            for item in files:
                item_path = os.path.join(folder_path, item)
                if not os.path.isfile(item_path):
                    continue
                
                # Get the filename without extension and remove anything after the space
                filename = os.path.splitext(item)[0].split()[0]
                if self._filter_data(item_path):
                    self._items.append([os.path.abspath(item_path), labels[filename.lower()], subject_id])

                if (index % 100) == 0:
                    print("Process {} items.".format(index+1))
                index += 1
        return self._items

# A boolean function to add item frames

    def filter_human36(self, item_path):
       
               frames = BodyFileReader(item_path)
        if len(frames) >= 60:
            for frame in frames:
                if len(frame) == 0:
                    return False
            return True
        return False

    

#splitting the data into training and testing data
#here, items is collection of clips and their label

    def split_data_human36(self, items):
        
        item_count = len(items)
        indices = np.arange(item_count) #create a numpy array with the lengh = the no. of items
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

    

    def write_csv_human36(self, items, file_path):
        
        if sys.version_info[0] < 3:
            with open(file_path, 'wb') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for item in items:
                    writer.writerow(item)
        else:
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for item in items:
                    writer.writerow(item)
    

    def compute_statistics_human36(self):
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
   
    data_human36 = data_split_human36(input_folder)
    items_human36 = data_split_human36.load_data_human36()
    print("{} items loaded for human 3.6 dataset".format(train_human36, test_human36 = data_split_human36.split_data(items)
    
    context_human36 = data_split_human36.compute_statistics_human36()
    #print("Complete computing statistics.")
    if len(train) > 0:
        data_split_human36.write_csv_human36(train, os.path.join(output_folder, 'train_human36.csv'))
        data_split_ntu.write_csv_ntu(train, os.path.join(output_folder, 'train_ntu.csv'))
    if len(test) > 0:
        data_split_human36.write_to_csv(test, os.path.join(output_folder, 'test_map.csv'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i",
                        "--input_folder",
                        type = str,
                        help = "Input folder",
                        required = True)

    parser.add_argument("-o",
                        "--output_folder",
                        type = str,
                        help = "Output folder",
                        required = True)

    args = parser.parse_args()
    main(args.input_folder, args.output_folder)


    
