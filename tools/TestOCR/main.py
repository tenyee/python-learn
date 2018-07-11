#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
功能：
提取目录下的图片文件到一个指定的根目录，保留文件的所在目录路径
'''
import os
import re
import shutil

gRoot = r'C:\Users\vmp\czw\python-learn'
gPattern = '.png|.jpg|.bmp'
gDir = 'pic'
#图片转存根目录 
gTarget = r'C:\Users\vmp\czw\python-learn\tools\TestOCR\pic'
print("所有图片将转存到此根目录：", gTarget)

def GetImagePaths(root):
	files = []

	for fpath, dirs, flist in os.walk(root, topdown=True):
		for i in flist:
			path = os.path.join(fpath, i)
			tmp = {}
			tmp["dir"] = fpath
			tmp["name"] = i
			files.append(tmp)

	return files

def CheckImages(path, types):
	match = re.search(r'({0})$'.format(types), path)
	if match != None:
		return True
	else:
		return False

if os.path.exists(gTarget):
	shutil.rmtree(gTarget)

files = GetImagePaths(gRoot)
for i in files:
	filePath = os.path.join(i["dir"], i["name"])
	if CheckImages(filePath, gPattern):
		dir = i["dir"]
		targetDir = dir.replace(gRoot, gTarget)
		if not os.path.exists(targetDir):
			os.makedirs(targetDir)
		targetPath = os.path.join(targetDir, i["name"])
		shutil.copy(filePath, targetPath)


