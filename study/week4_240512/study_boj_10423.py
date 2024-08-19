"""
    전기가 부족해(MST, 유니온파인드)

   N개의 도시가 있고 M개의 두 도시를 연결하는 케이블의 정보와 K개의 발전소가 설치된 도시가 주어지면,
   케이블 설치 비용을 "최소로 사용"하여 "모든 도시"에 전기가 공급할 수 있도록 해야된다..

   한 도시가 두 개의 발전소에서 전기를 공급 받으면 낭비가 되므로 케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재해야 한다.

   도시의 개수 N(1 ≤ N ≤ 1_000)
   케이블의 수 M(1 ≤ M ≤ 100_000)

   사고과정.

   문제의 해설을 보면 이해가 쉬운데 그냥 떠올리기에는 생각보다 어렵다.

   각 도시는 1개의 발전소로만 전력을 공급받아야한다.
   그 발전소하 어떤것이든 상관은 없다.

   MST를 구현할 때 실제로 발전소들은 떨어져 있지만, 만약 같은 집단이라 가정을한다면
   각각의 노드들 1개의 발전소와 연결될것이고 엣지들은 최소값을 가진다.

   배울점.
   MST를 구현하는 크루스칼 알고리즘의 원리를 물어보는 문제.

"""

# import sys
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
#
# power_plants = list(map(int, input().split()))
#
# edges = list()
# for i in range(m):
#     u, v, w = map(int, input().split())
#     edges.append((u, v, w))
#
# edges.sort(key=lambda x: x[2])
#
# parents = [0] * (n + 1)
# for i in range(len(parents)):
#     if i in power_plants:
#         parents[i] = 0
#     else:
#         parents[i] = i
#
#
# def get_parent(n):
#     if n == parents[n]:
#         return parents[n]
#     else:
#         parents[n] = get_parent(parents[n])
#         return parents[n]
#
#
# def union(a, b):
#     a_parent = get_parent(a)
#     b_parent = get_parent(b)
#     if a_parent < b_parent:
#         parents[b_parent] = a_parent
#     else:
#         parents[a_parent] = b_parent
#
#
# def find(a, b):
#     if get_parent(a) == get_parent(b):
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     cost = 0
#     for e in edges:
#         u, v, w = e
#         if not find(u, v):
#             union(u, v)
#             cost += w
#
#     print(cost)
