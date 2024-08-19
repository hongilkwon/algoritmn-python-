"""
    친구비

    학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다!
    준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다.

    “친구의 친구는 친구다”를 이용

    사람 수 N (1 ≤ N ≤ 10_000)
    친구관계 수 M (0 ≤ M ≤ 10_000)
    가지고 있는 돈 k (1 ≤ k ≤ 10_000_000)

    자기 자신과 친구일 수도 있고, 같은 친구 관계가 여러 번 주어질 수도 있다

    사고과정.


"""

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
cost_list = [0] + list(map(int, input().split()))
relations = [tuple(map(int, input().split())) for _ in range(m)]

arr = [i for i in range(n + 1)]


def get_parent(n):
    if n != arr[n]:
        arr[n] = get_parent(arr[n])
    return arr[n]


def union(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)

    if parent_a < parent_b:
        arr[parent_b] = parent_a
    else:
        arr[parent_a] = parent_b


def find(a, b):
    if get_parent(a) == get_parent(b):
        return True
    else:
        return False


if __name__ == '__main__':

    for relation in relations:
        u, v = relation
        union(u, v)

    # 분리 집합이 최상위 부모 1개로 통일 되지 않았기 때문.
    for i in range(1, n + 1):
        get_parent(i)

    temp = dict()
    for i in range(1, len(arr)):
        if arr[i] in temp:
            temp[arr[i]].append(i)
        else:
            temp[arr[i]] = list()
            temp[arr[i]].append(i)
    # print(temp)

    total_cost = 0
    for key, value in temp.items():
        min_cost = 10_000_001
        for i in value:
            min_cost = min(min_cost, cost_list[i])
        total_cost += min_cost

    if total_cost > k:
        print("Oh no")
    else:
        print(total_cost)
