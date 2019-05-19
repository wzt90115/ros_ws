#!/usr/bin/env python

import rospy
import os
import cv2
import numpy as np
from tqdm import tqdm
from glob import glob
from natsort import natsorted

if __name__ == '__main__':
    rospy.init_node("tovideo", anonymous = False)
    if not rospy.has_param('source_dir'):
        source_dir = '/home/wangzt/ros_ws/src/ft/video'
        rospy.set_param('source_dir', source_dir)

    rospy.spin()
    # output_folder = os.path.join(path_to_folder_with_images, 'video')
    # print output_folder
    # if not os.path.isdir(output_folder):
    #     os.mkdir(output_folder)
    # output_file = os.path.join(output_folder, 'output.avi')
    # images_paths = natsorted([path for path in glob(os.path.join(path_to_folder_with_images, '*')) if 'jpg' in  path])
    # image_test = cv2.imread(images_paths[0], 0)
    # image_shape = image_test.T.shape
    # print(image_shape)

    # # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'DVIX')
    # out = cv2.VideoWriter(output_file, fourcc, 60.0, image_shape,0)

    # for image_path in tqdm(images_paths, desc='saving video'):
    #     frame = cv2.imread(image_path)
    #     gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     out.write(gray_image)

    #     # cv2.imshow('frame',frame)
    #     # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     #     break

    # # Release everything if job is finished
    # out.release()
    # cv2.destroyAllWindows()
