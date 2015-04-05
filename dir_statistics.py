#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct, os
count_one, count_filesize = 0, 0
def count_dir(dirname):
    for parent, dirnames, filenames in os.walk(dirname):
        for current_filename in filenames:
            count_file(os.path.join(parent,current_filename)) #Count the number of 1 and 0 in current binary file. 
        for current_dirname in dirnames:
            count_dir(os.path.join(parent, current_dirname))  #Recursive
def count_file(filename):
    global count_one, count_filesize
    for current_byte in list(open(filename, 'rb').read()):
        count_one += bin(struct.unpack("B", current_byte)[0]).count('1')
    count_filesize += os.path.getsize(filename)
    print filename + '\nSize: ' + str(os.path.getsize(filename) * 8) + ' Bits\n'
if __name__ == '__main__':
    count_dir('C:\\Python27')
    print '\n\n\nResult: \n\nSize: ' + str(count_filesize*8) + ' Bits\nOne:  ' + str(count_one) + ' times\nZero: ' + str(count_filesize * 8 - count_one) + ' times\nOne/Zero: ' + str(float(count_one) / float(count_filesize * 8 - count_one))