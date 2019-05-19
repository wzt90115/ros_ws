#!/usr/bin/env python

import rospy
import os
import cv2
import numpy as np
from ft.srv import *

title_window = 'Linear Blend'
bkg1 = None

def bkg():
    param = rospy.get_param('video_info')
    # bkg = np.zeros((param['height'],param['width']))
    # print bkg.shape
    cap = cv2.VideoCapture(param['path'])
    frameInds = range(100,600, 100)
    # print len(frameInds)
    for ind in frameInds:
        print ind
        cap.set(1,ind)
        ret, frameBkg = cap.read()
        if ret:
            gray = cv2.cvtColor(frameBkg, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('image',gray)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if ind == 100:
                bkg = gray

            else:
                bkg = np.append(bkg,gray,axis = 0)
            # print bkg.shape
    bkg = bkg.reshape((len(frameInds),param['height'],param['width']))
    print bkg[:,0,1]
    bkg2 = np.median(bkg,axis = 0)
    print bkg2.shape
    # print bkg2.shape
    bkg2 = np.true_divide(bkg2, 255)
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.imshow('image',bkg2.astype('float32'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return bkg2.astype('float32')

def getframe(req):
    bkg1 = bkg()
    param = rospy.get_param('video_info')
    cap = cv2.VideoCapture(param['path'])
    cap.set(1,req.index)
    ret, frame = cap.read()
    cap.release()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('raw.png',frame)
    # frmae = np.true_divide(frame, 255)
    frame = frame.astype('float32')
    frame = frame/255
    print frame.dtype, bkg1.dtype
    frame = cv2.absdiff(bkg1,frame)
    frame = frame * 255
    frame = frame.astype('int8') 
    # cv2.imwrite('bkg.png',frame)

    # cv2.imshow('result',frame)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()
    return True

def getframe1(req):
    # if not vars().has_key('bkg1'):
    #     print 'dddd'
    #     bkg1 = bkg()
    param = rospy.get_param('video_info')
    cap = cv2.VideoCapture(param['path'])
    cap.set(1,req)
    ret, frame = cap.read()
    cap.release()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('raw.png',frame)
    # frmae = np.true_divide(frame, 255)
    frame = frame.astype('float32')
    frame = frame/255
    print frame.dtype, bkg1.dtype
    frame = cv2.absdiff(bkg1,frame)
    frame = frame * 255
    frame = frame.astype('int8') 
    return frame
    # cv2.imshow('result',frame)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()
    # return True

def param_set():
    if rospy.has_param('video_info'):
        rospy.delete_param('video_info')
    source_dir = '/home/wangzt/ros_ws/src/ft'
    rospy.set_param('video_info/source_dir',source_dir)  
    video_path = os.path.join(source_dir, 'video/Video_1.avi')
    rospy.set_param('video_info/path',video_path)
    cap = cv2.VideoCapture(video_path)    
    rospy.set_param('video_info/width',int(cap.get(3)))
    rospy.set_param('video_info/height',int(cap.get(4)))
    rospy.set_param('video_info/frames',int(cap.get(7)))
    cap.release()
    # cap.set(1,18)
    # ret, frame = cap.read()
    # cv2.imshow('image',frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def frame_request_server():
    s = rospy.Service('frame_request', FrameRequest, getframe)
    print "Ready to add two ints."
    rospy.spin()

def on_trackbar(val):
    cv2.imshow(title_window, getframe1(val))

if __name__ == '__main__':


    np.set_printoptions(threshold=np.nan)
    rospy.init_node("vidoe_preprocessing", anonymous = False)
    param_set()
    bkg1 = bkg()
    cv2.namedWindow(title_window)
    trackbar_name = 'index'
    cv2.createTrackbar(trackbar_name, title_window , 1, int(rospy.get_param('video_info/frames')), on_trackbar)
    on_trackbar(0)
    while True:
        k = cv2.waitKey() & 0xFF
        if k == ord('s'):
            v = 1 + cv2.getTrackbarPos(trackbar_name, title_window)
            cv2.setTrackbarPos(trackbar_name, title_window, v) 
            on_trackbar(v)
        if k == ord('q'):
            break

    # cap.set(1,18)
    # ret, frame = cap.read()
    # cv2.imshow('image',frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # rospy.spin()
