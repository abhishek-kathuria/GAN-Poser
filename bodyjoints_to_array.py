import sys
import csv
import numpy as np

class SequenceBodyReader(object):
  
    def __init__(self, map_file, sequence_length, dataset, skip_frame=0, 
                 data_preprocessing=None, random_sequence=False, label_count=None, 
                 in_memory=True, camera_data_file=None, is_training=True,
                 seed=None):
        
        self._source = SourceFactory(dataset, camera_data_file)
        self._map_file = map_file
        self._label_count = label_count
        self._sequence_length = sequence_length
        self._data_preprocessing = data_preprocessing
        self._files = []
        self._in_memory = in_memory
        self._files.clear()
        self._sensor = self._source.create_sensor() 
        self._body = self._source.create_body()
        self._feature_shape = (self._body.joint_count, 3)
        with open(map_file) as csv_file:
            data = csv.reader(csv_file)
            for row in data:
                filename_or_object = self._source.create_file_reader(row[0]) \
                                     if self._in_memory else row[0]
                self._files.append([filename_or_object, int(row[1]), int(row[2])])
                if (self._label_count is not None) and (len(row) > 1):
                    target = [0.0] * self._label_count
                    target[int(row[1])] = 1.0
                    self._targets.append(target)
        if is_training:
            if seed != None:
                np.random.seed(seed)
            np.random.shuffle(self._indices)

    def size(self):
        return len(self._files)

    def next_minibatch(self, batch_size):
        batch_end = min(self._batch_start + batch_size, self.size())
        current_batch_size = batch_end - self._batch_start
        if current_batch_size < 0:
            raise Exception('end ')
        inputs = np.empty(shape=(current_batch_size, self._sequence_length) + self._feature_shape, dtype=np.float32)
        activities = np.zeros(shape=(current_batch_size), dtype=np.int32)
        subjects = np.zeros(shape=(current_batch_size), dtype=np.int32)
        targets = None
        if self._label_count is not None:
            targets = np.empty(shape=(current_batch_size, self._label_count), dtype=np.float32)

        for idx in range(self._batch_start, batch_end):
            index = self._indices[idx]
            frames = self._files[index][0] if self._in_memory else self._source.create_file_reader(self._files[index][0])

            inputs[idx - self._batch_start, :, :, :] = self._select_frames(frames)
            activities[idx - self._batch_start] = self._files[index][1]
            subjects[idx - self._batch_start] = self._files[index][2]

            if self._label_count is not None:
                targets[idx - self._batch_start, :] = self._targets[index]

        self._batch_start += current_batch_size
        return inputs, targets, current_batch_size, activities, subjects

    def _select_frames(self, frames):
        num_frames = len(frames)
        multiplier = self._skip_frame + 1

        if not self._random_sequence:
            features = []
            if num_frames >= multiplier * self._sequence_length:
                start_frame = int(num_frames / 2 - (multiplier * self._sequence_length) / 2)
                for index in range(multiplier * self._sequence_length):
                    if (index % multiplier) == 0:
                        features.append(self._from_body_to_feature(frames[start_frame + index]))
            else:
                raise ValueError("Clip is too small, it has {} frames only.".format(num_frames))

            return np.stack(features, axis=0)
        else:
            features = []
            if num_frames >= multiplier * self._sequence_length:
                for index in range(multiplier * self._sequence_length):
                    if (index % multiplier) == 0:
                        features.append(self._from_body_to_feature(frames[start + index]))
            else:
                raise ValueError("Clip is too small, it has {} frames only.".format(num_frames))

            return np.stack(features, axis=0)

    def _from_body_to_feature(self, frame):
        if len(frame) > 0:
            body = frame[0]
            return self._data_preprocessing.normalize(body.as_numpy())
        return None