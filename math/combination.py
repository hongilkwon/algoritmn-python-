"""
    조합

    1. python 내장
    from itertools import combinations, permutations
    2. 재귀구현 및 3중 반복.

    ** double combination
     combination(n, r, i)
"""

# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# combi_list = ['a', 'b', 'c', 'd','e']
# combi_cnt = 0
#
# ret_list = []
#
# def combination(n, r, start= 0):
#     global combi_list, combi_cnt
#
#     if r == len(ret_list):
#         print(*ret_list)
#         combi_cnt += 1
#         return
#
#     for i in range(start, n):
#         ret_list.append(combi_list[i])
#         combination(n, r, i+1)
#         ret_list.pop()
#
# if __name__ == '__main__':
#     ret = list(combinations(combi_list, 2))
#     print(ret)