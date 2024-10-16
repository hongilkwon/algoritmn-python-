"""
    기적의 매매법(단순구현)

    준현이
    - 주식을 살수 있는 가격에 많이산다

    성민이
    - 모든 거래는 전량 매수와 전량 매도
    - 빚을 내서 주식을 하지는 않는다.

    현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도한다. 전일과 오늘의 주가가 동일하다면 가격이 상승한 것이 아니다.


    자산은 (현금 + 1월 14일의 주가 × 주식 수)로 계산
"""


# import sys
#
# input = sys.stdin.readline
#
# init_money = int(input())
#
# jun_money = init_money
# jun_stock_cnt = 0
#
# sung_money = init_money
# sung_stock_cnt = 0
#
# prices = list(map(int, input().split(" ")))
#
#
# if __name__ == '__main__':
#
#     g = 0
#     for i in range(len(prices)):
#         price = prices[i]
#
#         # 준현 매매
#         if jun_money >= price:
#             jun_stock_cnt += jun_money // price
#             jun_money = jun_money % price
#
#         # 성민 매매
#         if i >= 3:
#             if (prices[i] > prices[i-1]) and (prices[i-1] > prices[i-2]) and (prices[i-2] > prices[i-3]):
#                 sung_money += sung_stock_cnt * price
#
#             if (prices[i] < prices[i-1]) and (prices[i-1] < prices[i-2]) and (prices[i-2] < prices[i-3]):
#                 if sung_money >= price:
#                     sung_stock_cnt = sung_money // price
#                     sung_money = sung_money % price
#
#
#     jun_ret = jun_money + jun_stock_cnt * prices[-1]
#     sung_ret = sung_money + sung_stock_cnt * prices[-1]
#
#     if jun_ret > sung_ret:
#         print("BNP")
#     elif jun_ret < sung_ret:
#         print("TIMING")
#     else:
#         print("SAMESAME")