"""
    올림픽(정렬)

    금메달 수가 더 많은 나라
    금메달 수가 같으면, 은메달 수가 더 많은 나라
    금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

    한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의

"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = []

for i in range(n):
    idx, g, s, b = map(int, input().split())
    arr.append((idx, g, s, b))

if __name__ == '__main__':

    arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    # print(arr)

    # rank_arr[num] = rank
    rank_arr = [-1 for _ in range(n + 1)]
    rank_arr[arr[0][0]] = 1

    rank = 1
    cnt = 1
    prev = (arr[0][1], arr[0][2], arr[0][3])
    for i in range(1, len(arr)):
        num, g, s, b = arr[i]
        if (g, s, b) == prev:
            rank_arr[num] = rank
            cnt += 1
        else:
            rank += cnt
            rank_arr[num] = rank
            cnt = 1
            prev = (g, s, b)

    # print(rank_arr)
    print(rank_arr[k])
