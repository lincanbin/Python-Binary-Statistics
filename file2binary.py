#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct, os
filename = 'example.txt'
byte_list = list(open(filename,'rb').read())
for key in range(0, os.path.getsize(filename)):
    print "%08d " % int(bin(struct.unpack("B", byte_list[key])[0]).replace("0b","")),
    print "\n" if (key+1)%5 == 0 else "",