from python_utils import readlines

def main():
    input = [l.strip() for l in readlines()]
    
    all_fish = [int(v) for v in input[0].split(',')]
    
    num_days = 80
    for i in range(num_days):
        for j in range(len(all_fish)):
            if all_fish[j] == 0:
                all_fish[j] = 6
                all_fish.append(8)
            else:
                all_fish[j] = all_fish[j] - 1

    print(len(all_fish))
            

if __name__ == '__main__':
    main()
