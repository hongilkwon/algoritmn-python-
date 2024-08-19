"""
    스타트 링크

    지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동
    (U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

     G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.

     1 ≤ S, G ≤ F ≤ 1_000_000
     0 ≤ U, D ≤ 1_000_000

    S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값

    사고과정.

    예시)
    1층에서 10층, 위로2 아래로 1

    6번
    1 -> 3 -> 5 -> 7 -> 9 -> 8 -> 10

    각층을 노드 표현하고, bfs 탐색을 조진다.

"""


# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# F, S, G, U, D = map(int, input().split())
#
# visited = [0 for _ in range(F + 1)]
# directions = [U, -D]
#
#
# def go(start):
#     q = deque()
#     q.append(start)
#     visited[start] = 1
#
#     while q:
#         node = q.popleft()
#         for dir in directions:
#             next = node + dir
#             if next < 1 or next > F:
#                 continue
#             if visited[next] > 0:
#                 continue
#
#             visited[next] = visited[node] + 1
#             q.append(next)
#
#
# if __name__ == '__main__':
#     go(S)
#     # print(*visited)
#
#     if visited[G] == 0:
#         print("use the stairs")
#     else:
#         print(visited[G] - 1)
