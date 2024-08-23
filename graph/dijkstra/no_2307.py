"""
    도로검문(dijkstra, tracking)

    도로는 모두 양방향이라고 가정

    용의자는 도시를 가장 빠른 시간 내에 빠져나가고자 한다
    경찰이 어떤 하나의 도로(에지)를 선택하여 이 도로에서 검문을 하려고 한다
    경찰이 검문을 위하여 선택하는 도로에 따라서 용의자의 가장 빠른 탈출시간은 검문이 없을 때에 비하여 더 늘어날 수 있다.

    도로검문을 통하여 얻을 수 있는 탈출의 최대 지연시간을 계산

    입력 도시의 도로망에 따라서 경찰이 어떤 도로를 막으면 용의자는 도시를 탈출하지 못할 수도 있다.
    이 경우 검문으로 인하여 지연시킬 수 있는 탈출시간은 무한대이다. 이 경우에는 -1을 출력해야 한다.

    정수 N(6 ≤ N ≤ 1000)과 도로의 수 M(6 ≤ M ≤ 5000)

    사고과정

    용의자가 1번 정점에서 n번 정점까지 가는 데에 쓰인 간선 중에서만 검문

"""

import sys
import heapq


input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = [list() for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

INF = 1_000_000_000
dist = [INF for _ in range(n + 1)]

# tracking[도착지] = 출발지
tracking = [0 for _ in range(n + 1)]


def dijkstra(start, blocked):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, u = heapq.heappop(q)

        if dist[u] < d:
            continue

        for next in adj_list[u]:
            v, w = next

            if (u, v) == blocked:
                continue

            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

                if blocked == (-1, -1):
                    tracking[v] = u
                heapq.heappush(q, (dist[v], v))


def print_tracking(v):

    if tracking[v] == 0:
        return

    print_tracking(tracking[v])
    print(tracking[v], '->', v)


if __name__ == '__main__':
    dijkstra(1, (-1, -1))
    min_dist = dist[n]
    #print_tracking(n)

    answer = 0
    destination = n

    while tracking[destination] != 0:

        dist = [INF for _ in range(n + 1)]
        dijkstra(1, (tracking[destination], destination))
        blocked_dist = dist[n]

        if blocked_dist == INF:
            answer = -1
            break

        answer = max(answer, blocked_dist - min_dist)
        destination = tracking[destination]

    print(answer)