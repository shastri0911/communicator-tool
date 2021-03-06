
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################################
#                               content                               #


# Objective
    
#   Given the usr file for a language, generate the target language sentence.
#   Currently it is done for Tamil, Hindi
#    
#  Need to rename all csv occurences to usr 

# Logic:
#   
    1. Read the concept dictionary
    2. Read the usr file and capture all the information for giving to target generator (inverse of apertium morph) 
    3. 


Running :

    python  tamil-csv-sent-gen.py tamil.csv hnd-tamil-concept.dic  > tamil-gen.tmp
    lt-proc -cg tools/morph/Tamil/Tamilgenerator_KP_CALTS_030917.mo < tamil-gen.tmp 

#######################################################################


import sys
import csv
import subprocess
import os.path
import re

#path for communicator tool
COMMUNICATOR_TOOL_PATH = "/home/sriram/phd/communicator/communicator-tool/"

#read the concept dic
with open(sys.argv[2],'r') as fp:
    concept_dic = fp.readlines()

fp.close()

#read the tamil usr file  and prepare  all the information required for generation (apertium input)

with open(COMMUNICATOR_TOOL_PATH+'csv-generator/'+sys.argv[1], 'r') as fp:


    #csv_cont = csv.DictReader(fp)
    csv_cont = csv.reader(fp)
    
    # Intialise  all the information related lists
    i = 0
    group = []
    root = []
    wid = []
    pos = []
    gnp = []
    const = []
    karaka = []

    #read each row in usr file according to the usr-schema provided
    #need to do as per the usr-schema
    #maintain a hash instead of a simple list

    for row in csv_cont:

        if(i == 0):
            group = list(row)
        if(i == 1):
            root = list(row)
        if(i == 2):
            wid = list(row)
        if(i == 3):
            pos = list(row)
        if(i == 4):
            gnp = list(row)
        if(i == 5):
            const = list(row)
        if(i == 6):
            karaka = list(row)

        i += 1

    #print group,root, wid, pos, gnp, const, karaka

#since the way of writing in the usr file and the apertium input in the target language are
# different, so we have to map those acronyms as per the apertium input required.


map_pos = {"pron":"pn"}

map_gen = {"m":"any"}
map_num = {"sg":"sg"}
map_per = {"u":"1"}


#for each word in the usr file generate the required information to generate the final word in the apertium generator.

for i in range(0,len(wid)):
    
    lroot = root[i].split('_')[0]
    if(pos[i] != ''):
        lpos = map_pos[pos[i]]
    else:
        for l in concept_dic:
            if(root[i] == l.split(',')[1]):
                lpos = l.split(',')[2].strip()


    if(lpos == 'nst'):
        lgen = 'null'
    else:
        if(gnp[i] != ''):
            lgen = gnp[i].split()[0].strip("][")
            if((lpos == 'n') and (lgen == '-')):
                lgen = '0'
            else:
                lgen = map_gen[gnp[i].split()[0].strip("][")]
    if(gnp[i] != ''):
        lnum = map_num[gnp[i].split()[1].strip("][")]

    if(lpos == 'nst'):
        lper = 'null'
    else:
        if(gnp[i] != ''):
            lper = gnp[i].split()[2].strip("][")
            if((lpos == 'n') and (lper == 'a')):
                lper = '0'
            else:
                lper = map_per[gnp[i].split()[2].strip("][")]

        #if verb gnp is same as k1
        elif(lpos == 'v'):
            for j in range(0,len(karaka)):
                if(re.search("k1",karaka[j])):
                    if(i+1 == int(karaka[j].split(':')[0])):

                        lgen = map_gen[gnp[j].split()[0].strip("][")]
                        lper = map_per[gnp[j].split()[2].strip("][")]



    if(lpos == 'v'):
        lcase = '0'
    else:
        lcase = "d"
    

    if(re.search("_",group[i])):
        ltam_vib = group[i].split('_')[1]


    if (lpos == 'det'):
        print "^"+lroot+"<cat:"+lpos+">"+"$"
    else:
        print "^"+lroot+"<"+lpos+">"+"<"+lgen+">"+"<"+lnum+">"+"<"+lper+">"+"<"+lcase+">"+"<"+ltam_vib+">"+"$"


