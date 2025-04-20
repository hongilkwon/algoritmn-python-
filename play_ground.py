"""
    play_ground


"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

arr = [str(i+1) for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split(' '))

    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp

if __name__ == '__main__':
    arr = [1,2,3,4]
    for idx in range(len(arr)-1, -1, -1):
        print(arr[idx])