################################### NETWORK STATISTICS ##############################

from xml.etree import ElementTree as et
import numpy as np
from matplotlib import pyplot as plt

f = open('2_o.xml','r')
tree = et.parse(f)
def avg_cars(l,t1,t2):
    glob_count = 0
    for time in tree.iter('timestep'):
        count = 0
        if int(float(time.attrib.get('time'))) in range(t1,t2+1):
            for edge in time:
                for lane in edge:
                    if l == lane.attrib.get('id') and len(list(lane)):
                        for veh in lane:
                            count= count + 1
        glob_count = glob_count+count

    avg = float(glob_count/(t2-t1+1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

    return avg
def corr(l1,l2):
    t = 0
    x_1 = []
    y_1 = []
    for t in range(2,500,2):
        av1 = avg_cars(l1,1,t)
        x_1.append(av1)
        av2 = avg_cars(l2,1,t)
        y_1.append(av2)

      #  plt.scatter(av1,av2)
      #  plt.xlabel(l1)
      #  plt.ylabel(l2)
   # plt.plot([1,2,3,4],[7,8,9,10])


    fit = np.polyfit(x_1,y_1,1)
    fit_fn = np.poly1d(fit)
    plt.scatter(x_1,y_1)
  #  plt.plot( x_1, fit_fn(x_1), '--k')

    plt.hold(True)


def avg_edge(e,t1,t2):

    #first  count the no. of lanes in an edge, add the avg of the edges and divide by no. of lanes?
    for time in tree.iter('timestep'):
        count = 1
        if int(float(time.attrib.get('time'))) in range(t1,t2+1):
            for edge in time:
                if e == edge.attrib.get('id') and len(list(edge)):
                    for lanes in edge:
                        count = count+1

    lane_avs = []
    SUM = 0
    for i in range(count):
        suffix = str(i)
        l1 =e+'_'+suffix
       # print(l1)
        av = avg_cars(l1,t1,t2)
        lane_avs.append(av)
        SUM = SUM+av
    #    print(av)
    #print(lane_avs)
    AVERAGE = float(SUM/len(lane_avs))


    return AVERAGE


def edge_corr(e1,e2):
    #pass
    t = 0
    for t in range(2, 500):
        av1 = avg_edge(e1, 1, t)
        av2 = avg_edge(e2, 1, t)
        print(av1,av2)
        plt.scatter(av1, av2)
        plt.xlabel(e1)
        plt.ylabel(e2)
        # plt.plot([1,2,3,4],[7,8,9,10])
    plt.hold(True)

#plt.plot([1, 2, 3, 4], [7, 8, 9, 10])
#print(avg_edge('--31272#7',90,100))
#print(avg_edge('-31564#2',0,5))
corr('--30620_0','-31504#0_0')

"""
l1 = 'rads'
s = str(2)
e = l1+'_'+s
print(e)"""
plt.show()
"""
print('input t1,t2,l')
t1 = int(input())
t2 = int(input())
l = input()
av = avg_cars(l,t1,t2)
print(av)



plt.show()"""
f.close()
