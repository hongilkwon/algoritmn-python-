"""
    최소 스패닝 트리(Mst, 크루스칼)

"""

# import sys
#
# input = sys.stdin.readline
#
# v, e = map(int, input().split())
#
# table = [i for i in range(v + 1)]
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
#     edges = []
#     for i in range(e):
#         u, v, w = map(int, input().split())
#         edges.append((u, v, w))
#
#     # Greedy 원리에 따라 최소 가중치가 먼저 나오도록 정렬
#     edges.sort(key=lambda x: x[2])
#
#     total_cost = 0
#     for e in edges:
#         # 두개의 노드를 하나의 집합으로 합칠때, 사이클이 생기지 않는다면, 합친다.
#         if not find(e[0], e[1]):
#             union(e[0], e[1])
#             total_cost += e[2]
#
#     print(total_cost)
