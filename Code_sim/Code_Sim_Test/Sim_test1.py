#coding=utf-8
from __future__ import print_function
from sim import *
import os
import filetype
import shutil
Current_file = "buildtagger.py"
Compared_file = "buildtagger1.py"
Code_Similarity1 = code_sim(Current_file, Compared_file, 'fake_anti_uni')
Code_Similarity2 = code_sim(Current_file, Compared_file, 'jaccard')

print(Code_Similarity1,Code_Similarity2)
