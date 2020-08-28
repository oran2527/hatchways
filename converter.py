#!/usr/bin/python3

import csv
import sys
import os.path
option = 0
exist = False

try:
    exist = os.path.isfile(sys.argv[1])    
except:    
    while exist == False:
        print("Type the right and existing csv filenamed\n") 
        print("Or type 0 if you want to exit the program")
        option = input()
        exist = os.path.isfile(option)
        if exist == True and option != '0':
            with open(option) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                keys = []
                jsonfile = {}
                jsonline = {}
                for row in csv_reader:
                    if line_count == 0 and row != "":
                        for row_i in row:
                            keys.append(row_i)
                        line_count += 1    
                    else:
                        for i in range(0, len(keys)):
                            jsonline[keys[i]] = row[i]
                        jsonfile[line_count] = jsonline
                        jsonline = {}
                        line_count += 1    
                print(jsonfile)                
        if option == '0':
            break       
   
