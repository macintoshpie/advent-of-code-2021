from python_utils import readlines
from collections import namedtuple
from day_16_part_01 import TYPE_LITERAL, parse_packet, Packet
from math import prod

OPERATIONS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}

def evaluate_packet(packet: Packet):
    if packet.type == TYPE_LITERAL:
        return packet.literal
    
    return OPERATIONS[packet.type]([evaluate_packet(p) for p in packet.subpackets])

def main():
    input = [l.strip() for l in readlines()][0]
    hex_size = len(input) * 4
    bits = [v for v in str(bin(int(input, 16)))[2:].zfill(hex_size)]
    packet, bits_read = parse_packet(bits)
    
    print(evaluate_packet(packet))

if __name__ == '__main__':
    main()
