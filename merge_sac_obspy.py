#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Attention: the merged file may need to be deleted after every run!
@author: Sarvandani
"""
import os
from obspy import read
from obspy import Stream
os.chdir ('/volumes/DRIVE_2/Merge_github')
path = '/volumes/DRIVE_2/Merge_github/'
RECEIVER_name = "SULZ.LHZ.CH"
##############################################################################################
st1= Stream()
for file in os.listdir(path):
    if file.startswith('.'):
        continue
    if RECEIVER_name in file:
        st1.extend(read(path + file))
      
st1.merge(method=1, fill_value=0, interpolation_samples=1)
# we change the compnent of  receiver => Z, N, E
st1 = st1.select(channel='*Z')
print(st1)
tr = st1[0]
tr.plot(color='green')  
tr.write("merged_file.sac", format="sac") 
out = read("/Volumes/DRIVE_2/Merge_github/merged_file.sac")
out.plot(color='red')  

