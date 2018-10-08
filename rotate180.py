test_matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

def rotate180(matrix):
    new_matrix = [None for i in range(len(matrix))]
    # Here's the algorithm
    # Take the i-th row, reverse it
    # Insert as the N-1-ith row
    for i, row in enumerate(matrix):
        new_matrix[len(matrix)-i-1] = row[::-1]
    return new_matrix


def disp(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print matrix[i][j],
        print

if __name__ == "__main__":
    disp(test_matrix)
    print "\n\n"
    final = rotate180(test_matrix)
    disp(final)
