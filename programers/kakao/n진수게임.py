"""
    n진수 게임

"""

# import sys
#
#
# input = sys.stdin.readline
#
# def convert(num, base):
#     arr = "0123456789ABCDEF"
#     q, r = divmod(num, base)
#
#     if q == 0:
#         return arr[r]
#     else:
#         return convert(q, base) + arr[r]
#
#
# def solution(n, t, m, p):
#     answer = ''
#
#     s = ''
#     num = 0
#     while len(s) < (m*t):
#         s += convert(num, n)
#         num += 1
#
#     for i in range(0, len(s)):
#         if len(answer) == t:
#             break
#         if (i % m) == p-1:
#             answer += s[i]
#
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(2, 4, 2, 1)
