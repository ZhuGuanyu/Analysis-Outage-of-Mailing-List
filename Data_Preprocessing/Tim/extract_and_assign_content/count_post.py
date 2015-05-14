import os, sys

path = "outages/"
dirs = os.listdir(path)
total_count = 0
total_count2 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0

reply6 = 0
reply7 = 0
reply8 = 0
reply9 = 0
reply10 = 0
reply11 = 0
reply12 = 0
reply13 = 0
reply14 = 0
reply15 = 0

for filename in dirs:
	count = 0
	count2 = 0
	with open(path+filename, "r") as f:
		lines = f.readlines()
		for line in lines:	
			word = line.split(" ")
			if word and word[0] == "Message-ID:":
				if "2006" in filename:
					count6+=1
				elif "2007" in filename:
					count7+=1
				elif "2008" in filename:
					count8+=1
				elif "2009" in filename:
					count9+=1
				elif "2010" in filename:
					count10+=1
				elif "2011" in filename:
					count11+=1
				elif "2012" in filename:
					count12+=1
				elif "2013" in filename:
					count13+=1
				elif "2014" in filename:
					count14+=1
				elif "2015" in filename:
					count15+=1
				count+=1
			if word and word[0] == "In-Reply-To:":
				if "2006" in filename:
					reply6+=1
				elif "2007" in filename:
					reply7+=1
				elif "2008" in filename:
					reply8+=1
				elif "2009" in filename:
					reply9+=1
				elif "2010" in filename:
					reply10+=1
				elif "2011" in filename:
					reply11+=1
				elif "2012" in filename:
					reply12+=1
				elif "2013" in filename:
					reply13+=1
				elif "2014" in filename:
					reply14+=1
				elif "2015" in filename:
					reply15+=1
				count2+=1
		print(filename+ " has " + str(count) + " posts.")
		print(filename+ " has " + str(count2) + " replies.")
		total_count +=count
		total_count2 +=count2
print("Total posts = " + str(total_count))
print("Total replies = " + str(total_count2))
print("2006 posts = " + str(count6))
print("2007 posts = " + str(count7))
print("2008 posts = " + str(count8))
print("2009 posts = " + str(count9))
print("2010 posts = " + str(count10))
print("2011 posts = " + str(count11))
print("2012 posts = " + str(count12))
print("2013 posts = " + str(count13))
print("2014 posts = " + str(count14))
print("2015 posts = " + str(count15))

print("2006 replies = " + str(reply6))
print("2007 replies = " + str(reply7))
print("2008 replies = " + str(reply8))
print("2009 replies = " + str(reply9))
print("2010 replies = " + str(reply10))
print("2011 replies = " + str(reply11))
print("2012 replies = " + str(reply12))
print("2013 replies = " + str(reply13))
print("2014 replies = " + str(reply14))
print("2015 replies = " + str(reply15))
'''
In-Reply-To:
'''