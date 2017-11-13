def damaged_or_sunk (board, attacks):
    # Code here
    # convert board into dictionarry
    result = {'sunk': 0, 'damaged': 0 , 
              'not_touched': 0, 'points': 0}
    
    len_x =len(board[0])
    len_y = len(board)

#    boats = {board[col][row]:[col,row]  for row in range(len_x) for col in range(len_y) if board[col][row] != 0}

    coords = []
    boat_init = []
     
    coords = [[col + 1, len_y - row] for row in range(len_y) for col in range(len_x) if board[row][col] != 0]
    boat_init = [board[row][col] for row in range(len_y) for col in range(len_x) if board[row][col] != 0]
    boat_end = boat_init.copy()

    for attack in attacks:
        if attack in coords:
            boat_end.pop(coords.index(attack))
            coords.pop(coords.index(attack))
    
    for boat_id in set(boat_init):
        sum_init = sum([el == boat_id for el in boat_init])
        sum_end = sum([el == boat_id for el in boat_end])
        if sum_init - sum_end == 0:
            result['not_touched'] += 1
            result['points'] -= 1
        elif sum_end == 0:
            result['sunk'] += 1
            result['points'] += 1
        else:
            result['damaged'] += 1
            result['points'] += 0.5
    return result  

''' 
def damaged_or_sunk (board, attacks):
    boats, hits, attacks = {}, set(), [tuple(e) for e in attacks]
    cells = {(c, len(board) - r):v for r, row in enumerate(board) for c, v in enumerate(row, 1) if v}
    for p, v in cells.items(): boats[v] = boats.get(v, set()) | {p}
                
    for a in [e for e in attacks if cells.get(e, None) in boats]:
        hits.add(cells[a])
        boats[cells[a]] -= {a}
    result = {'sunk':sum(1 for k in boats if not boats[k]), 'damaged':sum(1 for k in hits if boats[k]), 'not_touched':sum(1 for k in boats if k not in hits)}
    result['points'] = result['sunk'] + result['damaged'] * 0.5 - result['not_touched']
    return result
 '''