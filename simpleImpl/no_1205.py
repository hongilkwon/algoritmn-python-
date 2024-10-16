"""
    등수 구하기(정렬)

    보통 위에서부터 몇 번째 있는 점수인지로 결정한다. 하지만, 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수

    만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.


    10 <= P <= 50
    N은 0보다 크거나 같고, P보다 작거나 같은 정수
    0 <= N <= P <= 50

    0 <= 점수 <=2,000,000,000
"""


# import sys
#
# input = sys.stdin.readline
#
# n, my_point, p = map(int, input().split())
# tmp = list(map(int, input().split()))
# #tmp.sort(reverse= True)
#
# rank_list = [-1 for _ in range(p)]
# for i, num in enumerate(tmp):
#     rank_list[i] = num
#
# if __name__ == '__main__':
#
#     if rank_list[-1] != -1 and rank_list[-1] >= my_point:
#         print(-1)
#         exit(0)
#
#     cnt = 1
#     for i in range(len(rank_list)):
#         if rank_list[i] > my_point:
#             cnt += 1
#         else:
#             break
#     print(cnt)