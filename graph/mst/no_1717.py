"""
    집합의 표현(유니온-파인드)
    - mst
    - 사이클의 유무 확인(단, 사이클의 구성원소는 dfs)
    - 0(n) table 생성

"""

# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# table = [i for i in range(n + 1)]
#
#
# # 해당 노드의 집합의 대표를 찾고, 대표값을 업데이트 한다.
# def get_parent(n):
#     if n == table[n]:
#         return n
#     else:
#         table[n] = get_parent(table[n])
#         return table[n]
#
#
# # 원소 a와 원소 b를 같은 집합으로 한다.
# def union(a, b):
#     ap = get_parent(a)
#     bp = get_parent(b)
#     if ap < bp:
#         table[bp] = ap
#     else:
#         table[ap] = bp
#
#
# # 원소 a와 원소 b가 같은 집합인지 확인 한다.
# def find(a, b):
#     return get_parent(a) == get_parent(b)
#
#
# if __name__ == '__main__':
#
#     for i in range(m):
#         operator, a, b, = map(int, input().split())
#         if operator == 0:
#             union(a, b)
#         else:
#             if find(a, b):
#                 print("YES")
#             else:
#                 print("NO")
