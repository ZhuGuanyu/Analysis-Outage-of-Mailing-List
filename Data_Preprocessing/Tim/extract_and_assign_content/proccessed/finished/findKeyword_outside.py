import os, sys
path = "."
dirs = os.listdir( path )
Nline=""
NNline=""
count = 0
pre_line =""
next_line=""
total_thread = 0
#=============Content providers================
yahoo = 0
totalyahoo = 0
netflix = 0
totalNetflix = 0
amazon = 0
totalAmazon = 0
fb = 0
totalFb = 0
google = 0
totalGoogle = 0
microsoft=0
totalMicrosoft=0
#=============ISPs================
att=0
totalATT=0
verison=0
totalVerison=0
sprint=0
totalSprint=0
comcast=0
totalcomcast=0
cogent=0
totalCogent=0
l3=0
totalL3=0
#=============Attacks================
ddos=0
totalDDos=0
hijack = 0
totalhijack = 0
virus=0
totalvirus=0
spam=0
totalspam=0
botnet=0
totalbotnet=0
#============Protocol================
bgp=0
totalbgp=0
dns=0
totaldns=0
icmp=0
totalicmp=0
ipv6=0
totalipv6=0
tcp=0
totaltcp=0
#=========== Type of outage ===================
routing = 0
totalRouting = 0

year = 2006
for filename in dirs:
	if filename == "Readme" or filename == "count_thread.py" or filename == "intergratedThreads.txt"\
	or filename == "tt" or filename == "test.py" or filename==".DS_Store" or filename == "findKeyword_outside.py":
		continue
	if str(year) not in filename and "New" in filename:
			year+=1
			print("################# CPs ###################")
			print(str(year-1) + " Yahoo = " + str(yahoo) + " Percentage = " + str(float(yahoo)/float(count)))
			print(str(year-1) + " Netflix = " + str(netflix) + " Percentage = " + str(float(netflix)/float(count)))
			print(str(year-1) + " Facebook = " + str(fb) + " Percentage = " + str(float(fb)/float(count)))
			print(str(year-1) + " Amazon = " + str(amazon) + " Percentage = " + str(float(amazon)/float(count)))
			print(str(year-1) + " Google = " + str(google) + " Percentage = " + str(float(google)/float(count)))
			print(str(year-1) + " Microsoft = " + str(microsoft) + " Percentage = " + str(float(microsoft)/float(count)))
			print("################### ISPs #####################")
			print(str(year-1) + " AT&T = " + str(att) + " Percentage = " + str(float(att)/float(count)))
			print(str(year-1) + " Verison = " + str(verison) + " Percentage = " + str(float(verison)/float(count)))
			print(str(year-1) + " Sprint = " + str(sprint) + " Percentage = " + str(float(sprint)/float(count)))
			print(str(year-1) + " Comcast = " + str(comcast) + " Percentage = " + str(float(comcast)/float(count)))
			print(str(year-1) + " Cogent = " + str(cogent) + " Percentage = " + str(float(cogent)/float(count)))
			print(str(year-1) + " Level-3 = " + str(l3) + " Percentage = " + str(float(l3)/float(count)))
			print("################# Attacks ###################")
			print(str(year-1) + " DDos = " + str(ddos) + " Percentage = " + str(float(ddos)/float(count)))
			print(str(year-1) + " Hijack = " + str(hijack) + " Percentage = " + str(float(hijack)/float(count)))
			print(str(year-1) + " Virus = " + str(virus) + " Percentage = " + str(float(virus)/float(count)))
			print(str(year-1) + " Spam = " + str(spam) + " Percentage = " + str(float(spam)/float(count)))
			print(str(year-1) + " Botnet = " + str(botnet) + " Percentage = " + str(float(botnet)/float(count)))
			print("################# Protocol ###################")
			print(str(year-1) + " BGP = " + str(bgp) + " Percentage = " + str(float(bgp)/float(count)))
			print(str(year-1) + " DNS = " + str(dns) + " Percentage = " + str(float(dns)/float(count)))
			print(str(year-1) + " ICMP = " + str(icmp) + " Percentage = " + str(float(icmp)/float(count)))
			print(str(year-1) + " IPv6 = " + str(ipv6) + " Percentage = " + str(float(ipv6)/float(count)))
			print(str(year-1) + " TCP = " + str(tcp) + " Percentage = " + str(float(tcp)/float(count)))
			
			totalAttack = totalDDos + totalhijack + totalvirus + totalspam + totalbotnet
			print(str(year-1) + " Attack percentage = " + str(float(totalAttack/(count))))

			print (str(year-1) +" has "+ str(count) + " threads.")
			print("\n")
			print(year)

			totalDDos+=ddos
			totalL3+=l3
			totalMicrosoft+=microsoft
			totalCogent+=cogent
			totalcomcast+=comcast
			totalSprint+=sprint
			totalATT+=att
			totalAmazon+=amazon
			totalyahoo+=yahoo
			totalNetflix+=netflix
			totalFb+=fb
			totalGoogle+=google
			totalVerison+=verison
			totalhijack+=hijack
			totalvirus+=virus
			totalspam+=spam
			totalbotnet+=botnet
			totalbgp+=bgp
			totaldns+=dns
			totalicmp+=icmp
			totalipv6+=ipv6
			totaltcp+=tcp


			ddos=0
			l3=0
			microsoft=0
			cogent=0
			comcast=0
			sprint=0
			verison=0
			att=0
			yahoo = 0
			netflix = 0
			fb=0
			amazon=0
			google=0
			hijack=0
			virus=0
			spam=0
			botnet=0
			bgp=0
			dns=0
			icmp=0
			ipv6=0
			tcp=0

			count = 0
	with open(filename, "r") as f:
		lines = f.readlines()
		for index in range(len(lines)):
			if index > 0 and index < len(lines)-1:
				if lines[index-1] == "###############################################################\n"\
				and lines[index+1] == "###############################################################\n":
					if "Yahoo" in lines[index] or "yahoo" in lines[index]:
						yahoo+=1	
					if "Netflix" in lines[index] or "netflix" in lines[index]:
						netflix+=1
					if "Facebook" in lines[index] or "facebook" in lines[index]:
						fb+=1
					if "Amazon" in lines[index] or "amazon" in lines[index]:
						amazon+=1
					if "Google" in lines[index] or "google" in lines[index]:
						google+=1
					if "AT&T" in lines[index] or "ATT" in lines[index] or "at&t" in lines[index] or "att" in lines[index]:
						att+=1
					if "Verizon" in lines[index] or "verizon" in lines[index]:
						verison+=1
					if "Sprint" in lines[index] or "sprint" in lines[index]:
						sprint+=1
					if "Comcast" in lines[index] or "comcast" in lines[index]:
						comcast+=1
					if "Cogent" in lines[index] or "cogent" in lines[index]:
						cogent+=1
					if "Microsoft" in lines[index] or "microsoft" in lines[index]:
						microsoft+=1
					if "Level-3" in lines[index] or "level-3" in lines[index] or \
					"Level 3" in lines[index] or "level 3" in lines[index] or "L3" in lines[index] or \
					"Level3" in lines[index] or "level3" in lines[index]: 
						l3+=1
					if "DDos" in lines[index] or "ddos" in lines[index] or \
					"Dos" in lines[index] or "dos" in lines[index] or "DDOS" in lines[index] or\
					"Ddos" in lines[index] or "DDoS" in lines[index]:
						ddos+=1
					if "Hijack" in lines[index] or "hijack" in lines[index]:
						hijack+=1
					if "Virus" in lines[index] or "virus" in lines[index]:
						virus+=1
					if "Spam" in lines[index] or "spam" in lines[index]:
						spam+=1
					if "Botnet" in lines[index] or "botnet" in lines[index]:
						botnet+=1
					if "BGP" in lines[index] or "bgp" in lines[index]:
						bgp+=1
					if "DNS" in lines[index] or "dns" in lines[index]:
						dns+=1
					if "ICMP" in lines[index] or "icmp" in lines[index]:
						icmp+=1
					if "IPv6" in lines[index] or "ipv6" in lines[index]:
						ipv6+=1
					if "TCP" in lines[index] or "tcp" in lines[index]:
						tcp+=1
				if lines[index-1] == "###############################################################\n"\
				and lines[index+1] == "###############################################################\n"\
				and "END" in lines[index]:
					count+=1
	'''
	print filename +" has "+ str(count) + " threads."
	'''
#2015
print("################# CPs ###################")
print(str(year) + " Yahoo = " + str(yahoo) + " Percentage = " + str(float(yahoo)/float(count)))
print(str(year) + " Netflix = " + str(netflix) + " Percentage = " + str(float(netflix)/float(count)))
print(str(year) + " Facebook = " + str(fb) + " Percentage = " + str(float(fb)/float(count)))
print(str(year) + " Amazon = " + str(amazon) + " Percentage = " + str(float(amazon)/float(count)))
print(str(year) + " Google = " + str(google) + " Percentage = " + str(float(google)/float(count)))
print(str(year) + " Microsoft = " + str(microsoft) + " Percentage = " + str(float(microsoft)/float(count)))
print("################# ISPs ###################")
print(str(year) + " AT&T = " + str(att) + " Percentage = " + str(float(att)/float(count)))
print(str(year) + " Verison = " + str(verison) + " Percentage = " + str(float(verison)/float(count)))
print(str(year) + " Sprint = " + str(sprint) + " Percentage = " + str(float(sprint)/float(count)))
print(str(year) + " Comcast = " + str(comcast) + " Percentage = " + str(float(comcast)/float(count)))
print(str(year) + " Cogent = " + str(cogent) + " Percentage = " + str(float(cogent)/float(count)))
print(str(year) + " Level-3 = " + str(l3) + " Percentage = " + str(float(l3)/float(count)))
print("################# Attacks ###################")
print(str(year) + " DDos = " + str(ddos) + " Percentage = " + str(float(ddos)/float(count)))
print(str(year) + " Hijack = " + str(hijack) + " Percentage = " + str(float(hijack)/float(count)))
print(str(year) + " Virus = " + str(virus) + " Percentage = " + str(float(virus)/float(count)))
print(str(year) + " Spam = " + str(spam) + " Percentage = " + str(float(spam)/float(count)))
print(str(year) + " Botnet = " + str(botnet) + " Percentage = " + str(float(botnet)/float(count)))
print("################# Protocols ###################")
print(str(year) + " BGP = " + str(bgp) + " Percentage = " + str(float(bgp)/float(count)))
print(str(year) + " DNS = " + str(dns) + " Percentage = " + str(float(dns)/float(count)))
print(str(year) + " ICMP = " + str(icmp) + " Percentage = " + str(float(icmp)/float(count)))
print(str(year) + " IPv6 = " + str(ipv6) + " Percentage = " + str(float(ipv6)/float(count)))
print(str(year) + " TCP = " + str(tcp) + " Percentage = " + str(float(tcp)/float(count)))

print (str(year) +" has "+ str(count) + " threads.")

print "============== Content Providers ==============="
print "Yahoo = " + str(totalyahoo)
print "Netflix = " + str(totalNetflix)
print "Facebook = " + str(totalFb)
print "Amazon = " + str(totalAmazon)
print "Google = " + str(totalGoogle)
print "Microsoft = " + str(totalMicrosoft)
print "==============	ISPs	==============="
print "AT&T = " + str(totalATT)
print "Verizon = " + str(totalVerison)
print "Sprint = " + str(totalSprint)
print "Comcast = " + str(totalcomcast)
print "Cogent = " + str(totalCogent)
print "Level-3 = " + str(totalL3)
print "==============	Attacks	==============="
print "DDos = " + str(totalDDos)
print "Hijack = " + str(totalhijack)
print "Virus = " + str(totalvirus)
print "Spam = " + str(totalspam)
print "Botnet = " + str(totalbotnet)
print "==============	Protocol ==============="
print "BGP = " + str(totalbgp)
print "DNS = " + str(totaldns)
print "ICMP = " + str(totalicmp)
print "IPv6 = " + str(totalipv6)
print "TCP = " + str(totaltcp)

'''
if lines[index-1] == "###############################################################\n"\
and lines[index+1] == "###############################################################\n":

if lines[index-1] == "###############################################################\n"\
and lines[index+1] == "###############################################################\n"\
and "END" in lines[index]:
'''



