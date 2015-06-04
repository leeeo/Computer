import sys
#import os

print('The command line arguments are:')
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'
#print os.getcwd()

#11.2. from import 문
from math import  sqrt
print "Square root f 16 is", sqrt(16)