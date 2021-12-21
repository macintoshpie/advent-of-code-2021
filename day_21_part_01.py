from __future__ import annotations
from python_utils import readlines

def roll():
    i = 1
    while True:
        yield (i % 100), i
        i += 1


def main():
    input = [l.strip() for l in readlines()]
    
    p1 = int(input[0].split(' ')[-1])
    p2 = int(input[1].split(' ')[-1])
    print(p1, p2)
    
    players = [p1, p2]
    scores = [0, 0]
    step = 0
    roller = roll()
    num_rolls = 0
    winner = None
    while True:
        current_player = players[step % 2]
        r, _ = next(roller)
        r2, _ = next(roller)
        r3, num_rolls = next(roller)
        new_pos = (current_player + r + r2 + r3) % 10
        new_pos = 10 if new_pos == 0 else new_pos
        players[step % 2] = new_pos
        scores[step % 2] += new_pos
        
        if scores[step % 2] >= 1000:
            print(step % 2)
            winner = step % 2
            break
        step += 1


    print(players)
    print(scores)
    print(num_rolls)
    print(num_rolls * scores[(winner + 1) % 2])

if __name__ == '__main__':
    main()
