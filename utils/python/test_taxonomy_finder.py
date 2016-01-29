#!/usr/bin/python
import sys
sys.path.append('./utils')
import taxonomy_finder

filename = sys.argv[1]
taxonomy_finder.full(filename)
