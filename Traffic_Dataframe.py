import parsing
import pandas as pd 
import os.path
import numpy as np
import matplotlib.pyplot as plt
import csv
def to_DataFrame(filename_json,output_csv):

	f = parsing.csv_writer(filename_json)
	path1 = os.path.normpath(os.path.join(os.getcwd(),f))
	#print(path1)
	df = pd.DataFrame()
	df = pd.read_csv(path1)
	#print(df.shape)
	df_new = pd.DataFrame()
	df_new = pd.DataFrame(columns =['LinkID', 'RoadName', 'RoadCategory','SpeedBand', 'MinimumSpeed', 'MaximumSpeed','Location'])
	headers = ['LinkID', 'RoadName', 'RoadCategory','SpeedBand', 'MinimumSpeed', 'MaximumSpeed','Location']
	pieces = []
	pieces = [df.ix[:,i*7:(i+1)*7] for i in range(int(df.shape[1]/7))]
	for piece in pieces:
		piece.columns =  ['LinkID', 'RoadName', 'RoadCategory','SpeedBand', 'MinimumSpeed', 'MaximumSpeed','Location']
			
	#r = pd.concat(pieces, axis =0).drop_duplicates().reset_index(drop=True)
	e = pd.DataFrame()
	e = pd.concat(pieces, ignore_index = True).reset_index(drop = True)	
	e['mu'] = (e['MaximumSpeed']+ e['MinimumSpeed'])/2
	e['mu'].fillna(80, inplace = True)
	v = []
	i = 0
	#e['RandomSpeed'] 
	for i in range(e.shape[0]):
	 	v.extend(np.random.normal(e['mu'][i],1,1))
	e['RandomSpeed'] = v
	#e['RandomSpeed'] = e['RandomSpeed'].str.get(0)
	e1 = e.sort(['LinkID'], ascending = 1)
	#print(e1.head(10))
	#print(os.getcwd())
	#plt.plot(x = e['LinkID'], y = e['RandomSpeed'], kind = 'bar')
	
	
	output = pd.DataFrame({
				'LinkID' : e['LinkID'],
				'RoadName' : e['RoadName'],
				'Speed': e['RandomSpeed']
		})
	output.to_csv(output_csv , index = True)
	

if __name__ == "__main__"	:
	to_DataFrame('/Users/radhikanikam/Downloads/Traffic_Data/Day3/traffic_speedbands_08:51r.json', '/Users/radhikanikam/Downloads/Traffic_Data/Day3/traffic_speedbands_08:51r.csv')