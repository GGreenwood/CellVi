from board import *
import random
import opc, time

client = opc.Client('beaglebone:7890')

length = 30
height = 23

output = []

for x in range(length*height):
    output.append((0,0,0))

while True:
    client.put_pixels(output, channel=0)

