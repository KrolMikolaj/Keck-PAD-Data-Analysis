#!/usr/bin/python3
#A version of chipbychip which only analizes exposure times up to 1ms, also removes exposures 0 and 1 from the averages

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#square and averager find the average intensity across a chip
def square(start,stop):
    change = 2 * shrink
    sqr = (stop[1] - start[1] - change) * (stop[0] - start[0] - change)
    return(sqr)

def averager(start,stop,arr):
    tot = 0
    for i in range(start[0] + shrink,stop[0] - shrink):
        for p in range(start[1] + shrink,stop[1] - shrink):
            tot += arr[i][p]
    return(tot/square(start,stop))

#Converts tif files into numpy arrays and outputs a 2D array, each row being 50 average intensities across the chosen chip
def chip(start,stop,times, chipnum):
    fdata = []
    counter = 0
    for frame in range(8):
        for time in times:
            data = []
            for exp in range(50):
                file = 'lintest_all_' + time + '_' + chipnum + '_' + str(exp) + '_00000_' + str(frame) + '.tif'
                img = Image.open(file, 'r')
                intn = np.array(img)
                data.append(averager(start,stop,intn))
            data = np.array(data)
            fdata.append([np.average(data),np.std(data)])
            counter += 1
    fdata = np.array(fdata)
    return(fdata)

#Global Variables that change the peramerters of the chip function and later on the plotter function
shrink = 4
xy0 = [(2,2),(3,135),(136,2),(137,135),(269,2),(270,135)]
xyf = [(129,129),(130,262),(264,129),(265,262),(396,129),(397,262)]
expts = ['1ms','2ms','3ms','4ms','5ms','6ms','7ms','8ms','9ms']
chips = ['chip0','chip1','chip2','chip3','chip4','chip5']
exts = [1,2,3,4,5,6,7,8,9]
ranges = [(0,9),(9,18),(18,27),(27,36),(36,45),(45,54),(54,63),(63,72)]
colors = ['C0','C1','C2','C3','C4','C8','C6','C9']

#Functions used for making plots
def framer(arr,rang):
    avgs = []
    for i in range(rang[0],rang[1]):
        avgs.append(arr[i][0])
    return(avgs)

def barrer(arr,rang):
    stds = []
    for j in range(rang[0],rang[1]):
        stds.append(arr[j][1])
    return(stds)

def plotter(arr,rang,xs,clr,chipnum):
    for k in range(8):
            plt.scatter(xs,framer(arr,rang[k]),c=clr[k])
            plt.errorbar(xs,framer(arr,rang[k]),yerr=barrer(arr,rang[k]),ecolor=clr[k])
    plt.legend(['f0','f1','f2','f3','f4','f5','f6','f7'])
    plt.title(chipnum)
    plt.ylabel('Intensity [ADU]')
    plt.xlabel('Exposure Time [ms]')
    plt.savefig('lintest_all_' + chipnum + '.png')
    plt.clf()

#main
for num in range(6):
    plotter(chip(xy0[num],xyf[num],chips[num])expts,ranges,exts,colors,chips[num])