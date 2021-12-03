from python_utils import readlines


FORWARD = 'forward'
UP = 'up'
DOWN = 'down'

AIM_DIR = {
    UP: -1,
    DOWN: 1,
}


def main():
    commands = [line.split() for line in readlines()]
    commands = [(command, int(units)) for command, units in commands]

    aim = 0
    horizontal_distance = 0
    depth = 0
    for command, units in commands:
        if command == FORWARD:
            horizontal_distance += units
            depth += aim * units
        else:
            aim += AIM_DIR[command] * units
    
    print(horizontal_distance * depth)
    

if __name__ == '__main__':
    main()