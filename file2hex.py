#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
for current_byte in list(open('example.txt','rb').read()):
    print hex(struct.unpack("B",current_byte)[0]),