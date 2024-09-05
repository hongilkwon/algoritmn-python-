"""
    진수 변환기
"""

# import sys
#
# input = sys.stdin.readline
#
# m, n = map(int, input().split())
#
#
# def convert(n, base):
#     arr = '0123456789ABCDEF'
#     q, r = divmod(n, base)
#
#     if q == 0:
#         return arr[r]
#     else:
#         return convert(q, base) + arr[r]
#
#
# if __name__ == '__main__':
#     print(convert(m, n))
