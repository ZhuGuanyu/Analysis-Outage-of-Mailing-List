import os, sys
path = "."
dirs = os.listdir( path )
Nline=""
NNline=""
count = 0
pre_line =""
next_line=""
total_thread = 0
contributer = ""
contributerList = []
for filename in dirs:
	count = 0
	if "20" not in filename:
		continue
	with open(filename, "r") as f:
		lines = f.readlines()
		for index in range(len(lines)):
			if index > 0 and index < len(lines)-1:
				if "From "in lines[index-1] and "From:" in lines[index]:
					contributer = lines[index].split()
					if contributer[1] not in contributerList:
						contributerList.append(contributer[1])
contributerList.sort()
for c in contributerList:
	print c
