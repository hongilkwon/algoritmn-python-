"""
    n으로 표현(재귀, DP)

    N과 사칙연산만 사용해서 표현 할 수 있는 방법 중,
    N 사용횟수의 최솟값을 return 하도록 solution 함수

    사칙연산만 가능하며 나누기 연산에서 나머지는 무시

    1 <= N <= 9
    1 <= number <= 32_000

    최솟값이 8보다 크면 -1
    => N의 개수는 최대 8개

    사고과정.

    완전탐색

    ('', +, -, *, /)

    N이 1개 n 1개
    N이 2개 nn, n+n, n-n, n/n, n*n 5개
    N이 3개 nnn, nn + n, nn - n, nn / n, nn * n
           n+nn, n+n+n, n+n-n, n+n/n, n+n*n
           n-nn, n-n+n, n-n-n, n-n/n, n-n*n
           n/nn, n/n+n, n/n-n, n/n/n, n/n*n
           n*nn, n*n+n, n*n-n, n*n/n, n*n*n (25개)

    N이 4개 n n n n
    N이 5개
    N이 6개
    N이 7개
    N이 8개
    + 괄호...

    실제 실행결과 대략 12_491_713 (1250만)

    DP =>

"""

import sys

input = sys.stdin.readline


def solution(_n, _number):
    answer = 0
    return answer


if __name__ == '__main__':
    solution(4, 31)


# 재귀함수를 이용한 완전탐색(시간이 오래걸림)
# INF = 1_000_000_000
# n, number, = 0, 0
#
# ret = INF
# total_call_cnt = 0
#
#
# def go(cur_num, cnt):
#     global n, number, ret, total_call_cnt
#     total_call_cnt += 1
#
#     # 8회 이상이면, 더 이상 진행하지 않음
#     if cnt > 8:
#         return
#     # 목표 숫자와 같으면 최솟값 갱신.
#     if cur_num == number:
#         ret = min(ret, cnt)
#         return
#
#     seqN = 0
#     for i in range(1, 9):
#         seqN = (seqN * 10) + n
#         go(cur_num + seqN, cnt + i)
#         go(cur_num - seqN, cnt + i)
#         go(cur_num // seqN, cnt + i)
#         go(cur_num * seqN, cnt + i)
#
#
# def solution(_n, _number):
#     answer = 0
#     global n, number, ret
#     n, number = _n, _number
#
#     if _n == _number:
#         return 1
#     go(0, 0)
#
#     if ret == INF:
#         answer = -1
#     else:
#         answer = ret
#     # print(total_call_cnt)
#     # print(answer)
#     return answer

