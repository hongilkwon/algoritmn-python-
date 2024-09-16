"""
    이친수

    이친수는 0으로 시작하지 않는다.
    이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.


    1 10 100 1000 10000
                  10001

             1001 10010

         101 1010 10100
                  10101
"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# # [자릿수][끝수]
# table = [[0,0] for _ in range(91)]
#
#
# if __name__ == '__main__':
#
#     table[1][0] = 0
#     table[1][1] = 1
#
#     for i in range(2, n + 1):
#         table[i][0] = table[i-1][1] + table[i-1][0]
#         table[i][1] = table[i-1][0]
#
#     answer = table[n][0] + table[n][1]
#     print(answer)