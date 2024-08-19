"""
   용감한 진수

   (1 ≤ K ≤ N ≤ 100)
   (0 ≤ 힘, 민첩, 지능 ≤ 1_000_000)

   사고과정

   어떻게 풀어야되는지 감이 잘 안옴.
   총 스탯 포인트가 최소이다, 즉, 각각 힘, 민첩, 지능의 제한은 없다는 것.
   힘, 민첩, 지능이 모두 높아야 이길 수 있음.

   1. 완전탐색

   n의 최대 크기가 100으로 작다.
   주어진 적들의 힘, 민첩, 지능의 모든 조합을 생성할 수 있다.

   힘, 민첩, 지능이 모두 높아야 이길 수 있다 -> 최소 1명을 이길려고 해도 그 적의 힘 + 민첩 + 지능을 모두 더한 스탯이 필요하다.
   100*100*100*100

   -> 100_000_000(1억)

    배울점
    CS 알고리즘은 기본적으로 컴퓨터를 통한 문제해결을 위한 순서이다.
    즉 1초에 대략 1억의 연산횟수를 크게 상회하지 않는다는 확신이 있다면, 반드시 완전탐색을 고려해야한다.
"""

# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(n)]
#
# if __name__ == '__main__':
#
#     min_stat = 1_000_000 * 3
#
#     for x in range(n):
#         for y in range(n):
#             for z in range(n):
#                 # 모든 힘, 민, 지, 경우에서 적 k명을 해치울 수 있는 지 확인한다.
#                 h = arr[x][0]
#                 m = arr[y][1]
#                 j = arr[z][2]
#
#                 cnt = 0
#                 for i in range(n):
#                     enemy = arr[i]
#                     if h >= enemy[0] and m >= enemy[1] and j >= enemy[2]:
#                         cnt += 1
#                     if cnt >= k:
#                         min_stat = min(min_stat, h + m + j)
#
#     print(min_stat)
