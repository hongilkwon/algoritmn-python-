"""
     단품메뉴들을 조합해서 코스요리 메뉴로 구성

     이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
     코스요리 메뉴는 "최소 2가지 이상"의 단품메뉴로 구성
     "최소 2명 이상"의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함


     각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders
     구성하는 단품메뉴들의 "갯수"가 담긴 배열 course가

     2 <= order <= 20
     1 <= course <= 10

     사고과정.

     제한 숫자가 작기 때문에 충분히 완전탐색이 가능해보인다.

     1. 각 주문의 원소를 오름차순으로 정렬한다.
     2. 2개, 3개, 4개 조합으로 cnt_map으로 카운팅한다.
     3. 후보를 세서 결과에 넣고 오름차순을 정렬한다.

"""

# import sys
#
# input = sys.stdin.readline
#
# from itertools import combinations
#
#
# def solution(orders, course):
#     answer = []
#
#     sorted_orders = []
#     for str in orders:
#         temp = list(str)
#         temp.sort()
#         sorted_orders.append(temp)
#     # print("sorted_orders:", sorted_orders)
#
#     for num in course:
#         cnt_dict = dict()
#         for order in sorted_orders:
#             combi_ret = list(combinations(order, num))
#             # print(combi_ret)
#
#             for e in combi_ret:
#                 new_course = ""
#                 for c in e:
#                     new_course += c
#
#                 if new_course in cnt_dict:
#                     cnt_dict[new_course] += 1
#                 else:
#                     cnt_dict[new_course] = 1
#
#         if not cnt_dict:
#             continue
#
#         max_cnt = max(cnt_dict.values())
#         for k, v in cnt_dict.items():
#             if v >= 2 and v == max_cnt:
#                 answer.append(k)
#
#     answer.sort()
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(["XYZ", "XWY", "WXA"],[2,3,4])
