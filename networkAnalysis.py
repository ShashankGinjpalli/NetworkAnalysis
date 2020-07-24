import os
import json
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys


downSpeed = []
upSpeed = []
packetLoss = []
latency = []
timeStamps = []

interval = input('Enter Time Interval(s)')





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
					timeStamps.append(str(current_time))
					latency.append(float(data["ping"]["latency"]))
					downSpeed.append(float(data["download"]["bandwidth"])/125000)
					upSpeed.append(float(data["upload"]["bandwidth"])/125000)
					packetLoss.append(float(data["packetLoss"]))
					


				else:
					outfile.write(str(current_time) + ',' + '0,0,0,100' + "\n")
					timeStamps.append(str(current_time))
					latency.append(0)
					downSpeed.append(0)
					upSpeed.append(0)
					packetLoss.append(100)


		
		


	
	plt.close('all')

	fig, axs = plt.subplots(3, sharex=True, figsize=(12,8))
	plt.tight_layout(pad = 3)
	
	
	# plt.se
	# fig.set_size_inches(11, 6, forward=True)
	

		
	axs[0].plot(timeStamps, latency)
	axs[0].set( ylabel = 'Latancy(ms)')
		
		

	axs[1].plot(timeStamps, downSpeed)
	axs[1].plot(timeStamps, upSpeed)
	axs[1].set( ylabel='Bandwidth(Mbps)')

		
	axs[2].plot(timeStamps, packetLoss)
	axs[2].set(xlabel='Time Stamp', ylabel='% Packet Loss')

	plt.xticks(rotation=90)


	time.sleep(1)
	plt.draw()
	time.sleep(int(interval))
	plt.pause(10)
	print("Starting Next Test")
	


	
	
	
