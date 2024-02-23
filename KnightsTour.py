# will return array of possible moves stemming from (r,c)
def possibleMoves(r,c):
    arr = [] # array containing next possible moves from (r,c)

    if (r+2) < 8: # if two to the right is still in bounds
        if (c+1) < 8: # if one up is still in bounds
            arr.append([r+2, c+1])
        if (c-1) >= 0: # if one down is still in bounds
            arr.append([r+2, c-1])

    if (r+1) < 8: # if one to the right is still in bounds
        if (c+2) < 8: # if two up is still in bounds
            arr.append([r+1, c+2])
        if (c-2) >= 0: # if two down is still in bounds
            arr.append([r+1, c-2])

    if (r-2) >= 0: # if two to the left is still in bounds
        if (c+1) < 8: # if one up is still in bounds
            arr.append([r-2, c+1])
        if (c-1) >= 0: # if one down is still in bounds
            arr.append([r-2, c-1])

    if (r-1) >= 0: # if one to the left is still in bounds
        if (c+2) < 8: # if two up is still in bounds
            arr.append([r-1, c+2])
        if (c-2) >= 0: # if two down is still in bounds
            arr.append([r-1, c-2])
    
    return arr # return arr = [[r1,c1], [r2,c2],...]

# given two coordinates (r1,c1) and (r2,c2), calculate the move distance between the two
def find(r1,c1, r2,c2):
    # forgot a couple of stupid edge cases (out of bounds inputs)

    # if starting coordinate is equal to end coordinate
    if abs(r2-r1) == 0 and abs(c2-c1) == 0:
        return 0 # 0 moves
        
    # create 8x8 matrix mirroring a chess board (filled with 0's)
    arr = [[0]*8 for _ in range(8)]
    
    # move tracker, n = x means starting point is x moves away from end point
    n = 1

    # first level of possible moves coming from r1, c1 (starting point)
    movesAvail = possibleMoves(r1,c1)
    
    # defining that 0 means uncalculated move distance at coordinate (r2,c2) from starting point
    # loop while the desired coordinate's move distance is 0 (undefined)
    while arr[r2][c2] == 0:
        possibilities = [] # will store next level of possible moves (refresh every loop)
        print(movesAvail) # print out calculated moves (for show purposes)
        for move in movesAvail: # for each of the calculated moves
            if(arr[move[0]][move[1]] == 0): # if coordinate hasn't been defined yet (0 == undefined)
                arr[move[0]][move[1]] = n # set equal to level depth (i.e. first level == (n=1))
            save = possibleMoves(move[0], move[1]) # calculate the next level possible moves from all moves in movesAvail
            for possibleMove in save: # for each calculated move from (move[0] aka row, move[1] aka col)
                possibilities.append(possibleMove) # append to running list
        movesAvail = possibilities # swap places with the level sets, movesAvail now shifts to the next level
        n = n+1 # since we are moving to next level, increment n
        
    return arr[r2][c2] # arr[r2][c2] is no longer 0, return the number at this element, indicating move distance (r1,c1) -> (r2,c2)

# test case, start = (2,2), target = (4,6)
print(find(2,2,4,6))
