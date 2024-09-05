"""
    순열

    1. python 내장
    from itertools import combinations, permutations
    2.

    ** double permutation
    is_selected = [False for _ in range(5)]를  없애면 됨.
"""

# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# permu_list = ['a', 'b', 'c', 'd','e']
# permu_cnt = 0
#
# is_selected = [False for _ in range(5)]
# ret_list = []
#
# def permutation(n, r):
#     global permu_list, permu_cnt
#
#     if r == len(ret_list):
#         print(*ret_list)
#         permu_cnt += 1
#         return
#
#     for i in range(n):
#         if is_selected[i]: continue
#
#         ret_list.append(i)
#         is_selected[i]= True
#         permutation(n, r)
#
#         ret_list.pop()
#         is_selected[i] = False
#
# if __name__ == '__main__':
#     # permutation(5, 2)
#     # print(permu_cnt)
#     ret = list(permutations(permu_list, 2))
#     print(ret)
#     print(len(ret))