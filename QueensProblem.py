N = 4

board = [[0 for i in range(N)] for j in range(N)]

def isSafe(row, col):

    # Check same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(col):

    # All 4 queens are placed
    if col == N:
        return True

    for row in range(N):

        if isSafe(row, col):

            # Place queen
            board[row][col] = 1

            # Move to next column
            if solve(col + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False

if solve(0):
    print("Solution of 4 Queens:")

    for row in board:
        print(row)

else:
    print("Solution does not exist")
