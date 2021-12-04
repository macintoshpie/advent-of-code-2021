from collections import defaultdict

from python_utils import readlines

BOARD_SIZE = 5
MARKED = None
Board = list[list[int]]


def parse_boards(lines: list[str]) -> list[Board]:
    current_board = []
    boards = []
    for line in lines:
        if line:
            current_board.append([int(v) for v in line.split()])
        else:
            boards.append(current_board)
            current_board = []
    boards.append(current_board)

    return boards


def is_winning_position(board: Board, row_idx: int, col_idx: int) -> bool:
    row = board[row_idx]
    column = [board[i][col_idx] for i in range(BOARD_SIZE)]
    return (
        all([v == MARKED for v in row])
        or all([v == MARKED for v in column])
    )


def score_board(board: Board, last_called_number: int) -> int:
    total = 0
    for row in board:
        for value in row:
            if value != MARKED:
                total += value

    return total * last_called_number


def main():
    input = [l.strip() for l in readlines()]
    bingo_balls = [int(v) for v in input[0].split(',')]
    
    boards = parse_boards(input[2:])

    inverted_boards = defaultdict(list)
    for board_idx, board in enumerate(boards):
        for row_idx, row in enumerate(board):
            for col_idx, value in enumerate(row):
                inverted_boards[value].append((board_idx, row_idx, col_idx))

    for called_ball in bingo_balls:
        for matching_board in inverted_boards[called_ball]:
            board_idx, row_idx, col_idx = matching_board
            board = boards[board_idx]
            board[row_idx][col_idx] = MARKED
            if is_winning_position(board, row_idx, col_idx):
                score = score_board(board, called_ball)
                print(score)
                return


if __name__ == '__main__':
    main()
