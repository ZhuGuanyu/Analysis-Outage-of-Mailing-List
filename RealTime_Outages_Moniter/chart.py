"""
Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt
import os,sys



total = 50.0
num = [0,0,4,7,0,5,2,3,0,7,0,0,22]
sizes = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

with open("2015_data.txt", "r") as f:
    data = f.read().splitlines()


total = int(data[0])

for index in range(13):
	num[index] = int(data[index+1])

if int(sys.argv[1]) != 14:
	output = open("2015_data.txt", "w")
	num[int(sys.argv[1])-1] += 1
	total += 1
	output.write(str(total)+'\n')
	for index in range(13):
		output.write(str(num[index])+'\n')
	output.close()
	

sizes_show = []
labels_show = []
colors_show = []
explode_show = []

# The slices will be ordered and plotted counter-clockwise.
labels = 'Natural disaster', 'Censorship', 'Attacks', 'Maintenance',  'Device failure', 'Fiber cut','Power outage','Server','Human Error', 'Routing', 'Congestion','DNS resolution','Mobile network'
for index in range(len(num)):
	sizes[index] = float(num[index]*1.0) * float(100.0/total*1.0)
	print sizes[index]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','violet','coral','Green','LightSeaGreen', 'steelblue' , 'cornsilk' ,'snow', 'gainsboro' ,'moccasin']
explode = (0, 0, 0, 0,0,0,0,0,0,0,0,0,0) # only "explode" the 2nd slice (i.e. 'Hogs')

for index in range(13):
	if sizes[index]:
		sizes_show.append(sizes[index])
		labels_show.append(labels[index])
		colors_show.append(colors[index])
		explode_show.append(explode[index])

plt.pie(sizes_show, explode=explode_show, labels=labels_show, colors=colors_show,
        autopct='%0.2f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.savefig("pie")
os.system("mv ./pie.png /Users/Guanyu/Website/octopress/source/images/pie.png")

print "Begin Posting to Our Website: http://zhuguanyu.github.io/fundamental_of_network/realtime/"
os.chdir("/Users/Guanyu/Website/octopress/")
os.system("rake generate")
os.system("rake deploy")
print "The outage prediction has been posted to the website."

plt.show()