import os, sys
path = "."
dirs = os.listdir( path )
count = 0
pword = "99"
for filename in dirs:
	if "New" in filename:
		with open(filename, "r") as f:
			lines = f.readlines()
			for index in range(len(lines)):
				if index > 0:
					word = lines[index].split()
					try:
						if word[0].isdigit() and float(word[0]) < 20:
							if (word[0]==1 or  float(word[0]) < float(pword)) and \
							("ms" in lines[index] or "." in lines[index] or "*" in lines[index]):
								print ("Traceroute # "+ str(count+1))
								count+=1
								pword = word[0]
							if ("ms" in lines[index] or "." in lines[index] or "*" in lines[index]):
								noEnd = lines[index].split("\n")
								print noEnd[0]
								pword = word[0]
					except:
						continue