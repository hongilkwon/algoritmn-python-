"""
    n^2 배열 자르기

    1 ≤ n ≤ 10_000_000
    0 ≤ left ≤ right < n^2
    right - left < 10^5

    단순구현

        0 1 2 3

    0   1 2 3 4
    1   2 2 3 4
    2   3 3 3 4
    3   4 4 4 4

    1234 / 223 4 / 3334 / 444 4

    배열 1억 * 1억 짜리 생성 -> 시간초과

    left - right => 100_000 10만개?

    0 1 2 3 .... (n*n) -1

    1 2 3 / 2 2 3 / 3 3 3

    2 => [0][2]
    5 => [1][2]

    4 => [1][0]
    4 => [1][2]
"""

# def solution(n, left, right):
#     answer = []
#
#     point_left = (left // n, left % n)
#     point_right = (right // n, right % n)
#
#     arr = []
#
#     if point_left[0] == point_right[0]:
#         temp = [point_left[0] + 1] * point_left[0] + [i for i in range(point_left[0]+1, n+1)]
#         arr = temp[point_left[1]:point_right[1]+1]
#     else:
#         for row in range(point_left[0], point_right[0]+1):
#
#             temp = [row + 1] * row + [i for i in range(row+1, n+1)]
#
#             if row == point_left[0]:
#                 arr += temp[point_left[1]:]
#             elif row == point_right[0]:
#                 arr += temp[:point_right[1]+1]
#             else:
#                 arr += temp
#
#     answer = arr
#     # print(*answer)
#     return answer

# 시간초과
# def solution(n, left, right):
#     answer = []
#
#     arr = [[0 for c in range(n)] for r in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] = max(i, j) + 1
#
#     temp = []
#     for e in arr:
#         # print(*e)
#         temp += e
#     answer = temp[left: right+1]
#     return answer
