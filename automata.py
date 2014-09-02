from board import *
import random
import opc, time

client = opc.Client('beaglebone:7890')

length = 30
height = 23

color = (128,0,128)

ruleset = "00110000"[::-1]

wrap = True
totalistic = True

delay = 1/2.0

rules = []
for x in ruleset:
    rules.append(x=="1")

board = Board(length, height, color, wrap, totalistic)

for x in range(0,500):
    board.toggle(random.randint(0,30), random.randint(0,23))
#board.toggle(2)

while True:
    client.put_pixels(board.output(), channel=0)
    time.sleep(delay)

    new_board = Board(length, height, color, wrap, totalistic)
    for x in range(0, length):
        for y in range(0, height):
            new_board.get(x, y).alive = rules[board.score(x, y) - 1]

    board = new_board

