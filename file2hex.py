#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct, os
filename = 'example.txt'
byte_list = list(open(filename,'rb').read())
for key in range(0, os.path.getsize(filename)):
    print hex(struct.unpack("B", byte_list[key])[0]).ljust(4,' '),
    print "\n" if (key+1)%10 == 0 else "",