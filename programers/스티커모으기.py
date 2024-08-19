"""
    스티커 모으기.

    원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어,
    뜯어낸 스티커에 적힌 숫자의 "합이 최대"

    양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

    1 이상 <= n <= 100_000

    사고과정.

    [14, 6, 5, 11, 3, 9, 2, 10]

    6  선택한 다면, -> 11 / 3
    11 선택한 다면, -> 9 / 2
    9  선택한 다면, -> 10 /

    모두 양수기 때문에 합이 최대가 되려면,
    특정 수를 선택하면 그이후 2가지 선택지가 있음.
    너무 많은 경우의 수

    --> DP
    table[스티커 번호] = 스티커를 뜯을지 말지 선택할때 최대값

    초기값
    table[0] = sticker[0]

    i를 기준으로 생각해야된다.
    i번째 스티커를 뜯었다면 => table[i] = table[i-2] + sticker[i]
    i번째 스티커를 뜯지 않았다면 => table[i] = table[i-1]

    table[i] = max(sticker[i] + table[i-2], table[i-1])

    그렇다면, 첫번째 스티커는 2가지 경우 모두 필요하기 때문에 table을 2개로 생성한다.

"""


# def solution(sticker):
#     answer = 0
#
#     if len(sticker) == 1:
#         answer = sticker[0]
#         return answer
#
#     # 첫번째 스티커를 뜯은 경우.
#     table1 = [0] * len(sticker)
#     table1[0] = sticker[0]
#     table1[1] = table1[0]
#
#     for i in range(2, len(sticker) - 1):
#         table1[i] = max(sticker[i] + table1[i-2], table1[i-1])
#
#     # 첫번째 스티커를 뜯지 않은 경우.
#     table2 = [0] * len(sticker)
#     for i in range(1, len(sticker)):
#         table2[i] = max(sticker[i] + table2[i-2], table2[i-1])
#
#     answer = max(table1[-2], table2[-1])
#     return answer