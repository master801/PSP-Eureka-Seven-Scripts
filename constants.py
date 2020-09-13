#!/usr/bin/env python3

import sys

if sys.platform == 'linux':
    FILE_PATH_SEPARATOR = '/'
    pass
else:
    FILE_PATH_SEPARATOR = '\\'
    pass

HEADER = b'\x74\xD6\x40\x00'


class Entry:

    def __init__(self, offset, len_, path, idk1, idk2, idk3, idk4, idk5, idk6, idk7, idk8, idk9, idk10, idk11, idk12,
                 idk13, idk14, idk15, idk16, idk17):
        self.offset = offset
        self.len_ = len_
        self.path = path
        self.idk1 = idk1
        self.idk2 = idk2
        self.idk3 = idk3
        self.idk4 = idk4
        self.idk5 = idk5
        self.idk6 = idk6
        self.idk7 = idk7
        self.idk8 = idk8
        self.idk9 = idk9
        self.idk10 = idk10
        self.idk11 = idk11
        self.idk12 = idk12
        self.idk13 = idk13
        self.idk14 = idk14
        self.idk15 = idk15
        self.idk16 = idk16
        self.idk17 = idk17
        return
