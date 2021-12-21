from __future__ import annotations
from python_utils import readlines
from day_20_part_01 import print_img, parse_input, pad_img, enhance_image, scan_img, image_map

def main():
    input = [l.strip() for l in readlines()]
    
    enhancement_alg, input_img = parse_input(input)
    print_img(input_img)
    
    void_value = '0'
    current_img = pad_img(input_img, void_value)

    for i in range(50):
        print(f'Solving {i}')
        current_img = enhance_image(current_img, enhancement_alg, void_value)
        # print_img(current_img)
        
        new_void_idx = scan_img(
            [[void_value] * 3] * 3,
            1,
            1,
            None
        )
        void_value = image_map[enhancement_alg[new_void_idx]]
        current_img = pad_img(current_img, void_value)
    
    num_lit = sum([sum([v == '1' for v in row]) for row in current_img])
    print(num_lit)

if __name__ == '__main__':
    main()
