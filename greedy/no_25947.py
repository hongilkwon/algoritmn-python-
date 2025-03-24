"""
    선물할인(누적합, 구간합, 이분탐색)

    n개의 선물,
    b의 예산으로
    a개의 반값할인 적용
    (단, 선물당 1번만 반값할인)

    최대로 살 수 있는 선물의 수

    n 10만. => 정렬가능
    단순구현

    반례)
    3 3 3
    2 2 2

    윈도우 슬라이딩??
    - 갯수가 정해져 있지 않음 => 불가능.

    구간합을 미리 연산하기. + 반값을 적용한 가격확인
    이분탐색
"""

# import sys
#
# input = sys.stdin.readline
#
# # n(선물의 개수) b(예산) a(할인 가능한 선물의 개수)
# n, b, a = map(int, input().split(' '))
#
# # 정렬.
# price_list = list(map(int, input().split(' ')))
# price_list.sort()
#
# # 누적합
# cumulative_list = [0] * len(price_list)
#
# cumulative_list[0] = price_list[0]
# for i in range(1, len(price_list)):
#     cumulative_list[i] = cumulative_list[i - 1] + price_list[i]
#
#
# # 선물갯수(count)가 예산을 벗어나지 않는지 확인.
# def chk(cnt):
#     idx = cnt - 1
#     total_price = 0
#
#     if cnt > a:
#         discount = (cumulative_list[idx] - cumulative_list[idx - a]) / 2
#         total_price = discount + cumulative_list[idx - a]
#     else:
#         total_price = cumulative_list[idx] / 2
#
#     if b >= total_price:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     answer = 0
#
#     left = 0
#     right = n
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if chk(mid):
#             answer = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(answer)

# 실패한 풀이.
# if __name__ == '__main__':
#     cnt = 0
#
#     for price in price_list:
#         if price <= a:
#             a -= price
#             cnt += 1
#         else:
#             if b > 0 and (price/2) <= a:
#                 a -= (price/2)
#                 b -= 1
#                 cnt += 1
#             else:
#                 break
#
#     print(cnt)
