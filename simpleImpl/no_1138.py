"""
    한 줄로 서기 (greedy)

     자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다
     사람들의 키는 1부터 N까지 모두 다르다.

     N은 10보다 작거나 같은 자연수

     사고과정


     1 2 3 4
     2 1 1 0

     줄을선 순서 => 4 2 1 3

     키순서대로 섰다면?
     1 2 3 4
     0 0 0 0

     4명중에
     1cm => 자신 보다 작은 사람 0명  큰 것이 2개 있다 -2
     2cm => 자신 보다 작은 사람 1명  큰 것이 1개 있다 0
     3cm => 자신 보다 작은 사람 2명  큰 것이 1개 있다 1, 0
     4cm => 자신 보다 작은 사람 3명  큰 것이 0개 있다 3, 2, 1, 0

     n이 충분히 작다...
     2중 반복문
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# if __name__ == '__main__':
#
#     order = [0 for _ in range(n)]
#
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             # 비어있는 자리의 갯수와 내 앞의 큰 사람의수가 같다면,
#             if cnt == arr[i] and order[j] == 0:
#                 order[j] = i + 1
#                 break
#             # 비어있는 자리라면
#             if order[j] == 0:
#                 cnt += 1
#     print(*order)