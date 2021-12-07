from python_utils import readlines


def main():
    input = [l.strip() for l in readlines()]
    input = input[0].split(',')
    input = [int(v) for v in input]

    minv = min(input)
    maxv = max(input)

    min_fuel = float('inf')
    for target_val in range(minv, maxv + 1):
        this_fuel = 0
        for v in input:
            n = abs(target_val - v)
            this_fuel += (n * (n+1)) / 2

        min_fuel = min(min_fuel, this_fuel)

    print(min_fuel)


if __name__ == '__main__':
    main()
