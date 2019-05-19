#!/usr/bin/env python

import rospy
import os
import cv2


def param_set():

    if rospy.has_param('~source_dir'):
        source_dir = rospy.get_param('~source_dir')
    else:
        rospy.logerr("no source_dir")
        exit()

    if rospy.has_param('~video_name'):
        video_name = rospy.get_param('~video_name')
        video_path = os.path.join(source_dir, 'video')
        video_path = os.path.join(video_path, video_name)
        if not os.path.isfile(video_path):
            rospy.logerr("dir")
            exit()

    rospy.loginfo(video_path)
    cap = cv2.VideoCapture(video_path)
    rospy.set_param('video_info/path',video_path)
    rospy.set_param('video_info/width',int(cap.get(3)))
    rospy.set_param('video_info/height',int(cap.get(4)))
    rospy.set_param('video_info/fps',int(cap.get(5)))
    rospy.set_param('video_info/frames',int(cap.get(7)))
    cap.release()


if __name__ == '__main__':
 
    rospy.init_node("data_reading", anonymous = False)
    param_set()
