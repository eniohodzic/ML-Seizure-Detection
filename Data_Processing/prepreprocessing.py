#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:52:59 2022

@author: HemSem
"""
import os

# regular expression python
# https://docs.python.org/3/library/io.html

def annotate_edf_file(signal, folder):
    # imports raw signal, and folder
    # folder should contain a .txt file
    # then associate the .txt file data with the signal
    
    f = open('5483367_20151228_eg.txt', 'r')
    content = f.read()
    text = ["no electrographic seizures","no seizures","no seizures during"]
    if any(i in text for i in content):
        print("no Electrographic seizures found")
    else:
        print("seizures found")
        

    return txt_filename



