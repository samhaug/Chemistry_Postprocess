# Made by Samuel Haugland Nov/2014

# Import python modules
import numpy as np
import os
import subprocess as sp
import datetime

# Dictionary to store the lines plotted on the final figure
line_dict = {'x1' : [17.5, 17.5, 17.5, 22.0, 20.0, 17.5, 17.5, 20.0],
             'y1' : [5132.5, 5130.0, 5124.0, 5128.5, 5130.0, 5132.5, 5130.0, 5130.0],
             'x2' : [17.5, 20.0, 22.0, 19.0, 17.5, 17.5, 17.5, 20.0, 17.5],
             'y2' : [0.70225, 0.70300, 0.7028, 0.7080, 0.7050, 0.7035, 0.70225, 0.7030, 0.7035],
             'x3' : [17.5, 17.5, 17.5, 19.5, 22.0, 20.0, 17.5, 17.5, 20.0],
             'y3' : [0.123, 0.132, 0.150, 0.153, 0.150, 0.132, 0.123, 0.132, 0.132],
             'x4' : [17.5, 18.0, 17.5, 20.0, 22.0, 19.5, 17.5, 18.0, 17.5, 20.0, 18.0],
             'y4' : [39.0, 38.2, 37.0, 39.0, 40.8, 40.0, 39.0, 38.2, 37.0, 39.0, 38.2],
             'x5' : [17.5, 17.5, 19.5, 22.0, 19.0, 17.5, 17.5, 19.5, 17.5],
             'y5' : [15.6, 15.3, 15.5, 15.85, 15.7, 15.6, 15.3, 15.5, 15.6],
             'x6' : [0.7028, 0.705, 0.708, 0.704, 0.70225, 0.7028, 0.704],
             'y6' : [5128.5, 5124.0, 5127.0, 5130.0, 5132.5, 5128.5, 5130.0],
            }

import matplotlib
# Make final output into PDF vector format, for use in Adobe Illustrator
matplotlib.use('PDF')

import matplotlib.pyplot as plt

#Sets the window size. Adjust to make the window dimensions different.
from pylab import *
rcParams['figure.figsize'] = 15, 12

# Open the GridChemistry.csv file, which has averaged isotope abundance values 
# in each column, along with cartesian coordinates, and a boolean that will 
# determine if a tracer element is in POOL.

Fopen = open("./MODELS/EPSL_2008/newtrial/GridChemistry.csv")
Rfile = Fopen.read()
Rows = Rfile.split('\n')

# Define array that will be filled with tracer dictionaries
Tracer_list = []

# Each element of Tracer_list is an associative array (a dictionary type) that 
# will be used in plotting isotope ratio diagrams.
for ii in range(1,len(Rows)-1):
# Split by commas; the .csv file is partitioned this way
   string = Rows[ii].split(',')

# A list of dictionaries is filled. This is more intuitive than making an array 
# thats column numbers must be associated with geochemical information. Each
# row in the .CSV file is read through and the numbers in between the commas are
# set as the entries in each dictionary.

   Tracer_list.append({'x_coord' : float(string[0]), 
                      'y_coord' : float(string[1]),
                      'NGCount_grid' : float(string[2]),
                      'Pool' : bool(float(string[3])),
                      'TZ' : bool(),
                      'ASTH' : bool(),
                      'LM' : bool(),
                      'Age' : float(string[4]),
                      'Pb206' : float(string[5]),
                      'Pb207' : float(string[6]),
                      'Pb208' : float(string[7]),
                      'Pb204' : float(string[8]),
                      'Sr87_86' : float(string[9]),
                      'Nd143_144' : float(string[10]),
                      'Os187_188' : float(string[11])})

# Determine what mantle region to classify a tracer as based on its radial 
# position.
for jj in range(0,len(Tracer_list)-1):
   x =  Tracer_list[jj]['x_coord']
   y =  Tracer_list[jj]['y_coord']
   radius = pow((x**2+y**2),0.5)
   if radius <= 1.114: # non-dim radii corresponding to lower mantle
      Tracer_list[jj]['LM'] = bool(1)
   elif 1.114 < radius <= 1.251: # non-dim radii corresponding to Transition zone;
      Tracer_list[jj]['TZ'] = bool(1)
   elif 1.251 < radius <= 1.385: # non-dim radii corresponding to Asthenosphere
      Tracer_list[jj]['ASTH'] = bool(1)

# Rename 'Tracer_list' to 'T' for ease of syntax.
T = Tracer_list

# Find number of Tracer_list elements that correspond to each mantle region for 
# preallocation. This is only used for troubleshooting.
'''
pool_length = []
TZ_length = []
LM_length = []
ASTH_length = []

for nn in range(1,len(Tracer_list)-1):
    if Tracer_list[nn]['Pool']:
        pool_length.append(1)
    if Tracer_list[nn]['TZ']:
        TZ_length.append(1)
    if Tracer_list[nn]['LM']:
        LM_length.append(1)
    if Tracer_list[nn]['ASTH']:
        ASTH_length.append(1)
'''
# Isotope values will be appended to these lists. They must be cleared before
# their values are changed.

xlist_pool = [] 
ylist_pool = [] 
xlist_TZ = [] 
ylist_TZ = []
xlist_ASTH = [] 
ylist_ASTH = [] 
xlist_LM = [] 
ylist_LM = [] 

##############################################################################
### PLOT 1 OF 6 ##############################################################
##############################################################################

print "Working on plot 1"
plt.subplot(3,2,1)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        xlist_pool.append(T[ii]['Pb206']/T[ii]['Pb204'])
        ylist_pool.append(T[ii]['Nd143_144'])
    if T[ii]['TZ']:
        xlist_TZ.append(T[ii]['Pb206']/T[ii]['Pb204'])
        ylist_TZ.append(T[ii]['Nd143_144'])
    if T[ii]['ASTH']:    
        xlist_ASTH.append(T[ii]['Pb206']/T[ii]['Pb204'])
        ylist_ASTH.append(T[ii]['Nd143_144'])
    if T[ii]['LM']:
        xlist_LM.append(T[ii]['Pb206']/T[ii]['Pb204'])
        ylist_LM.append(T[ii]['Nd143_144'])
# Scatter plot mantle regions
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
# Plot lines that roughly define mantle regions
plt.plot(line_dict['x1'], line_dict['y1'],'k')
# Plot text lables of different mantle regions on the graph
plt.text(17.5,5131,'DMM')
plt.text(17.7,5124,'EM1')
plt.text(19.0,5126,'EM2')
plt.text(22.0,5128,'HIMU')
# Set x and y axis limits
plt.ylim((5122,5136))
plt.xlim((15,24))
# Label axes
plt.xlabel('206Pb/204Pb')
plt.ylabel('10,000 x 143Nd/144Nd')

# Clear the lists so you don't continue to append to them
ylist_pool = []
ylist_TZ = []
ylist_ASTH = []
ylist_LM = []

##############################################################################
### PLOT 2 OF 6 ##############################################################
##############################################################################
print "Working on plot 2"
plt.subplot(3,2,2)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        ylist_pool.append(T[ii]['Sr87_86'])
    if T[ii]['TZ']:
        ylist_TZ.append(T[ii]['Sr87_86'])
    if T[ii]['ASTH']:    
        ylist_ASTH.append(T[ii]['Sr87_86'])
    if T[ii]['LM']:
        ylist_LM.append(T[ii]['Sr87_86'])
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
plt.plot(line_dict['x2'], line_dict['y2'],'k')
plt.text(17.5,0.7028,'DMM')
plt.text(17.7,0.7050,'EM1')
plt.text(19.0,0.7075,'EM2')
plt.text(22.0,0.7026,'HIMU')
plt.ylim((0.702,0.709))
plt.xlim((15.5,24))
plt.xlabel('206Pb/204Pb')
plt.ylabel('87Sr/86Sr')

ylist_pool = []
ylist_TZ = []
ylist_ASTH = []
ylist_LM = []

##############################################################################
### PLOT 3 OF 6 ##############################################################
##############################################################################
print "Working on plot 3"
plt.subplot(3,2,3)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        ylist_pool.append(T[ii]['Os187_188'])
    if T[ii]['TZ']:
        ylist_TZ.append(T[ii]['Os187_188'])
    if T[ii]['ASTH']:    
        ylist_ASTH.append(T[ii]['Os187_188'])
    if T[ii]['LM']:
        ylist_LM.append(T[ii]['Os187_188'])
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
plt.plot(line_dict['x3'], line_dict['y3'],'k')
plt.text(17.5,0.123,'DMM')
plt.text(17.7,0.150,'EM1')
plt.text(19.0,0.135,'EM2')
plt.text(22.0,0.153,'HIMU')
plt.ylim((0.12,0.30))
plt.xlim((15,24))
plt.xlabel('206Pb/204Pb')
plt.ylabel('187Os/188Os')

ylist_pool = []
ylist_TZ = []
ylist_ASTH = []
ylist_LM = []

##############################################################################
### PLOT 4 OF 6 ##############################################################
##############################################################################
print "Working on plot 4"
plt.subplot(3,2,4)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
       ylist_pool.append(T[ii]['Pb208']/T[ii]['Pb204'])
    if T[ii]['TZ']:
       ylist_TZ.append(T[ii]['Pb208']/T[ii]['Pb204'])
    if T[ii]['ASTH']:    
       ylist_ASTH.append(T[ii]['Pb208']/T[ii]['Pb204'])
    if T[ii]['LM']:
       ylist_LM.append(T[ii]['Pb208']/T[ii]['Pb204'])
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
plt.plot(line_dict['x4'], line_dict['y4'],'k')
plt.text(17.5,37.4,'DMM')
plt.text(17.7,39.0,'EM1')
plt.text(19.0,39.8,'EM2')
plt.text(22.0,40.8,'HIMU')
plt.ylim((35,44))
plt.xlim((15,24))
plt.xlabel('206Pb/204Pb')
plt.ylabel('208Pb/204Pb')
    
ylist_pool = []
ylist_TZ = []
ylist_ASTH = []
ylist_LM = []

##############################################################################
### PLOT 5 OF 6 ##############################################################
##############################################################################
print "Working on plot 5"
plt.subplot(3,2,5)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
       ylist_pool.append(T[ii]['Pb207']/T[ii]['Pb204'])
    if T[ii]['TZ']:
       ylist_TZ.append(T[ii]['Pb207']/T[ii]['Pb204'])
    if T[ii]['ASTH']:    
       ylist_ASTH.append(T[ii]['Pb207']/T[ii]['Pb204'])
    if T[ii]['LM']:
       ylist_LM.append(T[ii]['Pb207']/T[ii]['Pb204'])
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
plt.plot(line_dict['x5'], line_dict['y5'],'k')
plt.text(17.5,15.38,'DMM')
plt.text(17.7,15.5,'EM1')
plt.text(19.0,15.65,'EM2')
plt.text(22.0,15.86,'HIMU')
plt.ylim((15.0,16.5))
plt.xlim((15,24))
plt.xlabel('206Pb/204Pb')
plt.ylabel('207Pb/204Pb')

xlist_pool = []
xlist_TZ = []
xlist_ASTH = []
xlist_LM = []

ylist_pool = []
ylist_TZ = []
ylist_ASTH = []
ylist_LM = []

##############################################################################
### PLOT 6 OF 6 ##############################################################
##############################################################################
print "Working on plot 6"
plt.subplot(3,2,6)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        xlist_pool.append(T[ii]['Sr87_86'])
        ylist_pool.append(T[ii]['Nd143_144'])
    if T[ii]['TZ']:
        xlist_TZ.append(T[ii]['Sr87_86'])
        ylist_TZ.append(T[ii]['Nd143_144'])
    if T[ii]['ASTH']:    
        xlist_ASTH.append(T[ii]['Sr87_86'])
        ylist_ASTH.append(T[ii]['Nd143_144'])
    if T[ii]['LM']:
        xlist_LM.append(T[ii]['Sr87_86'])
        ylist_LM.append(T[ii]['Nd143_144'])
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
plt.plot(line_dict['x6'], line_dict['y6'],'k')
plt.text(0.7025,5131,'DMM')
plt.text(0.7050,5124,'EM1')
plt.text(0.7075,5126,'EM2')
plt.text(0.7025,5128,'HIMU')
plt.ylim((5122,5136))
plt.xlim((0.702,0.709))
plt.xlabel('87Sr/86Sr')
plt.ylabel('10,000 x 143Nd/144Nd')

plt.savefig('dummyfile.pdf')
plt.show()

# U/I commands for saving the plot, deleting the plot, or renaming the plot.
yes = set(['yes','ye','y',''])
no = set(['no','n'])
date = set(['date','dat','da','d'])

print "Save this figure?"
choice = raw_input("Enter 'yes' or 'no' :")

if choice in yes:
    print "Enter name or type 'date' to name by date"
    namechoice = raw_input("Enter name or 'date' :")

    if namechoice in date:
        dt = str(datetime.datetime.now())
        os.rename("dummyfile.pdf", dt+'.pdf')
    else:
        os.rename("dummyfile.pdf", namechoice+'.pdf')

elif choice in no:
    sp.call("rm dummyfile.pdf",shell=True)

else:
    print "Please respond with 'yes' or 'no'"

