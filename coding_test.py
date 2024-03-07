# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:56:44 2024
Rename the .jpg files usinf their subdirectories under the main directories ..
i.e. feb25_2009Images, octoberimages, trip02_april27_200.

Then moved the renamed images under their respective main ridrectories.
Need to convert the code to a function that could be called for the respective directories..
feb25_2009Images, octoberimages, trip02_april27_200.




@author: dossantoss
"""
import os
import shutil
from os import walk
import re

names=[]

directory = "C:/Users/dossantoss/Documents/GitHub/STRI-data-center-03/newImages/feb25_2009images"




for (dir_path, dir_name, filenames) in walk(directory):
     
    for filename in filenames:
         if re.search (r'\.jpg$', filename): 
            
            match = re.search(r'\\[0-9][a-zA-Z]\\[0-9]{3}[A-Z]{3}', dir_path)
            match_char= match.group(0)
            newname = str(match_char) + str(filename)
            mod_name = newname.replace("\\", "_")
            
            
            current_path_file = os.path.join(dir_path, filename)
            new_pathfile = os.path.join(dir_path, mod_name)
            
            
            print(current_path_file)
            print(new_pathfile)
            
            
            #print("In dir...")
            #print(dir_path)
            #print(filename)
            #print(mod_name)
            
            #rename the file
            confirm = input("Shoul I rename the file ...")
            if confirm =='y':
                os.rename(current_path_file,new_pathfile)
                
                file_destination = directory + "/" + mod_name
                
                #move the file to feb25_2009images
                new_path = shutil.move(new_pathfile, file_destination)
            else:
                
                print("too bad")
                exit(0)
             
           
            
            
            
            
            print("\n")
            #print(dir_path)
            #print(filename)
            #print(match)
             
     

     
     
     
    
   
    




