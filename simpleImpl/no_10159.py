"""
    저울(플로이드)

    우리는 일부 물건 쌍에 대해서 양팔 저울로 어떤 것이 무거운 것인지를 측정한 결과표

    사고과정...
    일단, 플로이드 와샬을 응용하여

"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# m = int(input())
#
# dist = [[0 for _ in range(n)] for _ in range(n)]
#
# for _ in range(m):
#     u, v = map(int, input().split())
#     dist[u - 1][v - 1] = 1
#
#
# def floyd():
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if dist[i][k] == 1 and dist[k][j] == 1:
#                     dist[i][j] = 1
#
#
# if __name__ == '__main__':
#     floyd()
#
#     temp = [0 for _ in range(n)]
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if i == j:
#                 continue
#             # i -> j 그리고 j -> i 모든 연결 상태가 없다면 => 둘이 비교가 안된다
#             if dist[i][j] == 0 and dist[j][i] == 0:
#                 cnt += 1
#         temp[i] = cnt
#
#     for c in temp:
#         print(c)