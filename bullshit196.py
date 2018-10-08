def is_border(dim, index, direction):
    rows, cols = dim
    row, col = index
    if col == cols - 1 and direction == 0:
        return True
    elif col == 0 and direction == 2:
        return True
    elif row == 0 and direction == 3:
        return True
    elif row == rows - 1 and direction == 1:
        return True
    return False

def flatten(grid):
    rows = len(grid)
    cols = len(grid[0])
    row = 0
    col = 0
    direction = 0 # 0 is right
    visited = {}
    flat = []
    skip = False
    visited[(0,0)] = True
    while len(visited) < rows * cols:
        # print (row, col)
        if not skip:
            flat.append(grid[row][col])
        else:
            skip = False
        temp = (row, col)
        # Now update the grid square
        if direction == 0: #right
            col += 1
        elif direction == 1: #down
            row += 1
        elif direction == 2: #left
            col -= 1
        elif direction == 3: #up
            row -= 1

        if (row, col) in visited: #change 
            row, col = temp
            direction += 1
            direction = direction % 4
            skip = True
        elif is_border((rows, cols), (row, col), direction):
            direction += 1
            direction = direction % 4

        visited[(row, col)] = True
    return flat





if __name__ == '__main__':
    arr = [[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]
    print (flatten(arr))
