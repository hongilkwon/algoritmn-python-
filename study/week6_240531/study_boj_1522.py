"""
    문자열 교환(투 포인터, 슬라이딩 윈도우)

   a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소값.
   원형이기 때문에, 처음과 끝은 서로 인접해 있는 것

   문자열의 길이는 최대 1_000

   사고과정
   예시 이해하기

   ab ab ab ab ab ab ab a
   3회??? 어떻게 하면 3회만에?

   1회
    *       *
   ab ab ab ab ab ab ab a
   aa ab ab bb ab ab ab a

   2회
       *       *
   aa ab ab bb ab ab ab a
   aa aa ab bb bb ab ab a

   3회
                  *   *
   aa aa ab bb bb ab ab a
   aa aa ab bb bb bb aa a

   ???? 모르겠음.

   슬라이딩 윈도우로 풀기!

   간단하게 생각을 해보면, (aa..aaa)(bbb..b)인 "최종 형태"를 가져야 한다.
   뭘해야 a끼리 뭉칠까!

   예시를 보면, 총 8개의 a가 최종적으로 연속해야 된다.

   8개 짜리 윈도우를 밀어가면서 교환 갯수(윈도우 내부의 b의 갯수), 최소값을 갱신한다.[ ]

   [ab ab ab ab] ab ab ab a
   a[b ab ab ab a]b ab ab a
    .
    .
   ab ab a[b ab ab ab ab a]
   .
   .
   a]b ab ab ab [ab ab ab a --> 3개

   ab ab ab a]b ab ab ab [a
"""

# import sys
#
# input = sys.stdin.readline
#
# s = input().rstrip()
#
# if __name__ == '__main__':
#
#     window_size = 0
#     for c in s:
#         if c == 'a':
#             window_size += 1
#
#     min_cnt = window_size
#     window = []
#     for i in range(len(s)):
#         if i + (window_size - 1) < len(s):
#             window = s[i:window_size + i]
#         else:
#             window = s[i:len(s)] + s[0:window_size - (len(s) - i)]
#
#         cnt = 0
#         for c in window:
#             if c == 'b':
#                 cnt += 1
#         min_cnt = min(min_cnt, cnt)
#
#     print(min_cnt)
