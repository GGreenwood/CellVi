from board import *
import random
import opc, time

client = opc.Client('localhost:7890')

size = 150

color = (125,125,150)

ruleset = "00000010"[::-1]

wrap = True

delay = 1/60.0

rules = []
for x in ruleset:
    rules.append(x=="1")

board = Board(size, color, wrap)

#for x in range(0,15):
#    board.toggle(x*10)
board.toggle(2)

while True:
    client.put_pixels(board.output(), channel=0)
    time.sleep(delay)

    new_board = Board(size, color, wrap)
    for x in range(0, size):
        new_board.get(x).alive = rules[board.score(x)]
    board = new_board

