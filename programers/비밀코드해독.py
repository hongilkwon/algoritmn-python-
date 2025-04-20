"""
    비밀코드 해독(단순구현)
    시스템은 1부터 n까지의 서로 다른 정수 5개가 오름차순으로 정렬된 비밀 코드를 가지고 있으며

    m번의 시도를 할 수 있습니다. 각 시도마다 서로 다른 5개의 정수를 입력하면,
    시스템은 그 중 몇 개가 비밀 코드에 포함되어 있는지 알려줍니다.


    10 ≤ n ≤ 30
    1 ≤ (q의 길이 = m) ≤ 10

    30C5 = 142,506

    14만 * 10

"""

# from itertools import combinations
#
#
# def solution(n, q, ans):
#     answer = 0
#     arr = [i for i in range(1, n + 1)]
#     case_list = list(combinations(arr, 5))
#
#     for c in case_list:
#         flag = True
#
#         for i, test in enumerate(q):
#             tmp = 0
#
#             for j in range(5):
#                 if c[j] in test:
#                     tmp += 1
#
#             if tmp != ans[i]:
#                 flag = False
#                 break
#
#         if flag:
#             answer += 1
#
#     return answer


if __name__ == '__main__':
    solution(
        n=10,
        q=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],
        ans=[2, 3, 4, 3, 3]
    )

    solution(
        n=15,
        q=[[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]],
        ans=[2, 1, 3, 0, 1]
    )
