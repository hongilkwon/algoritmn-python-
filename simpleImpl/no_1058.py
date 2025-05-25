"""
    친구(플로이드)
    * 경로 찾기

    어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선,

    A - B

    1. 두 사람이 친구이거나
    2. A와 친구이고, B와 친구인 C가 존재

    구하고자 하는것: 가장 유명한 사람은 2-친구의 수가 가장 많은 사람

    예시)

    3
    NYY   NYY
    YNY   YNY
    YYN   YYN

    011  011
    101  101
    110  110

    211
    121
    112

    A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.
    N은 50보다 작거나 같은 자연수
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# friends = [list(input().rstrip()) for _ in range(n)]
#
# if __name__ == '__main__':
#     two_friends = [[0 for _ in range(n)] for _ in range(n)]
#
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     two_friends[i][j] = 0
#                     continue
#                 if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
#                     two_friends[i][j] = 1
#
#     answer = 0
#     for e in two_friends:
#         answer = max(e.count(1), answer)
#     print(answer)
