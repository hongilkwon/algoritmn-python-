"""
    줄세우기(LIS.. 최장증가부분 수열)

    선생님은 아이들을 효과적으로 보호하기 위해 목적지까지 번호순서대로 "일렬"로 서서 걸어가도록 하였다
    이동 도중에 보니 아이들의 번호순서가 바뀌었다.

    아이들이 혼란스러워하지 않도록 하기 위해 위치를 옮기는 아이들의 수를 최소

    사고과정.

    3 7 5 2 6 1 4

    전체 갯수에서 - 이미 줄을 제대로 서 있는 애들

    이미 줄을 제대로 서 있다는 것 => LIS(최장증가부분 수열)

"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# LIS_table = [0] * n
#
# if __name__ == '__main__':
#     for i in range(n):
#         temp_max = 0
#         for j in range(i):
#             if (arr[i] > arr[j]) and LIS_table[j] > temp_max:
#                 temp_max = LIS_table[j]
#         LIS_table[i] = temp_max + 1
#
#     print(n - max(LIS_table))
