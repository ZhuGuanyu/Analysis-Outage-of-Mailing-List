import os, sys
path = "."
dirs = os.listdir( path )
Nline=""
NNline=""
count = 0
pre_line =""
next_line=""
total_thread = 0
t = 0
year = 2006
for filename in dirs:
	count = 0
	if str(year) not in filename  and "New" in filename:
		print (str(year)+" has " + str(t) + " threads." 
		year+=1
		t=0
	if "New" in filename:
		with open(filename, "r") as f:
			lines = f.readlines()
			for line in lines:
				word = line.split()
				if word and word[0]=="END":
					count+=1
					total_thread+=1
					t+=1
		print filename +" has "+ str(count) + " threads."
print "Total_thread = "+str(total_thread)


