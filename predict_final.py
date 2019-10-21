# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:04:03 2019

@author: ABARNA DEVI

"""
from pylab import *
import matplotlib.pyplot as plt
from segmentation import convert
from getborders import borders
from predict_diseases import predict
import cv2
class final:
    def disease(image):
        img = cv2.imread(image)
        segmented,binary_mask = convert.morphological_transformation(image)
        edges = borders.get_borders(binary_mask)
        disease_detected = predict.predict_disease(segmented)
        img_list = []
        img_list.append(img)
        img_list.append(binary_mask)
        img_list.append(edges)
        img_list.append(segmented)
        return (disease_detected)