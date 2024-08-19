"""
     특별한 마법 공격(db)

     1. 완전탐색

        2 5 4 1 3

        2,5중에 선택 -> 2를 선택(O) -> 5,4중에 선택 -> ....
                      2를 선택(x) -> 5는 무조건 선택 -> 4,1중에 선택 -> ...

        2*2*2*2...너무 많은 경우의 수

    2.  DP 상향식(tabulation)

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = [0] + list(map(int, input().split()))
#
# INF = 1_000_000_000_000_000_000
# table = [[INF for _ in range(2)] for _ in range(n + 1)]
#
# if __name__ == '__main__':
#
#     table[1][1] = arr[1]
#     table[1][0] = 0
#
#     for i in range(2, n + 1):
#         table[i][1] = arr[i] + table[i - 1][0]
#         table[i][0] = min(arr[i - 1] + table[i - 1][0], table[i - 1][1])
#
#     answer = min(table[n][0], table[n][1])
#     print(answer)
