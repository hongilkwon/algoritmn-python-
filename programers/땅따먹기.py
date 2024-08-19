"""
    땅따먹기

     땅따먹기 게임에는 한 행씩 내려올 때,
    "같은 열을 연속해서 밟을 수 없는" 특수 규칙이 있습니다.

    마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수

    1 <= N <= 100_000

    사고과정.

    문제는 어렵지 않았고, n의 크기를 고려하여 쉽게 상향식 dp문제인지 판별도 가능하다.
    하지만, table의 차원을 잘못 잡아서 조금 고생하였다....

    python - List Comprehension에서  for, if가 둘다 나오는 형태 알아두기.
    [ x for x in range(n) if x !=0 ]
"""


# import sys
#
# input = sys.stdin.readline
#
# n = 0
# # table[r][c] 현좌표까지의 최댓값을 기록한다.
# table = None
#
#
# def solution(land):
#     answer = 0
#     global n, table
#
#     n = len(land)
#     table = [[0 for c in range(4)] for r in range(n)]
#
#     table[0] = land[0]
#     for r in range(1, n):
#         for c in range(4):
#             table[r][c] = land[r][c] + max([table[r-1][nc] for nc in range(4) if nc != c])
#
#     answer = max(table[-1])
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])
