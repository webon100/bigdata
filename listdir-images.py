__author__ = 'webon'

import glob
#for file in glob.glob("C:/Users/webon/Desktop/loan-officer-images/*.jpg"):
#for file in glob.glob("C:/Python27/Scripts/*.py"):
for file in glob.glob("http://www.lhfs.com/sfdc_images/pics/"):   #seems not work this way
#for file in glob.glob("http://www.lhfs.com/sfdc_images/pics/*.jpg"):
    print (file)