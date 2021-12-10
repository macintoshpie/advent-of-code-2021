from python_utils import readlines

open_to_close = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}

close_to_open = {v: k for k, v in open_to_close.items()}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def main():
    input = [list(l.strip()) for l in readlines()]
    illegal_chars = []
    for line in input:
        stack = []
        for char in line:
            if char in open_to_close.keys():
                stack.append(char)
            else:
                if stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    illegal_chars.append(char)
                    break

    print(sum([points[char] for char in illegal_chars]))

if __name__ == '__main__':
    main()
