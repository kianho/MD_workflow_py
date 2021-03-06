#!/usr/bin/env python

import os
import sys 
import json
from collections import OrderedDict

lib_path = os.path.abspath('../../mdwf_lib')
sys.path.append(lib_path)
import mdwf_functions as mdwf

""" A python script to help setup the optimization phase of a MD simulation."""

jobid   = sys.argv[1]
jobtype = sys.argv[2]

def main():
    # open and modify local job details file. 
    ljdf_t = mdwf.read_local_job_details_file(".", "local_job_details.json")
    ljdf_t['CurrentJobId'] = jobid
    ljdf_t['JobStatus'] = 'submitted'
    if "opt" in jobtype:
        ljdf_t["RunCountDown"] = ljdf_t["TotalRuns"]



    with open("local_job_details.json", 'w') as outfile:
        json.dump(ljdf_t, outfile, indent=2)
    outfile.close()


    # check Ok for job to run:
#    mdwf.check_disk_quota(ljdf["Account"],ljdf["DiskSpaceCutoff"])
#    mdwf.check_for_pausejob()
    
    # initialize job counter if optimize flag set.  
    
if __name__ == "__main__":
    main()


'''
#!/usr/bin/env python

#!/usr/bin/env python

import sys
from ../mdwf_lib import mdwf_functions as mdwf

""" A python script to post process data files after a MD simulation."""

jobid   = argv[2]
jobtype = argv[3]

def main():

    # initialize job counter if optimize flag set.  
    if not "optimize" in jobtype:
        ljdf["RunCountDown"] = ljdf["TotalRuns"]




if __name__ == "__main__":
    main()

'''

