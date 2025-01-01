"""
    종이자르기(완전탐색, 단순구현)

    가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을


"""

# import sys
#
# input = sys.stdin.readline
#
# max_c, max_r = map(int, input().split(" "))
#
# n = int(input())
#
# point_c = [0, max_c]
# point_r = [0, max_r]
#
# for _ in range(n):
#     t, point = map(int, input().split(" "))
#     if t == 0:
#         point_r.append(point)
#     else:
#         point_c.append(point)
#
# point_r.sort()
# point_c.sort()
#
# if __name__ == '__main__':
#
#     max_size = 0
#
#     for i in range(1,len(point_r)):
#         h = point_r[i] - point_r[i-1]
#         for j in range(1,len(point_c)):
#             w =  point_c[j] - point_c[j-1]
#             max_size = max(max_size, h*w)
#
#     print(max_size)