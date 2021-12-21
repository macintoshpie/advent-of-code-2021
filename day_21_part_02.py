from __future__ import annotations
from python_utils import readlines

turns = {
    # roll total: number of ways to get that total
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

def count_wins(positions, scores, roll_total, player_turn):
    new_pos = (positions[player_turn] + roll_total) % 10
    new_pos = 10 if new_pos == 0 else new_pos

    if scores[player_turn] + new_pos >= 21:
        # that player won on this turn
        num_wins = turns[roll_total]
        if player_turn == 0:
            return (num_wins, 0)
        else:
            return (0, num_wins)

    # player did not win yet, test all rolls for next player
    if player_turn == 0:
        new_positions = (new_pos, positions[1])
        new_scores = (scores[0] + new_pos, scores[1])
    else:
        new_positions = (positions[0], new_pos)
        new_scores = (scores[0], scores[1] + new_pos)

    total_p1_wins, total_p2_wins = 0, 0
    for next_roll_total in turns.keys():
        p1_wins, p2_wins = count_wins(new_positions, new_scores, next_roll_total, player_turn=(player_turn + 1) % 2)
        total_p1_wins += p1_wins * turns[roll_total]
        total_p2_wins += p2_wins * turns[roll_total]

    return (total_p1_wins, total_p2_wins)

def main():
    input = [l.strip() for l in readlines()]
    
    p1 = int(input[0].split(' ')[-1])
    p2 = int(input[1].split(' ')[-1])
    print(p1, p2)
    
    players = (p1, p2)
    scores = (0, 0)
    
    total_p1_wins, total_p2_wins = 0, 0
    for roll_total in turns.keys():
        p1_wins, p2_wins = count_wins(players, scores, roll_total, player_turn=0)
        total_p1_wins += p1_wins
        total_p2_wins += p2_wins
        print(f'Done with {roll_total}:')
        print(f'  p1: {total_p1_wins}')
        print(f'  p2: {total_p2_wins}')

    print(total_p1_wins, total_p2_wins)

if __name__ == '__main__':
    main()
