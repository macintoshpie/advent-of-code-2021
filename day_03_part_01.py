from python_utils import readlines


def bit_array_to_number(bit_array: list[bool]) -> int:
    return int(f'0b{"".join([str(int(bit)) for bit in bit_array])}', 2)


def main():
    input = [line.strip() for line in readlines()]
    num_bits = len(input[0])
    bit_frequency = {
        '0': [0] * num_bits,
        '1': [0] * num_bits,
    }
    

    for binary_number in input:
        for idx, bit in enumerate(binary_number):
            bit_frequency[bit][idx] += 1

    gamma_bit_array = [
        bit_frequency['1'][bit_idx] > bit_frequency['0'][bit_idx]
        for bit_idx in range(num_bits)
    ]

    gamma_rate = bit_array_to_number(gamma_bit_array)
    epsilon_rate = bit_array_to_number([not bit for bit in gamma_bit_array])
    print(gamma_rate * epsilon_rate)


if __name__ == '__main__':
    main()
