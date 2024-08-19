"""
    1로 만들기(dp)

    -X가 3으로 나누어 떨어지면, 3으로 나눈다.
    -X가 2로 나누어 떨어지면, 2로 나눈다.
    -1을 뺀다.

    1 <= N <= 1_000_000
    예시)

    10 → 9 → 3 → 1
    위의 3가지 연산중 1개를 선택하여 숫자를 1로 만든다...
    반대로 1 -> n 이 되는 최솟값 이기도 하다.

    이전 값을 통해 다음 값을 정할수 있다.
    상향식 dp문제
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# INF = 1_000_000_000
# table = [INF] * 1_000_001
#
# if __name__ == '__main__':
#
#     table[0] = 0
#     table[1] = 0
#
#     for i in range(2, 1_000_001):
#         if i % 3 == 0:
#             table[i] = min(table[i], table[int(i / 3)] + 1)
#         if i % 2 == 0:
#             table[i] = min(table[i], table[int(i / 2)] + 1)
#
#         table[i] = min(table[i], table[i - 1] + 1)
#
#     print(table[n])
