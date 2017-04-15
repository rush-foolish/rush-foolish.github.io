#####################################################
#	File Name: _gen_mdindex.py
#	Author: Rachel Liu
#	Created Time: 2017-04-14
#	Description: 
#	
#	Modified History: 
#	
#	Copyright (C)2017 All Rights Reserved
#####################################################
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
#markdown index content
content = ""

def walkdir(dir,n=1):	# walk through dir and return the markdown content

	global content
	
	dirlist = os.listdir(dir)	#return the files list in specific directory
	for l in dirlist:
		path = os.path.join(dir,l)
		if l.startswith((".","_")):	#check if the file/dir contains the prefix ./_
			continue
		elif os.path.isdir(path):	#if dir, continue to scan the following contents
			#print("====%d=is dir===="%(n))
			dline = "\t"*(n-1) + "#"*(n+2) + " "+ l + "\n"
			content += dline 
			#print(content)
			walkdir(path,n+1)
		elif ( (n != 1) and os.path.isfile(path) ):	#if file, create the link
			#print(n)
			fname = os.path.splitext(l)[0]
			fline = "\t"*(n-2) + ("- [%s](%s)" % (fname,path)) + "\n"
			content += fline
	
	#print(n)
	if n == 1:
		return content

def createFile(fname,ftxt):
	print(fname)
	f = open(fname,'w')
	
	f.write(ftxt)
	f.close()

header = "## Welcome to R's Blog \n\
> The Harder, the Luckier\n\n\
## Index\n\n\
---\n"
footer = "\n---\n\
Actually, miscellaneous notes rather than blog...\n"

rootdir = "."
text = walkdir(rootdir)
ftxt = header+text+footer
createFile("index.md",ftxt)
