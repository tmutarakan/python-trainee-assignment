from typing import List
import re


def convert_str_to_matrix(data: str) -> List[List[int]]:
    """Возвращает матрицу состоящую из целых неотрицательных чисел, полученную из строки"""
    output = []
    data = data.split('\n')
    for elem in data:
        numbers = re.findall(r'[0-9]+', elem)
        if numbers:
            output.append([int(_) for _ in numbers])
    return output


def main():
    with open('matrix.txt', 'r') as f:
        print(convert_str_to_matrix(f.read()))


if __name__ == '__main__':
    main()
