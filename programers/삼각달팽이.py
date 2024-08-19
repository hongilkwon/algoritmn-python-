"""
    삼각 달팽이(배열 다루기)


    1. 수학적 규칙성을 찾는다.
    -> 실패

    2. n = 1000 때문에, 구현으로 2차원 배열을 생성후
    1차원 배열로 만들어 답을 도출한다.

    1
    2  9
    3 10  8
    4  5  6  7

    1. 위에서 아래로 
    2. 왼쪽에서 오른쪽으로
    3. 대각선 방향

    4칸(위에서 아래로) -> 3칸(왼쪽에서 오른쪽으로) -> 2칸(대각선 방향) -> 1칸(위에서 아래로)
"""


# import sys
#
# input = sys.stdin.readline
#
# def solution(n):
#     answer = []
#
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#
#     size = [i for i in range(n, 0, -1)]
#     num = 1
#     y, x = -1, 0
#
#     for i, v in enumerate(size):
#         for _ in range(v):
#             # 위 -> 아래 이동
#             if i % 3 == 0:
#                 y += 1
#             # 왼쪽 -> 오른쪽 이동
#             if i % 3 == 1:
#                 x += 1
#             # 대각선(상승) 이동
#             if i % 3 == 2:
#                 y -= 1
#                 x -= 1
#             arr[y][x] = num
#             num += 1
#
#     for e in arr:
#         print(*e)
#
#     for r in range(n):
#         for c in range(r + 1):
#             answer.append(arr[r][c])
#
#     return answer
#
#
# if __name__ == '__main__':
#     solution(4)
