"""
    공 넣기(브론즈, 단순 구현)

    바구니 N개
    1-n

    가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

    m번 공을 넣으려고한다.


     도현이는 한 번 공을 넣을 때,
     1. 공을 넣을 바구니 범위를 정하고,
     공을 넣을 바구니는 연속되어 있어야 한다.

     2.정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.

     M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성
"""

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(' '))
#
# # 바구니
# arr = ['0' for _ in range(n)]
#
# for _ in range(m):
#     i, j, k = map(int, input().split(' '))
#     for idx in range(i-1, j):
#         arr[idx] = str(k)
#
# if __name__ == '__main__':
#     print(' '.join(arr))
