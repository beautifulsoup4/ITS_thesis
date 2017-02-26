import parsing
import pandas as pd 
import os.path
import numpy as np
import matplotlib.pyplot as plt
import csv
import Traffic_Dataframe
import io
import re
import datetime 
BASE = "/Users/radhikanikam/Downloads/Traffic_Data"
now = datetime.datetime.now()
tmp = "Day4"
#tmp = str(now.strftime("%Y-%m-%d"))
TEMP_0 = "/" + tmp +"/"
folder = BASE+TEMP_0
os.chdir(folder)

#print(len(os.listdir(folder)))
#os.chdir('..')
files = []
for i in os.listdir(folder):
	if not i.startswith('.'):
		g = io.open(i, mode = 'rt', encoding = 'cp1252')
		#print(os.path.abspath(i))
		#g = open(os.path.abspath(i))
		#f.encode('utf-8').strip()
		#print(g)
		
		text = g.read()
		#COMMENT THE FOLLOWING OUT AFTER 1 RUN
		# text = re.sub('.\Z','',text)
		# print(text)
		# with open(i,"rb+") as out:
		# 	out.seek(-1,os.SEEK_END) 
		# 	out.truncate()
		with open(i.replace('.json','r.json'),"a+") as outfile:
			outfile.write('[' + '\n' + text + '\n]')	
			files.append(outfile.name)
			outfile.close()
#[files.append(i) for i in os.listdir(folder)]
os.chdir('..')
if os.path.isdir(folder + "CSV/") == False:
	os.makedirs(folder + "CSV/")

for i in files:

  	file_name = folder + i #i.replace('.json','r.json')
  	file_out = folder + "CSV/" + i.replace('.json', '.csv') 
  	Traffic_Dataframe.to_DataFrame(file_name,file_out)

#print(files)