#!/usr/bin/python3

#Import modules
import numpy as np
import decimal
import math
import os
import sys
import json

with open('job.sh', 'r') as file1:
	file_data2 = file1.read()

with open('KPOINTS','r') as file2:
	file_data3 = file2.read()

with open('INCAR','r') as file3:
	file_data4 = file3.read()

with open('POTCAR','r') as file4:
	file_data5 = file4.read()

parent = os.getcwd()

with open('PeriodicTableJSON.json', 'r') as pt:
	pt_data = json.load(pt)

for x in np.arange(2.20, 2.81, 0.001):
	
	#writes the POSCAR files to individual directories
	with open('POSCAR', 'r') as file:
		#elements = file.readlines()
		file_data = file.read()

	directory = str(round(x,2))
	os.makedirs(directory, exist_ok=True)
	numdir = os.path.join(parent,directory)
	#print(numdir)
	x = round((math.cos(math.pi/6)*x),6)
	y = round((math.sin(math.pi/6)*x),6)
	#print(x)
	#print(y)

	file_data = file_data.replace('%X', str(x))
	file_data = file_data.replace('%Y', str(y))
	
	with open(os.path.join(parent,directory,'POSCAR'), 'w') as file:
		file.write(file_data)

	#Obtaining species for POTCAR

	with open(os.path.join(parent,directory,'POSCAR'), 'r') as file:
		elements = file.readlines()
		species = elements[5]
		#print(species)

	#need to write other necessary files for VASP

	with open(os.path.join(parent,directory,'job.sh'), 'w') as file1:
		file1.write(file_data2)

	with open(os.path.join(parent,directory,'KPOINTS'), 'w') as file2:
		file2.write(file_data3)

	with open(os.path.join(parent,directory,'INCAR'), 'w') as file3:
		file3.write(file_data4)

	with open(os.path.join(parent,directory,'POTCAR'), 'w') as file4:
		file4.write(file_data5)

	#os.chdir(os.path.join(parent,directory))
os.rename('job.sh', 'oldjob.sh')


