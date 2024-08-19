"""
    순위검색

    * [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

    1 <= info 배열의 크기 <= 50_000
    1 <= query 배열의 크기 <= 100_000

    사고과정

    단순히 조건이 하나도 없다고 가정해보면,
    query가 10만 * info 5만개 ->  5_000_000_000(50억)

    1. 점수를 미리 정렬 O(NlogN), 쿼리 이분탐색O(logN)으로 한다

    2. 점수의 등장 횟수 counting O(N) -->  점수의 등장 횟수 prefix Sum O(N) --> 쿼리 O(1)

    * 모든 조건을 고려했을 경우 가능한 쿼리의 갯수는
     4('-', 'cpp', 'java', 'python')
     *3('-', 'backend', 'frontend')
     *3('-', 'junior', 'senior')
     *3('-', 'chicken', 'pizza')
     => 108개


"""

# import sys
#
# input = sys.stdin.readline
#
# import bisect
#
# c_dict = {
#     '-': 0,
#     'cpp': 1, 'java': 2, 'python': 3,
#     'backend': 1, 'frontend': 2,
#     'junior': 1, 'senior': 2,
#     'chicken': 1, 'pizza': 2,
# }
#
#
# def solution(info, query):
#     answer = []
#
#     # 108개의 쿼리의 형태마다 점수를 담을 리스트
#     q_arr = [[] for i in range(108)]
#
#     for s in info:
#         c_names = s.split(' ')
#         c1, c2, c3, c4, point = c_dict[c_names[0]], c_dict[c_names[1]], c_dict[c_names[2]], c_dict[c_names[3]], int(
#             c_names[4])
#         # print(c1, c2, c3, c4,)
#
#         # 1가지의 info가 저장되어야 하는 2^4 가지 쿼리타입에 포인트를 저장해야된다.
#         for i in range(1 << 4):
#             idx = 0
#             for j in range(4):
#                 if i & (1 << j):
#                     if j == 3:
#                         idx += c1 * 27
#                     if j == 2:
#                         idx += c2 * 9
#                     if j == 1:
#                         idx += c3 * 3
#                     if j == 0:
#                         idx += c4
#             q_arr[idx].append(point)
#
#     for i in range(108):
#         q_arr[i].sort()
#
#     for q in query:
#         q_names = q.split(' ')
#         q1, q2, q3, q4 = c_dict[q_names[0]], c_dict[q_names[2]], c_dict[q_names[4]], c_dict[q_names[6]]
#         target = int(q_names[7])
#
#         idx = q1 * 27 + q2 * 9 + q3 * 3 + q4
#         answer.append(len(q_arr[idx]) - bisect.bisect_left(q_arr[idx], target))
#     # print(answer)
#     return answer
#
#
# if __name__ == '__main__':
#     solution(
#         ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
#          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
#
#         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
#          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
#          "- and - and - and - 150"])
