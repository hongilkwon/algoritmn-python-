"""
    정수 삼각형

    그냥 보면 상향식 dp 문제이다.

    7
    3 8
    8 1 0
    2 7 4 4
    4 5 2 6 5
"""

# table[row][col]
# table = [[0 for _ in range(501)] for _ in range(501)]
#
#
# def solution(triangle):
#     answer = 0
#
#     table[0][0] = triangle[0][0]
#
#     for r in range(1, len(triangle)):
#         for c in range(len(triangle[r])):
#             if c == 0:
#                 table[r][c] = triangle[r][c] + table[r - 1][c]
#             elif c == len(triangle[r]) - 1:
#                 table[r][c] = triangle[r][c] + table[r - 1][c - 1]
#             else:
#                 table[r][c] = triangle[r][c] + max(table[r - 1][c - 1], table[r - 1][c])
#
#     answer = max(table[len(triangle) - 1])
#     print(answer)
#
#     return answer
