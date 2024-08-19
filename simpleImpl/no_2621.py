"""
    카드게임(단순구현)

    카드는 빨간색, 파란색, 노란색, 녹색의 네 가지 색이 있고,
    색깔별로 1부터 9까지 숫자가 쓰여진 카드가 9장씩 있다

    두 가지 이상의 규칙을 적용할 수 있는 경우에는 가장 높은 점수가 카드 게임의 점수

    단순구현이지만, 문제가 천천히 생각을 하고 깐깐하게 구현해야된다.

"""

# import sys
#
# input = sys.stdin.readline
#
# cards = [tuple(input().rstrip().split(" ")) for _ in range(5)]
# cards = list(map(lambda x: (x[0], int(x[1])), cards))
# cards.sort(key=lambda x: x[1])
#
# if __name__ == '__main__':
#     # print(cards)
#
#     max_p = max(cards, key=lambda x: x[1])[1]
#     total_point = 0
#
#     # 1번 규칙(모두 같은 색이면서 숫자가 연속적일 때)
#     if (
#             (cards[0][0] == cards[1][0] and
#              cards[1][0] == cards[2][0] and
#              cards[2][0] == cards[3][0] and
#              cards[3][0] == cards[4][0]) and
#             (cards[0][1] + 1 == cards[1][1] and
#              cards[1][1] + 1 == cards[2][1] and
#              cards[2][1] + 1 == cards[3][1] and
#              cards[3][1] + 1 == cards[4][1])
#     ):
#         total_point = max(max_p + 900, total_point)
#
#     # 2번 규칙(카드 5장 중 4장의 숫자가 같을 때)
#     cnt_dict = dict()
#     for card in cards:
#         num = card[1]
#         if num in cnt_dict:
#             cnt_dict[num] += 1
#         else:
#             cnt_dict[num] = 1
#
#     for k, v in cnt_dict.items():
#         if v == 4:
#             total_point = max(k + 800, total_point)
#
#     # 3번 규칙(3장의 숫자가 같고 나머지 2장도 숫자가 같을 때)
#     if (
#             (cards[0][1] == cards[1][1] and cards[1][1] != cards[2][1]) and
#             (cards[2][1] == cards[3][1] and cards[3][1] == cards[4][1])
#     ):
#         total_point = max(cards[0][1] + cards[2][1] * 10 + 700, total_point)
#     if (
#             (cards[0][1] == cards[1][1] and cards[1][1] == cards[2][1] and cards[2][1] != cards[3][1]) and
#             (cards[3][1] == cards[4][1])
#     ):
#         total_point = max(cards[0][1] * 10 + cards[3][1] + 700, total_point)
#
#     # 4번 규칙(색깔이 모두 같을 때)
#     if (
#             cards[0][0] == cards[1][0] and
#             cards[1][0] == cards[2][0] and
#             cards[2][0] == cards[3][0] and
#             cards[3][0] == cards[4][0]
#     ):
#         total_point = max(max_p + 600, total_point)
#
#     # 5번 규칙(5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500)
#     if (
#             cards[0][1] + 1 == cards[1][1] and
#             cards[1][1] + 1 == cards[2][1] and
#             cards[2][1] + 1 == cards[3][1] and
#             cards[3][1] + 1 == cards[4][1]
#     ):
#         total_point = max(max_p + 500, total_point)
#
#     # 6번 규칙(카드 5장 중 3장의 숫자가 같을 때)
#     for k, v in cnt_dict.items():
#         if v == 3:
#             total_point = max(k + 400, total_point)
#     # 7번 규칙(2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때)
#     num1 = 0
#     num2 = 0
#     for k, v in cnt_dict.items():
#         if num1 == 0 and num2 == 0 and v == 2:
#             num1 = k
#         elif num1 != 0 and num2 == 0 and v == 2:
#             num2 = k
#     if num1 != 0 and num2 != 0:
#         if num1 > num2:
#             total_point = max(num1*10 + num2 + 300, total_point)
#         else:
#             total_point = max(num1 + num2*10 + 300, total_point)
#
#     # 8번 규칙(2장의 숫자가 같을 때)
#     for k, v in cnt_dict.items():
#         if v == 2:
#             total_point = max(k + 200, total_point)
#
#     total_point = max(max_p + 100, total_point)
#     print(total_point)