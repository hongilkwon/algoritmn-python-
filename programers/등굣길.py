"""
    등굣길

"""

MOD = 1_000_000_007


def solution(m, n, puddles):
    answer = 0

    water = set()
    for e in puddles:
        water.add((e[1], e[0]))

    table = [[0 for c in range(m + 1)] for r in range(n + 1)]
    table[1][1] = 1

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if r == 1 and c == 1:
                continue
            if (r, c) in water:
                table[r][c] = 0
            else:
                table[r][c] = (table[r - 1][c] + table[r][c - 1]) % MOD

    # for e in table:
    #     print(*e)
    answer = table[n][m]
    return answer

# 반례 물웅덩이가 첫째줄에 있다면...
# def solution(m, n, puddles):
#     answer = 0
#
#     water = set()
#     for e in puddles:
#
#         water.add((e[1] - 1, e[0] - 1))
#
#     table = [[0 for c in range(m)] for r in range(n)]
#
#     for r in range(n):
#         for c in range(m):
#             if r == 0 or c == 0:
#                 if (r, c) in water:
#                     table[r][c] = 0
#                 table[r][c] = 1
#
#     for r in range(1, n):
#         for c in range(1, m):
#             if (r, c) in water:
#                 continue
#             table[r][c] = (table[r - 1][c] % MOD + table[r][c - 1]) % MOD
#
#     for e in table:
#         print(*e)
#
#     answer = table[n - 1][m - 1]
#     return answer


if __name__ == '__main__':
    solution(4,	3,	[[2, 2]])