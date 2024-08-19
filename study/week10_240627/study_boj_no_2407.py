"""
    조합

    nCm을 출력

    (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

    * 어떻게 뽑혔는지가 중요한게 아니가 결국 몇개의 조합이 나오는지를 묻고있다.

    사고과정.

    1. python 내장함수 -> -> 시간초과
    from itertools import combinations, permutations

    nums = [1,2,3,4]
    result = list(combinations(nums, 2))

    2. 재귀를 통한 구현 -> 시간초과

    nums = [1, 2, 3, 4, 5]
    result = []
    cnt = 0


    def combi(n, r, start=0):
        global cnt

        if len(result) == r:
            print(*result)
            cnt += 1
            return

        for i in range(start, n):
            result.append(i)
            combi(n, r, i + 1)
            result.pop()


    3. 상향식 DP를 통한 combination "갯수" 세기.

    100C20 도 너무 큰 숫자임.
    nCr = n-1Cr-1 + n-1Cr
    nC0 = 1

    단순히 조합의 갯수를 묻는다면 상향식 dp O(n^2)로 빠르게 해결 가능하다.
"""

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# table = [[0 for j in range(n + 1)] for i in range(n + 1)]
#
# if __name__ == '__main__':
#
#     for i in range(n):
#         table[i][0] = 1
#         table[i][i] = 1
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             table[i][j] = table[i - 1][j] + table[i - 1][j - 1]
#     # 출력
#     # for e in table:
#     #     print(*e)
#     print(table[n][m])
