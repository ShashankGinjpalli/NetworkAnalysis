# NetworkAnalysis
Simple Network Analysis using Speedtest-CLI

## Problem

During the Summer of 2020 we were having really spotty internet connection issues and our ISP refused to change the cable running to our house as they claimed it was a problem to the whole neighborhood. This was a really big problem as none of us were able to work from home effeciently with out internet cutting out all of the time

I was determine to get this problem resolved and so I ran a little monitoring utility using my raspberry pi for a couple of days


## Dependencies
- Python 3.8
- SpeedTest-CLI by SpeedTest.net

## Solution

I plotted network metrics such as Packet Loss and speed every 10 minutes over the course of a couple of days and discovered that the internet was very unstable around a certain time each day. We showed this to our ISP who finally agreed to change the cable running to out house


## To Run 
- Install SpeedTest-CLI
- make sure that you are running this on python 3.8
- activate the virtual environment
- run ``` python networkAnalysis.py ```


