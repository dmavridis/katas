import math
class Sudoku():
    #your code here
    def __init__(self, board):
        self.board = board
       
    def is_valid(self):
        N = len(self.board[0])
        S = int(math.sqrt(N))
        
        elem_ok =  all([type(el) == int for row in self.board for el in row])
        if not elem_ok:
            return False

        valid = [i+1 for i in range(N)]    
        rows_ok = all([sorted(row) == valid and len(row) == len(valid)  for row in self.board]) 
        cols_ok = all([sorted(col) == valid for col in zip(*self.board)])
        if not rows_ok or not cols_ok:
            return False
        
        box = [r[S*i:S*i+S] for r in self.board for i in range(S)]
        # Seperate in sets
        box = [box[S*i:S*i+S] for i in range(N)]
        for k in range(N):
            sub_box = []
            for j in range(S):
                # print(j + S*(k//S), k%S)
                sub_box += [el for el in box[j + S*(k//S)][k%S]]
                # sub_box.append(box[j + S*(k//S)][k//S])
            if sorted(sub_box) != valid:
                return False 
        return True
    