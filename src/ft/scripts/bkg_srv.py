#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from ft.srv import *


def roi_set(param):
    
    rospy.loginfo('roi setting') 
    cv2.setMouseCallback('src', on_mouse)
    cap = cv2.VideoCapture(param['path'])
    cap.set(1,50)
    ret, framedata = cap.read()
    if ret:
        gray = cv2.cvtColor(framedata, cv2.COLOR_BGR2GRAY)
        cv2.imshow('image',gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # pass

def median(param,roi=False):
  
    if roi:
        roi = roi_set(param)

    frameInds = range(10,param['frames'], 100)
    rospy.loginfo('calculate meidan of %i frames' %len(frameInds))

    cap = cv2.VideoCapture(param['path'])
    for ind in frameInds:
        cap.set(1,ind)
        ret, frameBkg = cap.read()
        if ret:
            gray = cv2.cvtColor(frameBkg, cv2.COLOR_BGR2GRAY)
            if ind == 10:
                bkg = gray
            else:
                bkg = np.append(bkg,gray,axis = 0)

    bkg = bkg.reshape((len(frameInds),param['height'],param['width']))
    bkg_median = np.median(bkg,axis = 0)
    bkg_median = np.true_divide(bkg_median, 255)

    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.imshow('image',bkg_median.astype('float32'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return bkg_median.astype('float32')

def handle_bkg(req=0):

    if not rospy.has_param('video_info'):
        rospy.logerr('no video_info')
        return False

    vi = rospy.get_param('video_info')
    if req == 0:
        median(vi)
        return True
    if req.index == 0:
        median(vi,req.roi)
        return True
    return True


if __name__ == '__main__':

    rospy.init_node("bkg", anonymous = False)
    s = rospy.Service('bkg', BkgRequest, handle_bkg)
    handle_bkg()
    rospy.spin()


