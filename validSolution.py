def validSolution(board):
    valid = [1,2,3,4,5,6,7,8,9]
    rows_ok = all([sorted(row) == valid  for row in board]) 
    cols_ok = all([sorted(col) == valid for col in zip(*board)])
    threes = [r[3*i:3*i+3] for r in board for i in range(3)]
    boxes = [threes[9*i + j] + threes[9*i + j+3] + threes[9*i + j+6] for i in range(3) for j in range(3)]
    box_ok = all(sorted(box) == valid for box in boxes)
    return rows_ok and cols_ok and box_ok


'''

print([r + c[] for ])

x = [[1,2,3,3], [4,5,6,6], [7,8,9,9],[2,3,5,7]]
i = j = 0
threes = [c[3*i:3*i+3] for c in b for i in range(3)]

[threes[9*i + j] + threes[9*i + j+3] + threes[9*i + j+6] for i in range(3) for j in range(3)]

'''