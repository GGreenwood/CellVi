class Board:
    def __init__(self, length, color = (255,255,255), wrap = False):
        self.cells = []
        self.length = length
        self.color = color
        self.wrap = wrap

        for pos in range(0,length):
            self.cells.append(Cell(self, pos, False))

    def get(self, pos):
        if(self.wrap):
            return self.cells[pos % self.length]
        elif pos >= 0 and pos < len(self.cells):
            return self.cells[pos]
        else:
            return None

    def score(self, pos):
        return self.get(pos).score()

    def toggle(self, pos):
        self.get(pos).toggle()

    def output(self):
        output = []
        for cell in self.cells:
            if(cell.alive):
                output.append(self.color)
            else:
                output.append((0,0,0))

        return output

class Cell:
    def __init__(self, board, pos, alive):
        self.board = board
        self.pos = pos
        self.alive = alive

    def toggle(self):
        self.alive = not self.alive

    def next(self):
        return self.board.get((self.pos + 1))
    
    def prev(self):
        return self.board.get((self.pos - 1))

    def neighbors(self):
        return [self.prev(), self, self.next()]  

    def score(self):
        area = self.neighbors()[::-1]
        total = 0
        for x in range(0, len(area)):
            if(area[x] is not None and area[x].alive):
                total += pow(2,x)
        return total

