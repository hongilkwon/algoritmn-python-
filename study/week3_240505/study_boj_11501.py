
"""
    주식

    - 주식 하나를 산다.(사는건 1개만 됨)
    - 원하는 만큼 가지고 있는 주식을 판다.(파는건 다팜)
    - 아무것도 안한다.


    (2 ≤ N ≤ 1,000,000)

    사고과정

    기본적으로 저렴할때 사서 가장 비쌀때 매도 해야 최대 이익을 받을 수 있음.
    즉, 자신이 주식을 구매한 날 이후에 가격이 단 1이라도 오른다면 최대 수익에 도움이된다 는것,

    1. 완전탐색(불가능함)
    N이 100만이라 각각 주식이 언제 최고점에 팔지는 알수 있지만, 2중 반복문 때문에 너무 많은 시간초과

    2.탐욕법

    무엇을 기준으로?

    - 날짜별로 주식의 가격이 정해져 있기 때문에 정렬 및 priority Queue를 사용할 수 없다.
    - 단, 모든 미래의 주식 가격을 알수 있다.
      역순으로 탐색을해서(미래 --> 과거) 미래의 최대값 보다 싸면 구매, 그렇지 않으면, 구매하지 않음.

    배울점
    - 미래를 전부 알수있다면??? 이런 표현이 있다면, 역탐색을 한번 고려해보자!
    - 파이썬 list 역탐색 문법

"""

# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# if __name__ == '__main__':
#
#     for _ in range(tc):
#
#         n = int(input())
#         arr = list(map(int, input().split()))
#
#         answer = 0
#         max_price = 0
#         for i in range(len(arr) - 1, -1, -1):
#             if arr[i] >= max_price:
#                 max_price = arr[i]
#             else:
#                 answer += max_price - arr[i]
#         print(answer)
