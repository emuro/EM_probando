# python3
# ################################################################## #
# 
# Author: Enrique M. Muro
# ################################################################## #
#
# ------------------------------------------------------------------------
# Idea: get all the subdirectories (only final leaves) given a root-path
#
# Use a lib from project geneLength project (C) Jan-2021 Mainz.
# Using the next modul:
#   os_utils.py # @ /home/emuro/git/github/geneLength/lib/
#
import os
import sys
from time import time
sys.path.append('/home/emuro/git/github/geneLength/lib/')
from lib import os_utils


# MAIN CODE
###########
def main():
    start_time = time()

    # search leave' subdirs from root
    #################################
    BOOL_SEARCH_LEAVE_SUBDIRS = 1
    if BOOL_SEARCH_LEAVE_SUBDIRS:
        current_path="/media/emuro/Wes/data/compressed/"
        current_path = current_path + "ftp.ensemblgenomes.org/pub/plants/release-49/gtf"
        path_leave_dirs=[]
        os_utils.recursiveSearch_leave_subdirs(current_path, path_leave_dirs) #output in path_list
        print("_"*40)
        #
        leave_dirs=[]
        for p in path_leave_dirs:
            leave_dirs.append(os.path.basename(p)) # basename get dir-name and not its path
        print(leave_dirs)
        print("there are",len(leave_dirs),"leave dirs")

    # Show the time the process took
    ################################
    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds" % elapsed_time)

if __name__ == "__main__":
    main()
