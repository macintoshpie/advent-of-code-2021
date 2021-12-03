from python_utils import readlines


def count_increases(x: list[int]) -> int:
    num_increases = 0
    for i in range(1, len(x)):
        if x[i-1] < x[i]:
            num_increases += 1
    
    return num_increases


def main():
    input = [int(v) for v in readlines()]
    print(count_increases(input))

if __name__ == '__main__':
    main()
