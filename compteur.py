#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

x = 0

while True:
    sys.stdout.write("%08d\r" % x)
    sys.stdout.flush()
    x += 1
