import os,sys
import math 
import string
import re


with open("stop_words_en.txt", "r") as f:
    stop_words = f.read().splitlines()

with open("test.txt", "r") as f:
    data = f.read().splitlines()

output = open("result.txt", 'w')

print "Begin load data"
for i in range(len(data)):
    row = data[i]
    word = re.findall(r"[\w']+|[.,!?;]",row)
    #word = row.split()  # as default using the ' ' to split item
    for j in range(len(word)):
        if (word[j] not in stop_words) and (word[j] not in string.punctuation) and word[j].isdigit()==False:
            output.write(word[j]+" ")
    output.write("\n")

output.close()
print "End"
