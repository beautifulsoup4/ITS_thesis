import sched, time
import API_calls
import os
BASE = "/Users/radhikanikam/Downloads/Traffic_Data"
TEMP_0 = "/Day4/"
if os.path.isdir(BASE + TEMP_0) == False:
	os.makedirs(BASE+ TEMP_0)
os.chdir(BASE + TEMP_0)
start_time = time.time()
while True:
		if time.time() >= start_time + 10800.0:	#43200 for 12 hour period // Rush hours 7-10am, 5-8 pm =10800 sec
			os.makedirs(BASE + "/Day" + [str(i) for i in range(2,6)])
			exit()
		else:
			calls = [str(i*50) for i in range(27)]
			[API_calls.get_data(add =calls[i] , suffix = str(time.strftime("%H:%M"))) for i in range(len(calls))]
				
			print (time.strftime("%H:%M:%S"))
			#time.sleep(60.0 - ((time.time() - start_time) % 60.0))
			time.sleep(600.0)



			#For once every 10 mins, generate seperate file, named by time and date
			#for once every day, store these full day files in a folder, calculate correlations between adjacent streets
			#At the end of the week-5days, see that correlations are consistent

