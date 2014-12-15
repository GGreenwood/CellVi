#! /usr/bin/python
from board import *
import random
import opc, time

client = opc.Client('localhost:7890')

length = 30
height = 23

#color = (0,80,140)
#color = (102,20,153)
color = (210,240,80)
colors = ((255,10,10),(10,255,20))

#ruleset = [[1, 1, 1, 1, 1, 1, 1, 1, 1], 
#           [1, 1, 1, 1, 1, 1, 1, 1, 1]]
ruleset = [[0, 0, 0, 1, 0, 0, 0, 0, 0], 
           [0, 0, 1, 1, 0, 0, 0, 0, 0]]

wrap = True
totalistic = True

delay = 1/3.0

iteration = 0

board = None

#if True:
#    for x in range(0,500):
#        board.toggle(random.randint(0,30), random.randint(0,23))
#else:
#    board.toggle(2,0)
#    board.toggle(2,1)
#    board.toggle(2,2)
#    board.toggle(1,2)
#    board.toggle(0,1)
#board.toggle(1,1)
#board.toggle(1,2)
#board.toggle(1,0)

def reset():
    board = Board(length, height, colors, wrap, totalistic)
    for x in range(0,500):
        board.toggle(random.randint(0,30), random.randint(0,23))

    return board

board = reset()

while True:
    if(iteration > 300):
        board = reset()
	iteration = 0
    else:
        iteration = iteration + 1

    #print board
    client.put_pixels(board.output(), channel=0)
    time.sleep(delay)

    new_board = Board(length, height, colors, wrap, totalistic)
    for x in range(0, length):
        for y in range(0, height):
            new_board.get(x, y).alive = ruleset[board.get(x,y).alive][board.score(x, y)]
            if board.get(x,y).alive:
                new_board.get(x,y).color = board.get(x,y).color
            else:
                new_board.get(x,y).color = colors[random.randint(0,len(colors) - 1)]


    board = new_board

