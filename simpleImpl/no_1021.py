"""
    회전하는 큐(구현, 큐)

    첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
    왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
    오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.


    예시)
    10 3
    2 9 5

    왼쪽 1번
    2 3 4 5 6 7 8 9 10 1
    3 4 5 6 7 8 9 10 1

    오른쪽 3번
    9 10 1 3 4 5 6 7 8
    10 1 3 4 5 6 7 8

    오른쪽4번? 왼쪽4번?
    5 6 7 8 10 1 3 4
    6 7 8 10 1 3 4

    총 8


    1 2 3 4 5 .. (n/2) .. n-2, n-1, n
"""

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(' '))
#
# q = deque()
# for i in range(1, n + 1):
#     q.append(i)
#
# position = list(map(int, input().split(' ')))
#
# if __name__ == '__main__':
#     cnt = 0
#     for p in position:
#         if q.index(p) <= len(q) / 2:
#             left_rotate_cnt = q.index(p)
#             q.rotate(-left_rotate_cnt)
#             cnt += left_rotate_cnt
#         else:
#             right_rotate_cnt = len(q) - q.index(p)
#             q.rotate(right_rotate_cnt)
#             cnt += right_rotate_cnt
#         q.popleft()
#
#     print(cnt)


# def rotate_left(q, p):
#     left_cnt = 0
#
#     while p != q[0]:
#         temp = q.popleft()
#         q.append(temp)
#         left_cnt += 1
#
#     return left_cnt
#
#
# def rotate_right(q, p):
#     right_cnt = 0
#
#     while p != q[0]:
#         temp = q.pop()
#         q.appendleft(temp)
#         right_cnt += 1
#
#     return right_cnt
#
#
# if __name__ == '__main__':
#     cnt = 0
#     for p in position:
#         left_q = deque(q)
#         left_cnt = rotate_left(left_q, p)
#
#         right_q= deque(q)
#         right_cnt = rotate_right(right_q, p)
#
#         if left_cnt >= right_cnt:
#             cnt += right_cnt
#             q = right_q
#         else:
#             cnt += left_cnt
#             q = left_q
#
#         q.popleft()
#     print(cnt)
