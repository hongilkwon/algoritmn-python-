"""
    2개 이하로 다른 비트

    f(x) => x보다 크고 x와 비트가 1~2개 다른 수들 중에서 "제일 작은 수"

    f(2) => 11 (3)

    f(7) =>
     111
    1011

    1 ≤ numbers의 길이 ≤ 100_000
    0 ≤ numbers의 모든 수 ≤ 1000_000_000_000_000 ???

    사고과정

    비트가 2이하로 다르면서 가장 작은수??

    1. 두수를 XOR 연산후 1이 2이하면?
    -> 시간초과.

    2. number
    짝수라면 XXXXXX0 마지막 비트가 0이기 때문에 여기를 1증가 시킨다.

    홀수라면 XXXXXX1 마지막 비트가 1이기 때문에 최소 1이 커지면,
    순차적으로 자릿수가 증가하고, xxxx01111 오른쪽부터 탐색시 최초로 0이 1이 되면서 xxxx10'000'이 되고
    xxxx10'000' 2개 초과된 비트가 바꼈을 수 있기 때문에, 최솟값은 xxxx10'111'이된다.

    즉 오른쪽으로 탐색시 최초 "01" 이 나오면 "01" => "10"으로 바꾼다.

    * format(num, 'b') 이진수 10진수 num을 string Type 2진수로 반환.
      str.count('1') string 내의 요소 갯수 세기.

    * 2-16진수 변환 함수 외우기.
    def convert(num, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(num, base)

        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
"""


# def convert(num, base):
#     arr = "0123456789ABCDEF"
#     q, r = divmod(num, base)
#
#     if q == 0:
#         return arr[r]
#     else:
#         return convert(q, base) + arr[r]
#
#
# def solution(numbers):
#     answer = []
#
#     for num in numbers:
#         if num % 2 == 0:
#             answer.append(num + 1)
#         else:
#             binary_num = format(num, 'b')
#             flag = True
#             for i in range(len(binary_num) - 1, -1, -1):
#                 if binary_num[i] == '0':
#                     binary_num = binary_num[0:i] + '10' + binary_num[i + 2:]
#                     flag = False
#                     break
#             if flag:
#                 binary_num = '10' + binary_num[1:]
#
#             answer.append(int(binary_num, 2))
#     # print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution([2, 7])

# 시간초과
# def solution(numbers):
#     answer = []
#
#     for num in numbers:
#
#         i = 1
#         while True:
#             ret = num ^ num + i
#             cnt = format(ret, 'b').count('1')
#             if 0 < cnt <= 2:
#                 answer.append(num + i)
#                 break
#             i += 1
#     return answer
