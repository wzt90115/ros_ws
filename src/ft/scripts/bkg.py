#!/usr/bin/env python

import rospy
import os
import cv2
import numpy as np
from ft.srv import *


def median():
    pass
    # param = rospy.get_param('video_info')
    # # bkg = np.zeros((param['height'],param['width']))
    # # print bkg.shape
    # cap = cv2.VideoCapture(param['path'])
    # frameInds = range(100,600, 100)
    # # print len(frameInds)
    # for ind in frameInds:
    #     print ind
    #     cap.set(1,ind)
    #     ret, frameBkg = cap.read()
    #     if ret:
    #         gray = cv2.cvtColor(frameBkg, cv2.COLOR_BGR2GRAY)
    #         # cv2.imshow('image',gray)
    #         # cv2.waitKey(0)
    #         # cv2.destroyAllWindows()
    #         if ind == 100:
    #             bkg = gray

    #         else:
    #             bkg = np.append(bkg,gray,axis = 0)
    #         # print bkg.shape
    # bkg = bkg.reshape((len(frameInds),param['height'],param['width']))
    # print bkg[:,0,1]
    # bkg2 = np.median(bkg,axis = 0)
    # print bkg2.shape
    # # print bkg2.shape
    # bkg2 = np.true_divide(bkg2, 255)
    # cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    # cv2.imshow('image',bkg2.astype('float32'))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # return bkg2.astype('float32')

def handle_bkg(req):
    pass
    return True


if __name__ == '__main__':
    rospy.init_node("bkg", anonymous = False)
    if not rospy.has_param('video_info'):
        rospy.logerr('no video_info')
        exit()
    s = rospy.Service('bkg', BkgRequest, handle_bkg)
    rospy.spin()


