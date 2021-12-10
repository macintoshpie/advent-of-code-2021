from python_utils import readlines

open_to_close = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}

close_to_open = {v: k for k, v in open_to_close.items()}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def main():
    input = [list(l.strip()) for l in readlines()]
    line_completions = []
    scores = []
    for line in input:
        stack = []
        illegal = False
        for char in line:
            if char in open_to_close.keys():
                stack.append(char)
            else:
                if stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    # skip illegal lines
                    illegal = True
                    break

        if not illegal and len(stack) > 0:
            completion = []
            total_score = 0
            for char in reversed(stack):
                total_score = (total_score * 5) + points[open_to_close[char]]
                completion.append(open_to_close[char])
            line_completions.append(completion)
            scores.append(total_score)

    print(sorted(scores)[int(len(scores) / 2)])

    # print(sum([points[char] for char in illegal_chars]))

if __name__ == '__main__':
    main()
