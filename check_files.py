############### Samuel Haugland October 2014 ################################

# This code checks to make sure you have all of the executables, f.90 files, etc.
# It gives you error messages if any file is missing

import os

# The following "*_LIST" entries indicate what files 'SHOULD' be in the directories

BIN_LIST = ['chempost',
            'gridit'
           ]

UTIL_LIST =['plot_allchem',
            'prep_geochem',
            'run_geochem'
           ]

Chempost_LIST = ['arrays_mod.f90',
        'averageC.f90',
        'chempost.f90',
        'control_mod.f90',
        'decay_mod.f90',
        'init_continent.f90',
        'initchem.f90',
        'logical_units_mod.f90',
        'output_to_file.f90',
        'partmelt.f90',
        'process.f90',
        'readchem.f90',
        'readlog.f90',
        'readtime.f90',
        'sedinput.f90',
        'sedtrac_mod.f90',
        'startup.f90',
        'types_mod.f90',
        'wrapup.f90'
                ]

GridIt_LIST = ['PbAge.f90',
        'allocate_grid_arrays_and_zero.f90',
        'arrays_mod.f90',
        'averageC.f90',
        'control_mod.f90',
        'divgrid_mod.f90',
        'error_handler.f90',
        'grid_setup.f90',
        'gridit.f90',
        'location_output.f90',
        'logical_units_mod.f90',
        'make_div.f90',
        'rav.f90',
        'readdata.f90',
        'startup.f90',
        'tracplot.f90',
        'tractocell.f90',
               ]

# Just store the path directories convieniently as variable names here:

bin_path = "./BIN/"
chempost_path = "./SOURCE/Chempost/"
gridit_path = "./SOURCE/GridIt/"
list_util = "./MODELS/EPSL_2008/UTIL/"

# The "os.*" commands are python's way of listing the contents of the directories
# And storing them in arrays

list_bin = os.listdir(bin_path)
list_chempost = os.listdir(chempost_path)
list_gridit = os.listdir(gridit_path)
list_util = os.listdir(list_util)

# These for loops determine if the files in the os.listdir arrays are also in the "*_LIST"
# arrays. If a file is missing, it will print an error message. If not, an "all clear"
# message.

for i in BIN_LIST:
    if not i in list_bin: print "********WARNING!!******** The executable", i, "is not in", bin_path
    else: print "The executable", i,"is in DISTRIBUTION/BIN/ where it sould be"
    
for i in Chempost_LIST:
    if not i in list_chempost: print "********WARNING!!******** The file", i, "is not in", chempost_path 
    else: print "The executable", i,"is in DISTRIBUTION/SOURCE/Chempost/ where it sould be"

for i in GridIt_LIST:
    if not i in list_gridit: print "********WARNING!!******** The file", i, "is not in", gridit_path 
    else: print "The executable", i,"is in DISTRIBUTION/SOURCE/Gridit/ where it sould be"

for i in UTIL_LIST:
    if not i in list_util: print "********WARNING!!******** The file", i, "is not in", list_util
    else: print "The executable", i,"is in DISTRIBUTION/SOURCE/Gridit/ where it sould be"

