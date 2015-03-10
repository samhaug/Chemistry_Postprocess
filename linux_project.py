
# Import python modules
import numpy as np
import os
import subprocess as sp
import datetime


import matplotlib
# Make final output into PDF vector format, for use in Adobe Illustrator
matplotlib.use('PDF')

import matplotlib.pyplot as plt

#Sets the window size. Adjust to make the window dimensions different.
from pylab import *
rcParams['figure.figsize'] = 15, 12

# Open the sam_additions.900 file, which has averaged isotope abundance values 
# in each column, along with cartesian coordinates, and a boolean that will 
# determine if a tracer element is in POOL.

Fopen = open("./MODELS/EPSL_2008/newtrial/sam_additions.900")
Rfile = Fopen.read()
Rows = Rfile.split('\n')

# Define array that will be filled with tracer dictionaries
Tracer_list = []

# Each element of Tracer_list is an associative array (a dictionary type) that 
# will be used in plotting isotope ratio diagrams.
for ii in range(1,len(Rows)-1):
# Split by commas; the .csv file is partitioned this way
   string = Rows[ii].split()
# A list of dictionaries is filled. This is more intuitive than making an array 
# whos column numbers must be associated with geochemical information. Each
# row in the .CSV file is read through and the numbers in between the commas are
# set as the entries in each dictionary.

   Tracer_list.append({'x_coord' : float(string[0]), 
                      'y_coord' : float(string[1]),
                      'Pool' : bool(float(string[2])),
					  'Gd/Pb' : float(string[3]),
                      'Sm/Pb' : float(string[4]),
                      'La/Pb' : float(string[5]),
                      'Ba/Pb' : float(string[6]),
                      'Nd/Pb' : float(string[7]),
                      'TZ' : bool(),
                      'ASTH' : bool(),
                      'LM' : bool()
                      })

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
plt.figure(1)
#plt.subplot(1,3,1)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        xlist_pool.append(T[ii]['Gd/Pb'])
        ylist_pool.append(T[ii]['Sm/Pb'])
    if T[ii]['TZ']:
        xlist_TZ.append(T[ii]['Gd/Pb'])
        ylist_TZ.append(T[ii]['Sm/Pb'])
    if T[ii]['ASTH']:    
        xlist_ASTH.append(T[ii]['Gd/Pb'])
        ylist_ASTH.append(T[ii]['Sm/Pb'])
    if T[ii]['LM']:
        xlist_LM.append(T[ii]['Gd/Pb'])
        ylist_LM.append(T[ii]['Sm/Pb'])
# Scatter plot mantle regions
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
# Label axes
plt.xlabel('Gd152/Pb204')
plt.ylabel('Sm148/Pb204')
plt.show()

xlist_pool = [] 
ylist_pool = [] 
xlist_TZ = [] 
ylist_TZ = []
xlist_ASTH = [] 
ylist_ASTH = [] 
xlist_LM = [] 
ylist_LM = [] 

##############################################################################
### PLOT 2 OF 6 ##############################################################
##############################################################################

print "Working on plot 2"
#plt.subplot(1,3,2)
plt.figure(2)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        xlist_pool.append(T[ii]['Sm/Pb'])
        ylist_pool.append(T[ii]['Nd/Pb'])
    if T[ii]['TZ']:
        xlist_TZ.append(T[ii]['Sm/Pb'])
        ylist_TZ.append(T[ii]['Nd/Pb'])
    if T[ii]['ASTH']:    
        xlist_ASTH.append(T[ii]['Sm/Pb'])
        ylist_ASTH.append(T[ii]['Nd/Pb'])
    if T[ii]['LM']:
        xlist_LM.append(T[ii]['Sm/Pb'])
        ylist_LM.append(T[ii]['Nd/Pb'])
# Scatter plot mantle regions
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
# Label axes
plt.xlabel('Sm148/Pb204')
plt.ylabel('Nd144/Pb204')
plt.show()

xlist_pool = [] 
ylist_pool = [] 
xlist_TZ = [] 
ylist_TZ = []
xlist_ASTH = [] 
ylist_ASTH = [] 
xlist_LM = [] 
ylist_LM = [] 

##############################################################################
### PLOT 3 OF 6 ##############################################################
##############################################################################

print "Working on plot 3"
#plt.subplot(1,3,3)
plt.figure(3)
for ii in range(0,len(Tracer_list)-1):
    if T[ii]['Pool']:
        xlist_pool.append(T[ii]['La/Pb'])
        ylist_pool.append(T[ii]['Ba/Pb'])
    if T[ii]['TZ']:
        xlist_TZ.append(T[ii]['La/Pb'])
        ylist_TZ.append(T[ii]['Ba/Pb'])
    if T[ii]['ASTH']:    
        xlist_ASTH.append(T[ii]['La/Pb'])
        ylist_ASTH.append(T[ii]['Ba/Pb'])
    if T[ii]['LM']:
        xlist_LM.append(T[ii]['La/Pb'])
        ylist_LM.append(T[ii]['Ba/Pb'])
# Scatter plot mantle regions
plt.scatter(xlist_ASTH,ylist_ASTH,s=1,lw=0,c='k')
plt.scatter(xlist_LM,ylist_LM,s=1,lw=0,c='k')
plt.scatter(xlist_pool,ylist_pool,s=4,lw=0,c='maroon')
plt.scatter(xlist_TZ,ylist_TZ,s=2,lw=0,c='darkgreen')
# Label axes
plt.xlabel('La138/Pb204')
plt.ylabel('Ba138/Pb204')
plt.show()


#plt.savefig('dummyfile.pdf')
#plt.show()

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

