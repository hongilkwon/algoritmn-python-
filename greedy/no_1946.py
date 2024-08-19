"""
    신입사원(그리디)

"""

# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# if __name__ == '__main__':
#     for _ in range(tc):
#         n = int(input())
#         arr = list()
#         for i in range(n):
#             temp = tuple(map(int, input().split()))
#             arr.append(temp)
#
#         arr.sort(key=lambda x: x[0])
#         # print(arr)
#
#         current = arr[0]
#         cnt = 1
#         for i in range(1, n):
#             if current[1] > arr[i][1]:
#                 cnt += 1
#                 current = arr[i]
#         print(cnt)