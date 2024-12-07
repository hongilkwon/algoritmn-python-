"""
    문서검색


     최대 몇 번 중복되지 않게 등장하는지 구하는...

     단순구현인데 생각을 잘못하면 어려워 질수 있음.
"""

# import sys
#
# input = sys.stdin.readline
#
# a = str(input().rstrip())
# b = str(input().rstrip())
#
# if __name__ == '__main__':
#
#     i = 0
#     cnt = 0
#
#     while i < len(a):
#         if a[i:i + len(b)] == b:
#             i += len(b)
#             cnt += 1
#         else:
#             i += 1
#
#     print(cnt)