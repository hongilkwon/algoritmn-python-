"""
    장난감 조립(위상정렬+dp)

    기본 부품은 다른 부품을 사용하여 조립될 수 없는 부품
    중간 부품은 또 다른 중간 부품이나 기본 부품을 이용하여 만들어지는 부품


    기본 부품 1, 2, 3, 4
    중간 부품 5 <= 기본1 2개 + 기본2 2개
    중간 부품 6 <= 중간5 2개 + 기본3 3개 + 기본4 4개

    완제품 7 <=  중간5 2개 + 중간6 2개 + 기본4 5개

    "하나의 장난감 완제품"을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산하는 프로그램을

"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# in_degree = [0 for _ in range(n + 1)]
# adj_list = [list() for _ in range(n + 1)]
# for _ in range(m):
#     # x를 만드는데 y가 k개 필요하다. (y -> x) 가중치 k
#     x, y, k = map(int, input().split())
#     adj_list[y].append((x, k))
#     in_degree[x] += 1
#
# parts = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#
#
# def topology_sort():
#     q = deque()
#
#     # in_degree가 0 이면 기본부품이다.
#     for i in range(1, n + 1):
#         if in_degree[i] == 0:
#             q.append(i)
#             parts[i][i] = 1
#
#     while q:
#         u = q.popleft()
#
#         for next in adj_list[u]:
#             v, w = next
#             # u -> v u부품을 구성하는 i부품 * w개 => v부품을 구성하는 i부품 갯수
#             for i in range(1, n+1):
#                 parts[v][i] += parts[u][i] * w
#
#             in_degree[v] -= 1
#             if in_degree[v] == 0:
#                 q.append(v)
#
#
# if __name__ == '__main__':
#     topology_sort()
#     for i in range(len(parts[n])):
#         if parts[n][i] != 0:
#             print(i, parts[n][i])