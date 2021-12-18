from python_utils import readlines
from collections import namedtuple

TYPE_LITERAL = 4
LENGTH_TYPE_TOTAL_LENGTH = '0'
LENGTH_TYPE_NUM_SUBPACKETS = '1'

Packet = namedtuple('Packet', ['version', 'type', 'literal', 'operator', 'subpackets'])


def pop_n(bits, n):
    result = ''
    for _ in range(n):
        result += bits.pop(0)
    return result


def parse_literal(bits: list[str]):
    literal = ''
    bits_read = 0
    while bits.pop(0) == '1':
        literal += pop_n(bits, 4)
        bits_read += 5

    literal += pop_n(bits, 4)
    bits_read += 5
    return int(literal, 2), bits_read


def parse_packet(bits: list[str]):
    version = int(pop_n(bits, 3), 2)
    type = int(pop_n(bits, 3), 2)
    total_bits_read = 6
    literal = None
    operator = None
    subpackets = []

    if type == TYPE_LITERAL:
        literal, literal_bits_read = parse_literal(bits)
        total_bits_read += literal_bits_read
    else:
        length_type = bits.pop(0)
        total_bits_read += 1

        if length_type == LENGTH_TYPE_TOTAL_LENGTH:
            num_bits = int(pop_n(bits, 15), 2)
            total_bits_read += 15
            subpackets_bits_read = 0
            while subpackets_bits_read < num_bits:
                subpacket, subpacket_bits_read = parse_packet(bits)
                subpackets_bits_read += subpacket_bits_read
                total_bits_read += subpacket_bits_read
                subpackets.append(subpacket)
        elif length_type == LENGTH_TYPE_NUM_SUBPACKETS:
            num_subpackets = int(pop_n(bits, 11), 2)
            total_bits_read += 11
            while len(subpackets) < num_subpackets:
                subpacket, subpacket_bits_read = parse_packet(bits)
                total_bits_read += subpacket_bits_read
                subpackets.append(subpacket)

    return Packet(version, type, literal, operator, subpackets), total_bits_read

def sum_packet_versions(packet: Packet):
    return packet.version + sum([sum_packet_versions(p) for p in packet.subpackets])

def main():
    input = [l.strip() for l in readlines()][0]
    print(input)
    hex_size = len(input) * 4
    bits = [v for v in str(bin(int(input, 16)))[2:].zfill(hex_size)]
    
    print(''.join(bits))
    packet, bits_read = parse_packet(bits)
    
    print(sum_packet_versions(packet))

if __name__ == '__main__':
    main()
