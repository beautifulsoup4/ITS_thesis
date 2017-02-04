################################## TRAFFIC STATISTICS ############################################

from xml.etree import ElementTree as et
f = open('2o.xml','r')
#print(f.read(10))
tree = et.parse(f)
# Data of which car is in which lane
def car_in_lane(s):
    for time in tree.iter('timestep'):

        t = int(float(time.attrib.get('time')))

        if(t ==(s)):
            for edge in time:
            # e = node1.attrib.get('id')
                for lane in edge:
                    lane_id = lane.attrib.get('id')
                    for veh in lane:
                        veh_id = veh.attrib.get('id')
                        print("%s         in lane               %s" % (veh_id, lane_id))
# No of cars per lane, given lane id
def cars_per_lane(l):

    for time in tree.iter('timestep'):
        count = 0
        for edge in time:
            for lane in edge:
                if l == lane.attrib.get('id') and len(list(lane)):
                    for veh in lane:
                        count= count + 1
        print('%s    car(s) at time %s'%(count,time.attrib.get('time')))

#All the lanes crossed by the car at each time step
def car_journey(c):
    for time in tree.iter('timestep'):
        for edge in time:
            for lane in edge:
                for veh in lane:
                    if c == veh.attrib.get('id'):
                        print('Lane  %s    at time    %s   at pos      %s' %(lane.attrib.get('id'), time.attrib.get('time'), veh.attrib.get('pos')))

print('Traffic Statistics (Select One):\n')
print(' 1. Car in Lane\n 2. No. of Cars/Lane at given time\n 3. Car journey with timestep\n')
print('Answer: ')
ans = int(input())
if ans == 1:
    print("Enter time: ")
    s = int(input())
    car_in_lane(s)
elif ans == 2:
    print("Enter lane:")
    l = input()
    cars_per_lane(l)
else:
    print("Enter car id:")
    c = input()
    car_journey(c)

f.close()