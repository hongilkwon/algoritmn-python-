"""
    감시피하기

    (3 ≤ N ≤ 6)

    장애물 뒤편에 숨어 있는 학생들은 볼 수 없다.
    선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정

    사고과정.

    완전탐색 + 복잡구현
    n이 6으로 충분히 작다
    36 C 3 (장애물 3개 설치) * (선생님의 수 * 12)

    배울점
    파이썬 언어 조합 및 바깥 for문 나가기.
    map(func, iterable)

"""

# import sys
# from itertools import combinations
# import copy
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = [list(map(str, input().split())) for row in range(n)]
# t_list = []
# for row in range(n):
#     for col in range(n):
#         if arr[row][col] == 'T':
#             t_list.append((row, col))
#
# nums = [i for i in range(n * n)]
# combi_result = list(combinations(nums, 3))
#
# # def convert_position(x):
# #     row = int(x / n)
# #     col = x % n
# #     return row, col
#
# # lamda 함수를 사용해도 된다.
# convert_position = lambda x: (int(x / n), x % n)
#
#
# def check(tempMap):
#     for t in t_list:
#         r, c = t
#
#         # 상
#         for i in range(r - 1, -1, -1):
#             if tempMap[i][c] == 'O':
#                 break
#             if tempMap[i][c] == 'S':
#
#                 return False
#         # 하
#         for i in range(r + 1, n):
#             if tempMap[i][c] == 'O':
#                 break
#             if tempMap[i][c] == 'S':
#                 return False
#         # 좌
#         for i in range(c - 1, -1, -1):
#             if tempMap[r][i] == 'O':
#                 break
#             if tempMap[r][i] == 'S':
#                 return False
#         # 우
#         for i in range(c + 1, n):
#             if tempMap[r][i] == 'O':
#                 break
#             if tempMap[r][i] == 'S':
#                 return False
#
#     return True
#
#
# if __name__ == '__main__':
#
#     is_possible = True
#
#     for e in combi_result:
#         positions = tuple(map(convert_position, e))
#         tempMap = copy.deepcopy(arr)
#
#         for p in positions:
#             r, c = p
#             if arr[r][c] != 'X':
#                 is_possible = False
#                 break
#             tempMap[r][c] = 'O'
#
#         if not is_possible:
#             is_possible = True
#             continue
#
#         if check(tempMap):
#             # for i in tempMap:
#             #     print(i)
#             print("YES")
#             exit(0)
#
#     print("NO")
