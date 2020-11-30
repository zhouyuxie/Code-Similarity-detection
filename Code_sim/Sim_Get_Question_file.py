#coding=utf-8
from __future__ import print_function
import rarfile
import zipfile
from sim import *
import os
import filetype
import shutil

#Create directory to store the code for each question.
if os.path.isdir("AS2_Q1") == False:
    os.mkdir("AS2_Q1")
else:
    shutil.rmtree('AS2_Q1')
    os.mkdir("AS2_Q1")

if os.path.isdir("AS2_Q2") == False:
    os.mkdir("AS2_Q2")
else:
    shutil.rmtree('AS2_Q2')
    os.mkdir("AS2_Q2")

if os.path.isdir("AS2_Q3") == False:
    os.mkdir("AS2_Q3")
else:
    shutil.rmtree('AS2_Q3')
    os.mkdir("AS2_Q3")

if os.path.isdir("AS2_Q4") == False:
    os.mkdir("AS2_Q4")
else:
    shutil.rmtree('AS2_Q4')
    os.mkdir("AS2_Q4")

if os.path.isdir("AS2_Q5") == False:
    os.mkdir("AS2_Q5")
else:
    shutil.rmtree('AS2_Q5')
    os.mkdir("AS2_Q5")

if os.path.isdir("AS2_Q6") == False:
    os.mkdir("AS2_Q6")
else:
    shutil.rmtree('AS2_Q6')
    os.mkdir("AS2_Q6")

#Get the list of current directory. 
dir_list = os.listdir("AS2")
os.chdir("AS2")
#print(dir_list)


#delete the .DS_Store file in MAC OS. 
for i in dir_list:
    if "DS_Store" in i:
        #os.remove(i)
        dir_list.remove(i)

#print(dir_list)

Submitted_Student = []
#To expand the file, and 
#判断解压出来的文件夹里面有没有directory, 如果有， 那就再往后面进一步。 Unfinished

for i in dir_list:
    #print(i.find("July, 2020)_")+1)
    Student_ID = i[int(i.find("July, 2020)_"))+12:int(i.find("July, 2020)_"))+21]
    Submitted_Student.append(Student_ID)
    #print(Student_ID)
    kind = filetype.guess(i)
    print(i)
    if kind.extension == "zip":
        if os.path.isdir(Student_ID) == False:
            os.mkdir(Student_ID)
        rf = zipfile.ZipFile(i)
        rf.extractall(os.path.splitext(Student_ID)[0])
        rf.close()
        File_List_Under_ID = os.listdir(Student_ID)
        #Only save the python and directory. 
        for f in File_List_Under_ID:
            try: 
                os.chdir(Student_ID)
                #os.chdir("..")
            except:
                continue
            #print(f)
            if ".py" in f:
                #print(f)
                if  "1"  in f:
                    Question_ID = Student_ID+"_Q1"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q1")
                elif  "5"  in f:
                    Question_ID = Student_ID+"_Q5"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q5")
                elif  "3"  in f:
                    Question_ID = Student_ID+"_Q3"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q3")
                elif  "4"  in f:
                    Question_ID = Student_ID+"_Q4"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q4")
                elif  "6"  in f:
                    Question_ID = Student_ID+"_Q6"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q6")
                elif  "2" in f:
                    Question_ID = Student_ID+"_Q2"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q2")
                else:
                    continue
            try:
                os.chdir("..")
            except:
                continue               


    elif kind.extension == "rar":
        if os.path.isdir(Student_ID) == False:
            os.mkdir(Student_ID)
        rf = rarfile.RarFile(i)
        rf.extractall(os.path.splitext(Student_ID)[0])
        rf.close()

        File_List_Under_ID = os.listdir(Student_ID)
        #Only save the python and directory. 
        for f in File_List_Under_ID:
            try: 
                os.chdir(Student_ID)
                #os.chdir("..")
            except:
                continue
            if ".py" in f:
                if  "1"  in f:
                    Question_ID = Student_ID+"_Q1"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q1")
                elif  "5"  in f:
                    Question_ID = Student_ID+"_Q5"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q5")
                elif  "3"  in f:
                    Question_ID = Student_ID+"_Q3"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q3")
                elif  "4"  in f:
                    Question_ID = Student_ID+"_Q4"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q4")
                elif  "6" in f:
                    Question_ID = Student_ID+"_Q6"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q6")
                elif  "2"  in f:
                    Question_ID = Student_ID+"_Q2"
                    os.rename(f,Question_ID+'.py')
                    shutil.copy(Question_ID+'.py',"../../AS2_Q2")
                else:
                    continue
            try:
                os.chdir("..")
            except:
                continue


    elif kind.extension == "7z":
        continue
    else:
        print("Do not suppport this kind of file now.")


