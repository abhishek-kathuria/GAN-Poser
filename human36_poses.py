import sys
import os.path
import numpy as np
import h5py

def get_labels():
    return {"directions":1,
            "discussion":2,
            "eating":3,
            "greeting":4,
            "phoning":5,
            "photo":6,
            "posing":7,
            "purchases":8,
            "sitting":9,
            "sittingdown":10,
            "smoking":11,
            "waiting":12,
            "walkdog":13,
            "walking":14,
            "walktogether":15}

class BodyFileReader(object):
  
    def __init__(self, file_path):
        self._file_path = file_path
        self._frames = self._read(file_path)

    def __len__(self):
        return len(self._frames)

    def __iter__(self):
        for frame in self._frames:
            yield frame

    def __getitem__(self, key):
        return self._frames[key]

    def _read(self, path):
        frames = []
        if os.path.splitext(path)[1] == '.h5':
            with h5py.File(path, 'r') as h5f:
                poses = h5f['3D_positions'][:].T
                for i in range(poses.shape[0]):
                    body = Body()
                    joints = poses[i]
                    joint_count = joints.shape[0]//3
                    joints = np.reshape(joints, (joint_count, 3))
                    body.add_joints(joints)
                    body_frame = [body]
                    frames.append(body_frame)
        else:
            raise Exception('Unsupported file.')
        return frames