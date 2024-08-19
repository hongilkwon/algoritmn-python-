"""
   주유소(단순구현)

   N(2 ≤ N ≤ 100,000)

   제일 왼쪽 도시부터 제일 오른쪽 도시까지의 거리 1이상 1_000_000_000 이하의 자연수

    사고과정.

    가장 저렴한 도시에서 미리 기름을 산다면? 최소비용으로 도착할 수 있다.

    배울점.
    단순구현 문제지만 정답률이 낮은걸로 봐서 조금 천천히 생각을 해야 풀 수 있다.
"""

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# lengthList = list(map(int, input().split()))
# cityList = list(map(int, input().split()))
#
# if __name__ == '__main__':
#
#     price = cityList[0]
#     totalPrice = price * lengthList[0]
#
#     for i in range(1, len(cityList) - 1):
#         if price > cityList[i]:
#             price = cityList[i]
#         totalPrice += price * lengthList[i]
#
#     print(totalPrice)