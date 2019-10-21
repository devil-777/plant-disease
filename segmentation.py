# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:03:17 2019

@author: ABARNA DEVI
"""

import cv2
import numpy as np

class convert:    
    def morphological_transformation(image_path):
        
        img = cv2.imread(image_path,1)    
        segmented = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        
        kernel = np.ones((5,5),np.float32)/25
        img = cv2.filter2D(img,-1,kernel)        
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sat = hsv[:,:,1]        
        median = cv2.medianBlur(sat,5)
        kernel1 = np.ones((5,5),np.float32)/25
        kernel2 = np.array([[-1,-1,-1], [-1,11,-1], [-1,-1,-1]])         
        blur = cv2.GaussianBlur(median,(5,5),0)        
        ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        dst = cv2.filter2D(th3,-1, kernel1)
        im = cv2.filter2D(dst, -1, kernel2)        
        binary_mask = np.array(im,dtype='bool') 
        binary = np.array(binary_mask,dtype = 'uint8')
        kernel = np.ones((5,5),np.uint8)
        binary_mask= cv2.dilate(binary,kernel,iterations = 1)
        segmented[:,:,0] = np.multiply(segmented[:,:,0],binary_mask)
        segmented[:,:,1] = np.multiply(segmented[:,:,1],binary_mask)
        segmented[:,:,2] = np.multiply(segmented[:,:,2],binary_mask)
        return segmented,binary_mask
