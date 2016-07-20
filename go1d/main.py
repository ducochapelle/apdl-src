'''
Have an empty board
Suggest all moves in a list
Go over the moves
filter the legal moves
If there are no legal moves, do the recursive!

(fuck ko for now)
'''

black, white = 0,1

class board():
    def __init__(self, board=None, size=5):
        if board==None:
            self.empty = range(size)
            self.black = []
            self.white = []
            self.turn = black
            self.other = self.white
            self.samer = self.black
        else:
            self.empty = [x for x in board.empty] # object pointer fucks
            self.black = [x for x in board.black]
            self.white = [x for x in board.white]
            self.turn = board.turn
            self.other = self.white if self.turn == black else self.black
            self.samer = self.white if self.turn == white else self.black
        self.draw()
    def move(self,square):
        ''' Either resolves the move or makes the pass. If legal, returns
        the new position. If the move is illegal, returns False.'''
        copy = board(self)
        if not square == None: # play the move if there is one
            if not square in self.empty: # moronic move
                return False
            copy.empty.remove(square)
            copy.samer.append(square)
        if square == None or copy.resolve(square): # pass or resolved move
            copy.flipturn()
            copy.draw()
            return copy
        else: # unresolved move
            return False 
    def resolve(self, square):
        # KILL, BREATH, DIE
        for n in [-1,1]:
            u = unit(square+n, self.other, self.empty)
            if u.birth and not u.alive:
                for p in range(u.tail+1, u.head):
                    self.other.remove(p)
                    self.empty.append(p)
        u = unit(square, self.samer, self.empty)
        return u.alive
    def flipturn(self):
        self.turn = black if self.turn == white else white
        self.other, self.samer = self.samer, self.other
    def prin(self):
        s, t = "", 0
        while True:
            if t in self.empty:   s += "+"
            elif t in self.black: s += "B"
            elif t in self.white: s += "W"
            else:                 break
            t += 1
        print(s)
    def draw(self):
        s, t = "", 0
        while True:
            if t in self.empty:   s += "+"
            elif t in self.black: s += "B"
            elif t in self.white: s += "W"
            else:                 break
            t += 1
        self.s = s

class unit():
    def __init__(self, square, pebbles, empty):
        self.birth = square in pebbles
        self.tail = self.find_end(square, pebbles, -1)
        self.head = self.find_end(square, pebbles, 1)
        self.alive = self.head in empty or self.tail in empty
    def find_end(self, square, pebbles, direction):
        n = direction
        while square + n in pebbles:
            n += direction
        return square + n

class game():
    def __init__(self, size=5):
        self.boards = []
        self.boards.append(board(size=size))
        self.prin()
    def prin(self):
        for board in self.boards:
            board.prin()
    def move(self,m):
        board = self.boards[-1].move(m)
        if board:
            self.boards.append(board)
            self.prin()
            return True
        else:
            self.prin()
            return False

def tree(board):
    return [board] + filter(bool, map(board.move, board.empty))

##b = board()    
##nodes = []
##nodes.append(tree(b))
##nodes += map(tree,nodes[-1][1:])
##nodes += map(tree,nodes[1:


