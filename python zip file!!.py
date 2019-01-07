'''
Created on 2010/12/20


0 Mon Dec 20 15:36:05 2010
0 Mon Dec 20 15:36:08 2010
0 Mon Dec 20 15:36:10 2010
1 Mon Dec 20 15:36:12 2010
0 Mon Dec 20 15:36:14 2010
0 Mon Dec 20 15:36:16 2010

@author: panda.huang
'''
#   <?xml version="1.0" encoding="US-ASCII"?>
#    <testsuite tests="2" time="" failures="1" error="0" name="[09-07][16-44-18][device_list_1]]">
#      <testcase time="0.0 sec" result="fail" name="test_db_1">
#        <failure message="FAIL !!"/>
#      </testcase>
#      <testcase time="2.0 sec" result="pass" name="test_db">
#      </testcase>
#    </testsuite>

import os
import zipfile
from zipfile import ZipFile 
if __name__ == '__main__':
    pass


#os.chdir("G:\\")
#zip1 = zipfile.ZipFile('G.zip', 'w')
#zip1.write('test1.pdf' , compress_type=zipfile.ZIP_DEFLATED)
#zip1.close()

    
zf = ZipFile('G:\\G.zip', 'r')
zf.extractall('H:\\G')
zf.close()

print("Completed")
    
#https://www.youtube.com/watch?v=5vkjXZ6RtFg
#https://stackoverflow.com/questions/3451111/unzipping-files-in-python

#define
#testsuite

#testcase time result name
#failure message

#testsuite