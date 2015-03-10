#!~/anaconda/bin

# Made by Samuel Haugland Oct/2014

# chem_postprocess takes input files from chemistry code and produces
# isotope space diagrams

############################################################
#DICTIONARY FOR VERTICIES TO CREATE LINES ON PLOT
############################################################
#X and Y coordinates for verticies of lines on each subplot
############################################################
# Associates X and Y coordinates with a dictionary entry

line_dict = {'x_Nd143_Nd144_Pb206_Pb204' : [17.5, 17.5, 17.5, 22.0, 20.0, 17.5, 17.5, 20.0],
             'y_Nd143_Nd144_Pb206_Pb204' : [5132.5, 5130.0, 5124.0, 5128.5, 5130.0, 5132.5, 5130.0, 5130.0],
             'x_Nd143_Nd144_Sr87_Sr86'   : [0.7028, 0.705, 0.708, 0.704, 0.70225, 0.7028, 0.704],
             'y_Nd143_Nd144_Sr87_Sr86'   : [5128.5, 5124.0, 5127.0, 5130.0, 5132.5, 5128.5, 5130.0],
             'x_Sr87_Sr86_Pb206_Pb204'   : [17.5, 20.0, 22.0, 19.0, 17.5, 17.5, 17.5, 20.0, 17.5],
             'y_Sr87_Sr86_Pb206_Pb204'   : [0.70225, 0.70300, 0.7028, 0.7080, 0.7050, 0.7035, 0.70225, 0.7030, 0.7035],
             'x_Os187_Os188_Pb206_Pb204' : [17.5, 17.5, 17.5, 19.5, 22.0, 20.0, 17.5, 17.5, 20.0],
             'y_Os187_Os188_Pb206_Pb204' : [0.123, 0.132, 0.150, 0.153, 0.150, 0.132, 0.123, 0.132, 0.132],
             'x_Pb208_Pb204_Pb206_Pb204' : [17.5, 18.0, 17.5, 20.0, 22.0, 19.5, 17.5, 18.0, 17.5, 20.0, 18.0],
             'y_Pb208_Pb204_Pb206_Pb204' : [39.0, 38.2, 37.0, 39.0, 40.8, 40.0, 39.0, 38.2, 37.0, 39.0, 38.2],
             'x_Pb207_Pb204_Pb206_Pb204' : [17.5, 17.5, 19.5, 22.0, 19.0, 17.5, 17.5, 19.5, 17.5],
             'y_Pb207_Pb204_Pb206_Pb204' : [15.6, 15.3, 15.5, 15.85, 15.7, 15.6, 15.3, 15.5, 15.6]
            }

###########################################################
#Specify directory where input files are stored.#
###########################################################
input_file_dir = './MODELS/EPSL_2008/trialrun/Plot/'
###########################################################

###########################################################
#Specify directory where STANDARDS are stored.#
###########################################################
standards_dir = './SOURCE/STANDARDS/'
###########################################################

# Import modules
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import subprocess as sp
import datetime

# Make final output into PDF vector format, for use in Adobe Illustrator
matplotlib.use('PDF')

# Run the code "check_files.py" 
sp.call("python check_files.py", shell=True)

# Sets the size of the window
from pylab import *
rcParams['figure.figsize'] = 15, 12

# Define label class
class Marker(object):
   def __init__(self,label,x_coord,y_coord,home):
      self.label = label
      self.x_coord = x_coord
      self.y_coord = y_coord
      self.home = home
      
# Define function 'array_maker' that will turn input files into workable arrays 
def array_maker(text_file):
    Fopen = open(text_file)
    Rfile = Fopen.read()
    Rows = Rfile.split('\n')
    Array = [ii.split() for ii in Rows]
    Array = Array[0:len(Array)-1]
    Output_Array = np.array(Array,float)
    return Output_Array

# Extract mantle component data from standards_dir
Standards_List = ['Nd143_Nd144_Pb206_Pb204',
                  'Sr87_Sr86_Pb206_Pb204',
                  'Os187_Os188_Pb206_Pb204',
                  'Pb208_Pb204_Pb206_Pb204',
                  'Pb207_Pb204_Pb206_Pb204',
                  'Nd143_Nd144_Sr87_Sr86'
                 ]

# Nested dictionary to store instances of marker classes
standards_dict = {}

# Create an instance of the Marker class to create labels for mantle components.
# Store these in nested dictionary

for standardnamedx,standardname in enumerate(Standards_List):
   y = os.listdir(standards_dir)
   standard_sublist = [j for j in y if standardname in j]
   # Outside for loop defines outside element of nested dictionary 
   standards_dict[standardname] = {}
   for jdx,jj in enumerate(standard_sublist):
      standard_label_list = jj.split('_') 
      if 'DMM' in standard_label_list[4]:
         #Must add [0] to end of array maker for standards. Not sure why.
         DMM = array_maker(standards_dir+standard_sublist[jdx])[0]
         DMMclass = Marker('DMM',DMM[0],DMM[1],Standards_List[standardnamedx])
         standards_dict[standardname]['DMM'] = DMMclass
      if 'EM1' in standard_label_list[4]:
         EM1 = array_maker(standards_dir+standard_sublist[jdx])[0]
         EM1class = Marker('EM1',EM1[0],EM1[1],Standards_List[standardnamedx])
         standards_dict[standardname]['EM1'] = EM1class
      if 'EM2' in standard_label_list[4]:
         EM2 = array_maker(standards_dir+standard_sublist[jdx])[0]
         EM2class = Marker('EM2',EM2[0],EM2[1],Standards_List[standardnamedx])
         standards_dict[standardname]['EM2'] = EM2class
      if 'HIMU' in standard_label_list[4]:
         HIMU = array_maker(standards_dir+standard_sublist[jdx])[0]
         HIMUclass = Marker('HIMU',HIMU[0],HIMU[1],Standards_List[standardnamedx])
         standards_dict[standardname]['HIMU'] = HIMUclass

# Main_List is a list of keywords used to search the input files
Main_List = ['Nd143_Nd144_Pb206_Pb204',
             'Sr87_Sr86_Pb206_Pb204',
             'Os187_Os188_Pb206_Pb204',
             'Pb208_Pb204_Pb206_Pb204',
             'Pb207_Pb204_Pb206_Pb204',
             'Nd143_Nd144_Sr87_Sr86'
            ]

# Colorlist is referenced to color mantle regions
colorlist = ['red','green','blue','black']
mantleregime = ['DMM','EM1','EM2','HIMU']

# Outside loop iterates over each keyword
for namesdx,names in enumerate(Main_List):
   print '******Currently working in dataset',namesdx+1,'/',len(Main_List),names
   x = os.listdir(input_file_dir)
   list = [i for i in x if names in i]
# Inside loop iterates over different mantle regions within each keyword
   for idx,ii in enumerate(list):
      temp_array = array_maker(input_file_dir+ii)
      print 'Processing:', ii
      # Split input file by underscore, dictates how to label graph
      Label = ii.split("_")
      if 'TZ' in Label[5]:
         color_index = 0
      elif 'LM' in Label[5]:
         color_index = 1
      elif 'POOL' in Label[5]:
         color_index = 2 
      elif 'ASTH' in Label[5]:
         color_index = 3
      plt.subplot(3,2,namesdx+1)
      plt.scatter(temp_array[:,0],temp_array[:,1],s=1,lw=0,c=colorlist[color_index])
      x_lines = 'x_'+names
      y_lines = 'y_'+names
      plt.plot(line_dict[x_lines], line_dict[y_lines])  
      for mantlenamesdx,mantlenames in enumerate(mantleregime):
         plt.text(standards_dict[names][mantlenames].x_coord,standards_dict \
         [names][mantlenames].y_coord,standards_dict[names][mantlenames].label)
      if 'Nd143' in Label[0]:
         plt.ylabel('1000 x %s/%s'%(Label[0],Label[1]))
         plt.xlabel('%s/%s'%(Label[2],Label[3]))
      else:
         plt.ylabel('%s/%s'%(Label[0],Label[1]))
         plt.xlabel('%s/%s'%(Label[2],Label[3]))
plt.savefig('dummyfile.pdf')
plt.show()

# raw_input returns the empty string for "enter"
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])
date = set(['date','d'])
name = set(['name', 'n'])

# Give the user options about how to save figure. The user can choose to not save
# The file, save it with an inputed name, or save the file as

print "Do you like this figure? Should I save it?"
choice = raw_input("Enter yes or no --->").lower()

if choice in yes:
   print "Name by date/time or Name yourself?"
   namechoice = raw_input("Enter 'date' or 'name' --->").lower()

   if namechoice in date:
      dt = str(datetime.datetime.now())
      os.rename("dummyfile.pdf", dt+'.pdf')
   else:
      os.rename("dummyfile.pdf", namechoice+".pdf")

elif choice in no:
   print "Hope the next one looks better"
   sp.call("rm dummyfile.pdf", shell=True) 

else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
