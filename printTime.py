#! /usr/bin/env python  
#coding=utf-8  
import time
import os
a=time.localtime()
filePath=os.path.split(os.path.realpath(__file__))[0]
fileData = open(filePath+"/testTime.txt", "a")
fileData.write(str(a)+"\n")
fileData.close()