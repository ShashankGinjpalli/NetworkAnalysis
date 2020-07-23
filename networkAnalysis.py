import os
import json
import time
import matplotlib.pyplot as plt
import sys


downSpeed = []
upSpeed = []
packetLoss = []
latency = []
timeStamps = []

argument = sys.argv[1]

plot = True

if (argument == 'False'):
	plot = False




if(not plot):

	while True:
		os.system('speedtest -p yes -f json-pretty -s 12818 > output.json')
		

		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		print(current_time)

		with open('output.json') as json_file:
			data = json.load(json_file)
			print(data)
			with open('data.txt', 'a') as outfile:
				if('type' in data.keys()):
					if(data['type'] == "result"):
						outfile.write(str(current_time) + ',' +  str(data["ping"]
								["latency"]) +','+ str(data["download"]["bandwidth"]) +',' + str(data["upload"]["bandwidth"]) +',' + str(data["packetLoss"]) + "\n")
				else:
					outfile.write(str(current_time) + ',' + '0,0,0,100' + "\n")

		print("Sleeping for 10 minutes")
		time.sleep(1200)

else:
	reading = 1
	with open('data.txt', 'r') as infile:
		for line in infile:
			print(line)
			l = line.split(",")
			timeStamps.append(l[0])
			latency.append(float(l[1]))
			downSpeed.append(int(l[2])/125000)
			upSpeed.append(int(l[3])/125000)
			packetLoss.append(float(l[4]))

	fig, axs = plt.subplots(3, sharex=True)

	
	axs[0].plot(timeStamps, latency)
	axs[0].set( ylabel = 'Latancy(ms)')
	
	

	axs[1].plot(timeStamps, downSpeed)
	axs[1].plot(timeStamps, upSpeed)
	axs[1].set( ylabel='Bandwidth(Mbps)')

	
	axs[2].plot(timeStamps, packetLoss)
	axs[2].set(xlabel='Time Stamp', ylabel='% Packet Loss')

	plt.xticks(rotation=90)
	plt.show()
	
	
	
