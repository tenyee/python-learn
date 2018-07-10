#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import shutil

gRoot = '/Users/tenyee/workspace/2018/prj-python-learn'
gPattern = '.png|.jpg|.bmp'
gDir = './pic'

def GetImagePaths(root):
	files = []
	for fpath, dirs, flist in os.walk(root, topdown=True):
		for i in flist:
			path = os.path.join(fpath, i)
			files.append(path)
	return files

def CheckImages(path, types):
	match = re.search(r'({0})$'.format(types), path)
	if match != None:
		return True
	else:
		return False

if os.path.exists(gDir):
	shutil.rmtree(gDir)

os.mkdir(gDir)

files = GetImagePaths(gRoot)
for i in files:
	if CheckImages(i, gPattern):
		shutil.copy(i, gDir)






