import json
import csv
import sys
import os,io


def get_leaves(item, key = None):		#great!!
	if isinstance(item, dict):
		leaves = []
		for i in item.keys():
			leaves.extend(get_leaves(item[i],i))
		return leaves
	elif isinstance(item, list):
		leaves = []
		for i in item:
			leaves.extend(get_leaves(i,key))
		return leaves
	else:
		return [(key,item)]



def csv_writer(filename):
	json1=open(filename)
	print(json1)
	data = json.load(json1)
	
	#data = io.open(filename, mode = 'rt', encoding = 'cp1252')
	#print(data[0])
	path = '/Users/radhikanikam/Downloads/Traffic_Data/Day3/1.csv'
	path1 = path
	f = csv.writer(open(path, "w+"), delimiter = ',')

	write_header = True
	headers = ['LinkID', 'RoadName', 'RoadCategory','SpeedBand', 'MinimumSpeed', 'MaximumSpeed','Location']
	for entry in data:
		leaf_entries = (get_leaves(entry))
		del leaf_entries[0]
		leaf = zip(leaf_entries)
		if write_header:		
			f.writerow([k for k,v in (leaf_entries)])
		#f.writerow(headers)
			write_header = False	
		f.writerow([v for k,v in leaf_entries])	
		
	return path
	


if __name__ == "__main__":
	csv_writer('/Users/radhikanikam/Downloads/Traffic_Data/Day3/traffic_speedbands_08:00r.json')	
	#csv_writer('r.json')




