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
# walk through dir and return the markdown content
def walkdir(dir,n=1):	

	global content
	#return the files list in specific directory
	dirlist = os.listdir(dir)	
	for l in dirlist:
		path = os.path.join(dir,l)
		#check if the file/dir contains the prefix ./_
		if l.startswith((".","_")):	
			continue
		#if dir, continue to scan the following contents
		elif os.path.isdir(path):
			sign = "- "
			dline = "\n" + "\t"*(n-2) + sign + "**" + l + "**\n"
			if n == 1:
				sign = "### "
				dline = "\n" + sign + l +"\n"
			content += dline 
			walkdir(path,n+1)
		elif ( (n != 1) and os.path.isfile(path) ):	#if file, create the link
			fname = os.path.splitext(l)[0]
			fline = "\t"*(n-2) + ("- [%s](%s)" % (fname,path)) + "\n"
			content += fline
	
	#print(n)
	if n == 1:
		return content

def createFile(fname,ftxt):
	f = open(fname,'w')
	
	f.write(ftxt)
	f.close()

header = "## Welcome to R's Blog \n\
> The Harder, the Luckier... >>go to my [**GITHub**](https://github.com/rush-foolish) page\n\n\
## Index\n\n\
---\n"
footer = "\n---\n\
Actually, miscellaneous notes rather than blog...\n"

rootdir = "."
text = walkdir(rootdir)
ftxt = header+text+footer
createFile("index.md",ftxt)
