"""
    숫자블록(정수론)

    1 ≤ begin ≤ end ≤ 1_000_000_000

    사고과정.
    결국 그 블록에 써질것은...
    그 블록의 자신을 제외한 가장 큰 약수.

    범위가 end - begin ≤ 5_000 이기 때문에,
    완전탐색
"""


# import math
#
#
# def cal_yaksu(n):
#     temp = set()
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             if i <= 10_000_000:
#                 temp.add(i)
#             if i != 1:
#                 a = n // i
#                 if a <= 10_000_000:
#                     temp.add(a)
#
#     return list(temp)
#
#
# def solution(begin, end):
#     answer = []
#
#     for num in range(begin, end + 1):
#         if num == 1:
#             answer.append(0)
#         else:
#             ret = cal_yaksu(num)
#             answer.append(max(ret))
#
#     return answer
#
#
# if __name__ == '__main__':
#     pass

