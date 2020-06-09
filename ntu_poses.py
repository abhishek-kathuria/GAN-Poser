import sys

from ..kinect_v2 import Body, Joint

class BodyFileReader(object):
    
    def __init__(self, file_path):
        self.frames = self._read(file_path)

    def __len__(self):
        return len(self.frames)

    def __iter__(self):
 
        for frame in self.frames:
            yield frame

    def __getitem__(self, key):
        return self.frames[key]

    def _read(self, path):
        frames = []
        with open(path, "r") as f:
            line_index = 0
            lines = f.read().splitlines()
            frame_count = int(lines[line_index]); line_index += 1
            for _ in range(frame_count):
                body_count = int(lines[line_index]); line_index += 1
                body_frame = []
                for _ in range(body_count):
                    body_info = lines[line_index].split(" "); line_index += 1
                    body = Body(int(body_info[0]))
                    body.cliped_edges = int(body_info[1])
                    body.hand_left_confidence = int(body_info[2])
                    body.hand_left_state = int(body_info[3])
                    body.hand_right_confidence = int(body_info[4])
                    body.hand_right_state = int(body_info[5])
                    body.restricted = int(body_info[6])
                    body.lean_x = float(body_info[7])
                    body.lean_y = float(body_info[8])
                    body.tracking_state = int(body_info[9])
                    joint_count = int(lines[line_index]); line_index += 1
                    joints = []
                    for _ in range(joint_count):
                        joint_info = lines[line_index].split(" "); line_index += 1

                        joint = Joint()

                        # 3D location of the joint
                        joint.x = float(joint_info[0])
                        joint.y = float(joint_info[1])
                        joint.z = float(joint_info[2])

                        joint.depth_x = float(joint_info[3])
                        joint.depth_y = float(joint_info[4])

                        joint.color_x = float(joint_info[5])
                        joint.color_y = float(joint_info[6])

                        # The orientation of the joint
                        joint.orientation_w = float(joint_info[7])
                        joint.orientation_x = float(joint_info[8])
                        joint.orientation_y = float(joint_info[9])
                        joint.orientation_z = float(joint_info[10])

                        # The tracking state of the joint
                        joint.tracking_state = int(joint_info[11])
                        joints.append(joint)
                    body.add_joints(joints)
                    body_frame.append(body)
                frames.append(body_frame)
        return frames