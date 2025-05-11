"""
    스위치 켜고 끄기(단순 구현)

    남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.

    여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
    그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

"""

# import sys
#
# input = sys.stdin.readline
#
# switch_cnt = int(input())
#
# arr = [-1] + list(map(int, input().split(' ')))
#
# student_cnt = int(input())
#
#
# def man(n):
#     for idx in range(n, len(arr), n):
#         if arr[idx] == 0:
#             arr[idx] = 1
#         else:
#             arr[idx] = 0
#
#
# def woman(n):
#     offset = 1
#     temp = list()
#     temp.append(n)
#
#     while n - offset in range(1, switch_cnt + 1) and n + offset in range(1, switch_cnt + 1) and arr[n - offset] == arr[n + offset] :
#         temp.append(n - offset)
#         temp.append(n + offset)
#         offset += 1
#     temp.sort()
#
#     for idx in temp:
#         if arr[idx] == 0:
#             arr[idx] = 1
#         else:
#             arr[idx] = 0
#
#
# if __name__ == '__main__':
#     for _ in range(student_cnt):
#         sex, num = map(int, input().split(' '))
#         if sex == 1:
#             man(num)
#         else:
#             woman(num)
#
#     for i in range(1, switch_cnt+1):
#         print(arr[i], end=' ')
#         if i % 20 == 0:
#             print()
