"""
    과일 탕후루(*투포인터)

    막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다

    1 <= n <= 20 0000

    * 2개의 종류의 과일로 이루어진 최대 길이를 구하자

    dic => 구간의 과일의 종류별 카운팅
    1: 2
    2: 1
    5: 0

           r
      l
  5 5 1 1 2 1

"""

# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split(' ')))
#
# if __name__ == '__main__':
#     max_length = 0
#     dic = defaultdict(int)
#
#     # 투포인터
#     left, right, fruit_type_cnt = 0, 0, 0
#
#     # while right < n:
#     #     ...
#     #     right += 1
#
#     for right in range(n):
#         # 한번도 사용하지 않은 과일,
#         if dic[arr[right]] == 0:
#             fruit_type_cnt += 1
#         dic[arr[right]] += 1
#
#         # 사용된 과일의 종류가 2개 이상 (구현)
#         while fruit_type_cnt > 2:
#             dic[arr[left]] -= 1
#             if dic[arr[left]] == 0:
#                 fruit_type_cnt -= 1
#             left += 1
#
#         max_length = max(max_length, right - left + 1)
#         # right += 1
#
#     print(max_length)
