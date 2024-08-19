"""
    배열 돌리기

    2 ≤ N, M ≤ 300
    1 ≤ R ≤ 10**9
    min(N, M) mod 2 = 0
    1 ≤ Aij ≤ 10**8

    사고과정

    2차원 배열의 크기는 300*300이라 그렇게 크지 않다.

    겉면 회전 하고 내부도 회전하고..

    얼마나 깊이 까지 회전을 하지???
    - 가로 또는 세로가 1 이면 회전을 못함.
    -> 가로 또는 세로중에 짧은놈을 2로 나눈 횟수 만큼의 깊이까지 회전.
    min(n, m) / 2

    회전 횟수가 10억?
    하지만 회전을 하다 보면 반복된 형태닥 나타나게 됨.

    회전횟수 % 배열의 길이

"""

# # import copy
# import sys
#
# input = sys.stdin.readline
#
# n, m, r = map(int, input().split())
#
# arr = [list(map(int, input().split())) for r in range(n)]
#
#
# # # 원본 배열을 복사하는 형태로 회전시키면 시간초과남.
# # def rotate(left_top, right_bottom):
# #     global arr
# #     temp = copy.deepcopy(arr)
# #     # 위
# #     for i in range(left_top[1], right_bottom[1]):
# #         temp[left_top[0]][i] = arr[left_top[0]][i + 1]
# #     # 아래
# #     for i in range(right_bottom[1], left_top[1], -1):
# #         temp[right_bottom[0]][i] = arr[right_bottom[0]][i - 1]
# #     # 왼쪽
# #     for i in range(right_bottom[0], left_top[0], -1):
# #         temp[i][left_top[1]] = arr[i - 1][left_top[1]]
# #     # 오른쪽
# #     for i in range(left_top[0], right_bottom[0]):
# #         temp[i][right_bottom[1]] = arr[i + 1][right_bottom[1]]
# #
# #     arr = copy.deepcopy(temp)
#
# def rotate(i, j, n, m):
#     top_left = arr[i][j]
#     top_right = arr[i][m - 1]
#     bottom_left = arr[n - 1][j]
#     bottom_right = arr[n - 1][m - 1]
#
#     # left
#     for x in range(n - 1, i, -1):
#         arr[x][j] = arr[x - 1][j]
#     # right
#     for x in range(i, n - 1):
#         arr[x][m - 1] = arr[x + 1][m - 1]
#     # top
#     for y in range(j, m - 1):
#         arr[i][y] = arr[i][y + 1]
#     # bottom
#     for y in range(m - 1, j, -1):
#         arr[n - 1][y] = arr[n - 1][y - 1]
#
#     arr[i + 1][j] = top_left
#     arr[i][m - 2] = top_right
#     arr[n - 1][j + 1] = bottom_left
#     arr[n - 2][m - 1] = bottom_right
#
#
# if __name__ == '__main__':
#     arr_cnt = min(n, m) // 2
#
#     for ac in range(arr_cnt):
#         # left_top = (ac, ac)
#         # right_bottom = (n - (1 + ac), m - (1 + ac))
#         size = 2 * (n - ac * 2) + 2 * (m - ac * 2) - 4
#         rotate_cnt = r % size
#
#         for rc in range(rotate_cnt):
#             rotate(ac, ac, n - ac, m- ac)
#
#     for line in arr:
#         print(*line)
