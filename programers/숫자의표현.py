"""
    숫자의 표현(투 포인터)

    자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
    "연속된 자연수"들로 n을 표현하는 방법의 수

    n은 10_000 이하의 자연수

    사고과정.

    연속된 자연수?

    연속된 자연수의 구간?
    투 포인터?

    *       *
    1 2 3 4 5 6 7 8 9....

"""

# import sys
#
# input = sys.stdin.readline
#
#
# def solution(n):
#     answer = 0
#
#     # edge case
#     if n == 1:
#         return 1
#
#     start = 1
#     end = 1
#     seq_sum = 0
#
#     while start <= n and end <= n:
#
#         if seq_sum == n:
#             answer += 1
#
#         if seq_sum <= n:
#             seq_sum += end
#             end += 1
#         else:
#             while seq_sum > n:
#                 seq_sum -= start
#                 start += 1
#
#     return answer + 1
#
#
# if __name__ == '__main__':
#     solution(15)
