"""
    가희와 키워드

    지금까지 메모장에 써진 키워드는 모두 서로 다르며, 총 N개가 존재

    1 ≤ N ≤ 2×10^5
    1 ≤ M ≤ 2×10^5

    이미 적혀있는 키워드 N개
    쓴 글의 개수 M개

    새로운 글을 작성할 때, "최대 10개의 키워드"에 대해서 글을 작성

    1. set으로 풀이 => 시간 초과
        O(len(N) + len(10)) * M

    2. dict 풀이

"""

# 시간초과
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(" "))
#
# memo = set()
# new_post = set()
#
# for _ in range(n):
#     memo.add(input().rstrip())
#
#
# if __name__ == '__main__':
#     for _ in range(m):
#         temp_list = input().rstrip().split(',')
#         new_post.update(temp_list)
#         answer = len((memo - new_post))
#         print(answer)


# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(" "))
#
# memo = dict()
# for _ in range(n):
#     key = input().rstrip()
#     memo[key] = 1
#
# cnt = len(memo)
#
#
# if __name__ == '__main__':
#     for _ in range(m):
#         post = input().rstrip().split(',')
#         for keyword in post:
#             if keyword in memo and memo[keyword] == 1:
#               memo[keyword] = 0
#               cnt -= 1
#         print(cnt)