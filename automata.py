from board import *
import random
import opc, time

client = opc.Client('localhost:7890')

size = 150

color = (125,125,150)

ruleset = "00011110"
rules = []
for x in reversed(ruleset):
    rules.append(x=="1")

board = Board(size, color, False)

#for x in range(0,15):
#    board.toggle(x*10)
board.toggle(10)

while True:
    client.put_pixels(board.output(), channel=0)
    time.sleep(1/3.0)

    new_board = Board(size, color)
    for x in range(0, size):
        new_board.get(x).alive = rules[board.score(x)]
    board = new_board

