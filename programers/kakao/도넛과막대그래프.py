"""
    도넛과 막대 그래프.

    도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들이 있습니다.
    이 그래프들은 1개 이상의 정점과, 정점들을 연결하는 단방향 간선

    각 정점에 서로 다른 번호를 매겼습니다.

     그래프들과 "무관한 정점"을 하나 생성한 뒤,
     각 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 "임의의 정점 하나"로 향하는 간선들을 연결했습니다.

     그래프의 간선 정보가 주어지면 생성한 정점의 번호와 정점을 생성하기 전
     도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 구해야 합니다.

     사고과정

     무관한 정점은 모든 간선이 나가는 방향 (in_degree 0개이고, out_degree 2개이상)

     1. 무관한 정점을 찾는다.
     2. 무관한 정점을 삭제한다. 그 그래프가 무엇인지 알아낸다.

     알아내는 방법 ???
     도넛 모양 그래프 => (n개의 정점, n개의 간선) cycle 있음
     막대 모양 그래프 => (n개의 정점, n-1개의 간선) cycle 없음
     팔자 모양 그래프 => (2n+1개의 정점, 2n+2개의 간선) cycle 있음

     union_find로 노드, 엣지 군집화.
     갯수로 판별?

"""


# n = 0
# node_set = set()
# center_node = 0
# degree_list = None
# removed_edges = None
#
# parent = None
#
#
# def get_parent(idx):
#     global n, center_node, degree_list, removed_edges, parent
#
#     if parent[idx] == idx:
#         return parent[idx]
#     else:
#         parent[idx] = get_parent(parent[idx])
#         return parent[idx]
#
#
# def union(a, b):
#     pa = get_parent(a)
#     pb = get_parent(b)
#     if pa < pb:
#         parent[pb] = pa
#     else:
#         parent[pa] = pb
#
#
# def find(a, b):
#     return get_parent(a) == get_parent(b)
#
#
# def solution(edges):
#     global n, center_node, degree_list, removed_edges, parent
#     answer = []
#
#     # 초기화.
#     for edge in edges:
#         temp = max(edge)
#         node_set.add(edge[0])
#         node_set.add(edge[1])
#         n = max(n, temp)
#
#     degree_list = [[0, 0] for _ in range(n + 1)]
#
#     for u, v in edges:
#         degree_list[u][1] += 1
#         degree_list[v][0] += 1
#
#     for i, degree in enumerate(degree_list):
#         in_d, out_d = degree
#         if in_d == 0 and out_d >= 2:
#             center_node = i
#     # 중심 노드 삭제.
#     removed_edges = []
#     for u, v in edges:
#         if u == center_node or v == center_node:
#             continue
#         removed_edges.append([u, v])
#     # print(*removed_edges)
#
#     # 군집화.
#     parent = [i for i in range(n + 1)]
#     for u, v in removed_edges:
#         if not find(u, v):
#             union(u, v)
#
#     for i in range(1, n + 1):
#         get_parent(i)
#     # print(*parent)
#
#     # node edge 갯수 세기.
#     cnt_dict = dict()
#     for i in range(1, len(parent)):
#         if i == center_node:
#             continue
#         if i not in node_set:
#             continue
#         if parent[i] in cnt_dict:
#             cnt_dict[parent[i]][0] += 1
#         else:
#             cnt_dict[i] = [1, 0]
#
#     for u, v in removed_edges:
#         if parent[u] in cnt_dict:
#             cnt_dict[parent[u]][1] += 1
#     # print(cnt_dict)
#
#     answer = [center_node, 0, 0, 0]
#     for v in cnt_dict.values():
#         cnt_node, cnt_edge = v
#         if cnt_node - cnt_edge == 0:
#             answer[1] += 1
#         elif cnt_node - cnt_edge == 1:
#             answer[2] += 1
#         elif cnt_node - cnt_edge == -1:
#             answer[3] += 1
#     # print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(
#         [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
#          [11, 9], [3, 8]])
