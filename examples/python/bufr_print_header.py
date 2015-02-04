# Copyright 2005-2015 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import traceback
import sys

from eccodes import *

INPUT='../../data/bufr/syno_multi.bufr'
VERBOSE=1 # verbose error reporting
    
def example():
    f = open(INPUT)

    keys = [
        'dataCategory',
        'dataSubCategory',
        'typicalDate',
        'centre',
        'subCentre',
        'masterTablesVersionNumber',
        'localTablesVersionNumber',
        'numberOfSubsets',
        ]
        
    cnt=0    
    while 1:
        gid = codes_bufr_new_from_file(f)
        if gid is None: break

        print "message: %s" % cnt

        for key in keys:
            if not codes_is_defined(gid,key): raise Exception("Key was not defined")
            print '  %s: %s' % (key,codes_get(gid,key))

        cnt+=1

        codes_release(gid)

    f.close()

def main():
    try:
        example()
    except CodesInternalError,err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            print >>sys.stderr,err.msg

        return 1

if __name__ == "__main__":
    sys.exit(main())