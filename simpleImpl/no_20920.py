"""
    영단어 암기는 어려워(정렬, 문자열,string)

   자주 나오는 단어일수록 앞에 배치한다.
   해당 단어의 길이가 길수록 앞에 배치한다.
   알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

    1 <= n <= 100_000
    1 <= m <= 10

    사고과정
    어렵지 않은 문제이며, 단순히 정렬 조건을 여러개지만
    comparator를 직접 작성만 할줄 알면 쉽게 해결가능하다.

    배울점.
    파이썬 다중 정렬하기.
"""

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# str_list = []
# for i in range(n):
#     str_list.append(input().strip())
#
# dic = dict()
#
# if __name__ == '__main__':
#     for s in str_list:
#         if len(s) >= m:
#             if s not in dic:
#                 dic[s] = 1
#             else:
#                 dic[s] += 1
#
#     answer = list(dic.keys())
#     answer.sort(key=lambda x: (-dic[x], -len(x), x))
#
#     for s in answer:
#         print(s)
