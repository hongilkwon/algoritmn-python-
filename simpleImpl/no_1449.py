"""
    수리공 항승

    물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때,
    항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오

    테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.
    좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각
    길이가 L인 테이프를 무한개

    사고과정

    -1--2-  ......100 101
     *  *

"""


# import sys
#
# input = sys.stdin.readline
#
# n, l = map(int, input().split())
#
# arr = list(map(int, input().split()))
# arr.sort()
#
# if __name__ == '__main__':
#
#     cnt = 0
#     blocked_points = set()
#     for point in arr:
#         if point in blocked_points:
#             continue
#         cnt += 1
#         for i in range(0, l):
#             blocked_points.add(point + i)
#     print(cnt)
