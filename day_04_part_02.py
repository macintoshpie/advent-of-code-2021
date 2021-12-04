from collections import defaultdict

from python_utils import readlines
from day_04_part_01 import (
    MARKED,
    is_winning_position,
    parse_boards,
    score_board,
)


def main():
    input = [l.strip() for l in readlines()]
    bingo_balls = [int(v) for v in input[0].split(',')]

    boards = parse_boards(input[2:])

    inverted_boards = defaultdict(list)
    for board_idx, board in enumerate(boards):
        for row_idx, row in enumerate(board):
            for col_idx, value in enumerate(row):
                inverted_boards[value].append((board_idx, row_idx, col_idx))

    winning_board_indices = set()
    for called_ball in bingo_balls:
        for matching_board in inverted_boards[called_ball]:
            board_idx, row_idx, col_idx = matching_board
            if board_idx in winning_board_indices:
                continue

            board = boards[board_idx]
            board[row_idx][col_idx] = MARKED
            if is_winning_position(board, row_idx, col_idx):
                winning_board_indices.add(board_idx)
                if len(winning_board_indices) == len(boards):
                    # board that just won was the last to win
                    score = score_board(board, called_ball)
                    print(score)
                    return


if __name__ == '__main__':
    main()
