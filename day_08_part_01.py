from python_utils import readlines


def main():
    input = [l.strip() for l in readlines()]
    input = [l.split('|') for l in input]
    total = 0
    for signal_raw, output_raw in input:
        sig = signal_raw.split(' ')
        out = output_raw.split(' ')
        
        for output in out:
            if len(output) in [2, 3, 4, 7]:
                total += 1
    
    print(total)
    


if __name__ == '__main__':
    main()
