from test_framework import generic_test


def fill_surrounded_regions(board):
    from collections import deque
    queue = deque([])
    X, Y = len(board), len(board[0])
    for i in range(X):
        queue.append((i, Y - 1))
        queue.append((i, 0))
    for j in range(Y):
        queue.append((0, j))
        queue.append((X - 1, j))

    while len(queue) > 0:
        x, y = queue.popleft()
        if x < 0 or x >= X or y < 0 or y >= Y:
            continue
        if board[x][y] == 'V' or board[x][y] == 'B':
            continue
        board[x][y] = 'V'

        queue.append((x - 1, y))
        queue.append((x + 1, y))
        queue.append((x, y - 1))
        queue.append((x, y + 1))

    for x in range(X):
        for y in range(Y):
            if board[x][y] == 'W':
                board[x][y] = 'B'
            elif board[x][y] == 'V':
                board[x][y] = 'W'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
