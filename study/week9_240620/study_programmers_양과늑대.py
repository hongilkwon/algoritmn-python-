"""
    양과 늑대(완탐, 백트레킹, 재귀)

    2진 트리 모양
    "루트 노드에서 출발"
    노드를 방문할 때 마다 "해당 노드에 있던 양과 늑대가 당신을 따라오게" 됩니다
    모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다

    양이 늑대에게 잡아먹히지 않도록 하면서 "최대한 많은 수의 양"

    2 ≤ info의 길이 ≤ 17

   0은 양
    1은 늑대

    edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태

    사고과정.    

    2진 "트리"다.
    - 사이클이 없다.
    - 무조건 한점에서 다른점으로 갈수 있다.

    info의 길이! 노드의 개수 17개 -> 전부 돌 수있다. 
    길을 존나 중복해서 가도 됨 -> 완전탐색

    양 의수 <= 늑대의 수 --> 잡아먹음(백트레킹)

    재귀 구현시 어떻게 종료할 것인가???

    1. "visited[node][sheep_cnt][wolf_cnt]"
    -> 노드를 특정 양과 늑대를 따라 다니게 하고 방문하는 경우는 1번 뿐이다!!

    2. 이미 지나갔던 정점은 생각해봤을 때, 다시 방문하더라도,아무런 변화가 없다.
       1번 방문시에 정점에 있던 동물이 따라오고, 탐색이 끝날 때 까지 계속 따라 다닌다.
       같은 정점을 다시 방문해도 결국에는, 아무런 의미가 없습니다.
"""

# solution_1
# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# node_animal = []
# adj_list = [[] for _ in range(17)]
#
# visited = [[[False for wolf_cnt in range(18)] for sheep_cnt in range(18)] for node in range(17)]
#
# # 최소 0마리 양(루트)에서 시작하여 최대값 갱신.
# max_sheep_cnt = 0
#
#
# def go(node, sheep_cnt, wolf_cnt):
#     global node_animal, adj_list, max_sheep_cnt
#
#     if visited[node][sheep_cnt][wolf_cnt]:
#         return
#     visited[node][sheep_cnt][wolf_cnt] = True
#
#     # 현재 노드에서 동물을 데리고 감.
#     new_sheep_cnt = sheep_cnt
#     new_wolf_cnt = wolf_cnt
#
#     animal = node_animal[node]
#     if animal == 0:
#         new_sheep_cnt += 1
#     elif animal == 1:
#         new_wolf_cnt += 1
#
#     # 현재 노드의 동물을 데리고 다님을 -1로 표기.
#     node_animal[node] = -1
#
#     if new_sheep_cnt > new_wolf_cnt:
#         max_sheep_cnt = max(max_sheep_cnt, new_sheep_cnt)
#         for next in adj_list[node]:
#             go(next, new_sheep_cnt, new_wolf_cnt)
#
#     visited[node][sheep_cnt][wolf_cnt] = False
#     node_animal[node] = animal
#
#
# def solution_1(info, edges):
#     answer = 0
#     global node_animal, adj_list, max_sheep_cnt
#
#     node_animal = info
#     for edge in edges:
#         u, v = edge
#         adj_list[u].append(v)
#         adj_list[v].append(u)
#
#     go(0, 0, 0)
#     answer = max_sheep_cnt
#     return answer

# solution_2
# import sys
#
# sys.setrecursionlimit(10 ** 8)
#
# adj_list = [[] for _ in range(17)]
# node_animal = []
#
# max_sheep_cnt = 0
#
#
# def go(node, sheep_cnt, wolf_cnt, possible):
#     global node_animal, adj_list, max_sheep_cnt
#
#     # 현재 노드의 양/늑대 확인 후 카운팅
#     animal = node_animal[node]
#     if animal == 0:
#         sheep_cnt += 1
#     elif animal == 1:
#         wolf_cnt += 1
#
#     if sheep_cnt <= wolf_cnt:
#         return
#
#     # 최댓값 갱신.
#     max_sheep_cnt = max(max_sheep_cnt, sheep_cnt)
#
#     # 현재 노드에서 다음에 갈 수 있는 노드를 추가해 준다....
#     possible = possible + adj_list[node]
#     for next in possible:
#         go(next, sheep_cnt, wolf_cnt, [node for node in possible if node != next])
#
#
# def solution_2(info, edges):
#     answer = 0
#     global node_animal, adj_list, max_sheep_cnt
#     node_animal = info
#
#     for u, v in edges:
#         adj_list[u].append(v)
#
#     go(0, 0, 0, [])
#     answer = max_sheep_cnt
#     return answer
#
#
# if __name__ == '__main__':
#     # ret_1 = solution_1([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#     #                    [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
#     # print(ret_1)
#
#     ret_2 = solution_2([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#                        [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
#     print(ret_2)
