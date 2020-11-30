#coding=utf-8
from __future__ import print_function
from sim import *
import os
import filetype
import shutil

File_Path = "AS2_Q6"
Sim_result = open("Similarity_Result.txt","w")
dir_list = os.listdir(File_Path)

os.chdir(File_Path)

#delete the .DS_Store file in MAC OS. 
for i in dir_list:
    if "DS_Store" in i:
        #os.remove(i)
        dir_list.remove(i)

#print('Using jaccard method')
for i in range(len(dir_list)):
    Current_file = dir_list[i]
    if i>0:
        for j in range(i):
            Compared_file = dir_list[j]
            #print(Current_file)
            #print(Compared_file)
            Code_Similarity = code_sim(Current_file, Compared_file, 'fake_anti_uni')
            if Code_Similarity > 0.6:
                Sim_Record = Current_file+'    '+Compared_file+'     '+"Similarity:"+str(Code_Similarity)+"\n"
                Sim_result.write(Sim_Record)
Sim_result.close()
