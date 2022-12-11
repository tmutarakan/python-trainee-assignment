from typing import List
import re


def convert_str_to_matrix(data: str) -> List[List[int]]:
    """
    Возвращает матрицу состоящую из целых неотрицательных чисел,
    полученную из строки"""
    output = []
    data = data.split('\n')
    for elem in data:
        numbers = re.findall(r'[0-9]+', elem)
        if numbers:
            output.append([int(_) for _ in numbers])
    return output


def convert_matrix_to_list(matrix: List[List[int]]) -> List[int]:
    """
    Возвращает список содержащий результат обхода полученной матрицы по
    спирали: против часовой стрелки, начиная с левого верхнего угла
    """
    length = len(matrix)
    x = 0   # текущая позиция в матрице
    y = 0
    dx = 1  # смещение по осям, может принимать значения -1, 0, 1
    dy = 0
    depth = 0   # шаг спирали
    curr_perimeter = (length - depth * 2 - 1) * 4
    total_perimeter = 0
    output = []
    for i in range(length**2):
        output.append(matrix[x][y])
        test = x + dx if dx else y + dy
        if i + 1 == total_perimeter + curr_perimeter:
            total_perimeter += curr_perimeter
            depth += 1
            curr_perimeter = (length - depth * 2 - 1) * 4
        if test < depth or test == length - depth:
            dx, dy = -dy, dx
        x += dx
        y += dy
    return output


def main():
    with open('matrix.txt', 'r') as f:
        matrix = convert_str_to_matrix(f.read())
    print(matrix)
    print(convert_matrix_to_list(matrix))


if __name__ == '__main__':
    main()
