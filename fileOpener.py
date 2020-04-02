#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:29:57 2020

@author: jeffreyscruggs
"""

#import libraries
import cv2
import glob
#Set Library Directory
path = '/Users/jeffreyscruggs/Desktop/IphonePhotos/Year 1/*.*'
#Cycle through directory
for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    print(a)
    #c = cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
    cv2.imshow('Color Image', a)
    
    #Wait a 2 seconds, (Each 1000 equals 1 seconds, unit is in milliseconds.)
    
    k = cv2.waitKey(2000)
    #Destroy Windows to save memory.
    cv2.destroyAllWindows()