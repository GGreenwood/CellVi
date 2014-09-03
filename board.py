class Board:
    def __init__(self, length, height, color = (255,255,255), wrap = False, totalistic = True):
        self.cells = []
        self.length = length
        self.height = height
        self.color = color
        self.wrap = wrap
        self.totalistic = totalistic

        for x in range(0,length):
            self.cells.append([])
            for y in range(0, height):
            	self.cells[x].append(Cell(self, x, y, 0))

    def get(self, x, y):
        if(self.wrap):
            return self.cells[x % self.length][y % self.height]
        elif x >= 0 and x < self.length and y >= 0 and y < self.height:
            return self.cells[x][y]
        else:
            return None

    def score(self, x, y):
        return self.get(x, y).score()

    def toggle(self, x, y):
        self.get(x, y).toggle()

    def output(self):
        output = []
        for row in zip(*self.cells):
            for cell in row:
                if(cell.alive == 1):
                    output.append(self.color)
                else:
                    output.append((0,0,0))

        return output

    def __str__(self):
        output = ""
        for x in range(self.length):
            for y in range(self.height):
                output = output + str(self.get(x, y))
            output = output + "\n"
        return output


class Cell:
    def __init__(self, board, x, y, alive):
        self.board = board
        self.x = x
        self.y = y
        self.alive = alive

    def toggle(self):
        if self.alive == 1:
            self.alive = 0
        else:
            self.alive = 1

    def next(self):
        return self.board.get((self.pos + 1))
    
    def prev(self):
        return self.board.get((self.pos - 1))

    def neighbors(self):
        output = []
        for x in range(-1,2):
            for y in range(-1, 2):
                if(x != 0 or y != 0):
                    output.append(self.board.get(self.x + x, self.y + y))
        return output

    def score(self):
        area = self.neighbors()[::-1]
        total = 0
        for x in range(0, len(area)):
            if(area[x] is not None and area[x].alive == 1):
                if(self.board.totalistic):
                    total = total + 1
                else:
                    total += pow(2,x)
        return total

    def __str__(self):
        if self.alive == 1:
            return "*"
        else:
            return "."
