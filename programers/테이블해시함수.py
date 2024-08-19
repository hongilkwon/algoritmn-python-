"""
    테이블 해시 함수

    플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되,
    "만약 그 값이 동일"하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬

    S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 "나머지들의 합"으로 정의

    S_i를 누적하여 bitwise XOR 한 값을 해시 값


    1 ≤ data[i][j] ≤ 1,000,000

    사고과정.

    그냥 문제 설명대로 단순 구현 하면됨.
"""

# r = 0
# c = 0
#
#
# def solution(data, col, row_begin, row_end):
#     answer = 0
#     global r, c
#
#     r = len(data)
#     c = len(data[0])
#
#     data.sort(key=lambda x: (x[col - 1], -x[0]))
#
#     s_list = []
#     for i in range(r):
#         sum = 0
#         for j in range(c):
#             sum += data[i][j] % (i + 1)
#         s_list.append(sum)
#
#     total_sum = s_list[row_begin - 1]
#     for i in range(row_begin, row_end):
#         print(total_sum, s_list[i])
#         total_sum = total_sum ^ s_list[i]
#
#     answer = total_sum
#     return answer
