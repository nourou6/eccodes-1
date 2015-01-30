#!/bin/sh
# Copyright 2005-2015 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# 
# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.
#

. ./include.sh

#set -x


#Enter data dir
cd ${data_dir}/bufr

fLog="bufr_filter.log"
rm -f $fLog

fTmp="tmp.bufr_filter.txt"
rm -f $fTmp

#Create log file
touch $fLog

#-----------------------------------------------------------
# Filter out only header information the all
# the bufr files must have. We just check if it works.
#-----------------------------------------------------------

fFilter="bufr_filter_header.filter"
cat > $fFilter <<EOF
print "[centre] [subCentre] [masterTablesVersionNumber] [localTablesVersionNumber] [numberOfSubsets]"; 
EOF

for f in `ls *.bufr` ; do
   echo "file: $f" >> $fLog
   ${tools_dir}/bufr_filter $fFilter $f >> $fLog
done


rm -f $fLog $res_ls $fTmp