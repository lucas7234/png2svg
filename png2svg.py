#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Forked by @lucas119, original file by @ianmackinnon
#Using XML SVG Tech

import sys
import logging
import operator
from collections import deque
from StringIO import StringIO
from optparse import OptionParser

import Image
import pngtosvg_functions

parser = OptionParser()
parser.add_option("-v", "--verbose", action="store_true", dest="verbosity", help="Print verbose information for debugging", default=None)
parser.add_option("-q", "--quiet", action="store_false", dest="verbosity", help="Suppress warnings", default=None)
parser.add_option("-p", "--pixels", action="store_false", dest="contiguous", help="Generate a separate shape for each pixel; do not group pixels into contiguous areas of the same colour", default=True)
parser.add_option("-o", "--opaque", action="store_true", dest="opaque", help="Opaque only; do not create shapes for fully transparent pixels. ", default=None)
parser.add_option("-1", "--one", action="store_true", dest="keep_every_point", help="1-pixel-width edges on contiguous shapes; default is to remove intermediate points on straight line edges. ", default=None)

(options, args) = parser.parse_args()

if options.verbosity == True:
    log.setLevel(logging.DEBUG)
elif options.verbosity == False:
    log.setLevel(logging.ERROR)

assert len(args) == 1, "Usage: %s [FILE]"
print png_to_svg(args[0], contiguous=options.contiguous, opaque=options.opaque, keep_every_point=options.keep_every_point)
