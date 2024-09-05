"""
    다음 큰 숫자(수학, 이진법)

    78(1001110)
    83(1010011)

    2진법으로 바꿔가면서 1의 개수가 가장 같은것을 찾는다.

    4/2 0
    2/2 0
    1

    9/2 1
    4/2 0
    2/2 1
    1

"""


# def to_binary_num(n):
#     ret = ''
#     while n != 0:
#         ret = str(n % 2) + ret
#         n = n // 2
#
#     return ret
#
#
# def solution(n):
#     answer = 0
#
#     cnt_1 = 0
#     for c in to_binary_num(n):
#         if c == '1':
#             cnt_1 += 1
#
#     while True:
#         n += 1
#         temp = 0
#         for c in to_binary_num(n):
#             if c == '1':
#                 temp += 1
#
#         if cnt_1 == temp:
#             answer = n
#             break
#
#     print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(78)
