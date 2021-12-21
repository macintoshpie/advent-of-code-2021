from __future__ import annotations
from python_utils import readlines

image_map = {
    '.': '0',
    '#': '1'
}

rev_map = {v: k for k, v in image_map.items()}

def parse_input(lines: list[str]):
    enhancement_alg = lines[0]
    
    input_image = [
        [image_map[v] for v in row]
        for row in lines[2:]
    ]
    
    return enhancement_alg, input_image
    

def scan_img(img, i, j, void_value) -> int:
    binary_result = ''
    for i_delt in [-1, 0, 1]:
        for j_delt in [-1, 0, 1]:
            new_i = i + i_delt
            new_j = j + j_delt
            
            if (
                new_i < 0
                or new_i >= len(img)
                or new_j < 0
                or new_j >= len(img[0])
            ):
                binary_result += void_value
            else:
                binary_result += img[new_i][new_j]

    return int(binary_result, 2)

    
def enhance_image(img, alg, void_value) -> list[list[str]]:
    new_img = []
    for i in range(len(img)):
        new_row = []
        for j in range(len(img[i])):
            alg_idx = scan_img(img, i, j, void_value)
            new_row.append(image_map[alg[alg_idx]])

        new_img.append(new_row)

    return new_img


def print_img(img):
    for line in img:
        print(''.join([rev_map[v] for v in line]))


def pad_img(img, pad_val):
    new_img = [[pad_val] * (len(img[0]) + 2)]
    for row in img:
        new_img.append([pad_val] + row + [pad_val])

    new_img.append([pad_val] * (len(img[0]) + 2))
    return new_img

def main():
    input = [l.strip() for l in readlines()]
    
    enhancement_alg, input_img = parse_input(input)
    print_img(input_img)
    
    void_value = '0'
    input_img = pad_img(input_img, void_value)
    
    print_img(input_img)
    
    enhanced_img = enhance_image(input_img, enhancement_alg, void_value)
    print_img(enhanced_img)
    
    new_void_idx = scan_img(
        [[void_value] * 3] * 3,
        1,
        1,
        None
    )
    void_value = image_map[enhancement_alg[new_void_idx]]
    enhanced_img = pad_img(enhanced_img, void_value)
    
    final_img = enhance_image(enhanced_img, enhancement_alg, void_value)
    
    print_img(final_img)
    
    num_lit = sum([sum([v == '1' for v in row]) for row in final_img])
    print(num_lit)

if __name__ == '__main__':
    main()
