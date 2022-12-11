from typing import List
import aiohttp
import asyncio
from converter import convert_str_to_matrix, convert_matrix_to_list


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return convert_matrix_to_list(
                        convert_str_to_matrix(await resp.text())
                    )
                print(resp.status)
        except Exception as e:
            print(e)


SOURCE_URL = '''https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'''
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL


if __name__ == '__main__':
    test_get_matrix()
