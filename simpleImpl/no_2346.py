"""
    풍선 터트리기(단순구현)
    * 요제프스 문제

    N개의 풍선이 원형으로 놓여 있고.

    양수 => 오른쪽,
    음수 => 왼쪽

    1. deque (rotate 이용하기).
    2. * 직접 index 이용하기.

    사고과정

    이해는 된다.
    근데 어떻게 구현하지?
    "직접??? 어렵다?? => 원형 => 큐"
"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split(' ')))
#
# q = deque()
# for i, v in enumerate(arr):
#     q.append((i + 1, v))
#
#
# if __name__ == '__main__':
#     # 터진 풍선 순서
#     ret = list()
#
#     # q가 빌때까지(풍선이 다 터질떄 까지)
#     while q:
#         print(q)
#         # 풍선을 터침
#         i, v = q.popleft()
#         ret.append(i)
#
#         if v > 0:
#             q.rotate(-(v-1))
#         else:
#             q.rotate(-v)
#
#     print(' '.join(map(str, ret)))