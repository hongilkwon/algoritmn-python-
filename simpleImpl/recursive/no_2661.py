"""
    좋은 수열(재귀, 백트레킹)

    임의의 길이의 "인접한" 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜 수열이라고 부른다. 그렇지 않은 수열은 좋은 수열이다.

    1 <= N <= 80

    사고과정.

    최대 3^80
    dp?

    새로운 숫자를 뒤에 붙혔을 때, 좋은수열인 확인하기.

    이미 좋은수열이라고 확인된, 수열에 + @
    ( 좋은 수열 ) + @

    예) 12312 + 3

    길이가 1인 부분수열은
        *   *
    12312 / 3
    2와 3을 비교하면 된다.

    길이가 2인 부분수열은
       **   **
     1231 / 23
    31와 23을 비교하면된다.

    길이가 3인 부분수열은
     ***   ***
     123 / 123
    123와 123을 비교하면된다.


"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# answer = 0
#
#
# def chk(s):
#     flag = True
#     length = len(s)
#     for i in range(1, (length // 2) + 1):
#         if s[length - i * 2:length - i] == s[length - i:]:
#             flag = False
#
#     return flag
#
#
# def go(s):
#     global n, answer
#
#     if len(s) == n:
#         print(s)
#         exit()
#
#     for next in '123':
#         ns = s + next
#         if chk(ns):
#             go(ns)
#
#
# if __name__ == '__main__':
#     go('')
