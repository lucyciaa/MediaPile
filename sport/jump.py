# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:10:44 2021

@author: Youmu
"""
# 导入opencv工具包
import cv2
# 导入numpy
# 导入姿势识别器
from count.mediapip import PoseDetector



def ropeSkipping(detectVideo):
    # 打开视频文件
    cap = cv2.VideoCapture(detectVideo)
    # 姿势识别器
    detector = PoseDetector()
    
    leftHip = []
    rightHip = []
    
    count = 0
    
    # begin_time = time.time()
    while True:
        # 读取摄像头，img为每帧图片
        success, img = cap.read()
        if success:
            h, w, c = img.shape
            # 识别姿势
            img = detector.find_pose(img, draw=True)
            # 获取姿势数据
            positions = detector.find_positions(img)
            
            if positions:
                #获取双髋位置数据
                leftHip.append(positions[23][2])
                rightHip.append(positions[24][2])
        else:
            break
    
    # 关闭摄像头
    cap.release()
    # 关闭程序窗口
    cv2.destroyAllWindows()
    
    #处理数据
    # print(len(rightHip))
    if len(rightHip) > 3 and len(leftHip) > 3:
        minLeftHip, maxLeftHip = min(leftHip), max(leftHip)
        minRightHip, maxRightHip = min(rightHip), max(rightHip)
        averageLeftHip = sum(leftHip)/len(leftHip)
        averageRightHip = sum(rightHip)/len(rightHip)
        baseleftHip = (minLeftHip+maxLeftHip)/2
        baserightHip = (minRightHip+maxRightHip)/2
    
        for i in range(1, len(leftHip)-1):
            if (leftHip[i] > leftHip[i-1] and leftHip[i] > leftHip[i+1]) and (rightHip[i] > rightHip[i-1] and rightHip[i] > rightHip[i+1]):
                if leftHip[i] > averageLeftHip and rightHip[i] > averageRightHip:
                    count += 1
    
        # print(count)
        return count
    else:
        count = 0
        return count
