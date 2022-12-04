from typing import List


def convert_matrix_to_list(matrix: List[List[int]]) -> List[int]:
    """Возвращает список содержащий результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла"""
    length = len(matrix)
    x = 0
    y = 0
    dx = 1
    dy = 0
    depth = 0
    curr_perimeter = (length - depth * 2 - 1) * 4
    total_perimeter = 0
    output = []
    for i in range(length**2):
        output.append(matrix[x][y])
        test = x + dx if dx else y + dy
        if i + 1 == total_perimeter+ curr_perimeter:
            total_perimeter += curr_perimeter
            depth += 1
            curr_perimeter = (length - depth * 2 - 1) * 4
        if test < depth or test == length - depth:
            dx, dy = -dy, dx
        x += dx
        y += dy
    return output


def main():
    '''matrix = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]'''
    '''matrix = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]'''
    '''matrix = [
        [10,20,30,40,50],
        [60,70,80,90,100],
        [110,120,130,140,150],
        [160,170,180,190,200],
        [210,220,230,240,250],
    ]'''
    matrix = [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]
    ]
    print(convert_matrix_to_list(matrix))


if __name__ == '__main__':
    main()
