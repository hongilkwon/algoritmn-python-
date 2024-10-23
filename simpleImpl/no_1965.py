"""
    상자넣기(LIS)

     앞에 있는 상자의 크기가 뒤에 있는 상자의 크기보다 작으면, 앞에 있는 상자를 뒤에 있는 상자 안에 넣을 수가 있다.
     한 번에 넣을 수 있는 최대의 상자 개수를 출력

     상자의 개수 n (1 ≤ n ≤ 1000)

     LIS(최장증가 부분 수열)


"""


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split(' ')))
#
# LIS_TABLE = [0] * n
#
# if __name__ == '__main__':
#     for i in range(n):
#         temp_max = 0
#         for j in range(i):
#             # 현재 숫자(arr[i]) 보다 작으면서 LIS_TABLE[j] 보다 temp가 작다면 갱신.
#             if (arr[i] > arr[j]) and (LIS_TABLE[j] > temp_max):
#                 temp_max = LIS_TABLE[j]
#         LIS_TABLE[i] = temp_max + 1
#
#     print(max(LIS_TABLE))