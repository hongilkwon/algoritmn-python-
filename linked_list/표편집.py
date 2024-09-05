"""
    표 편집

    "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
    "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
    "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    "Z" : 가장 최근에 "삭제된 행"을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

    5 ≤ n(행의 개수) ≤ 1_000_000
    0 ≤ k < n
    1 ≤ cmd의 원소 개수 ≤ 200_000

    표의 모든 행을 제거하여, 행이 하나도 남지 않는 경우는 입력으로 주어지지 않습니다.
    표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.

    사고과정.

    단순구현??
    명령어를 직접 반영하고, 단순 배열로 만들면,
    함수 때문에 insert()
    시간초과 남

    현제 포인터에서 위 아래로 이동도 쉽고, 삽입, 삭제도 쉬운
    double linked list로 구현한다.

    단순한 python class 구현을 이용할 줄 알아야 한다.

"""


# class Node:
#     def __init__(self):
#         self.removed = False
#         self.prev = None
#         self.next = None
#
#
# def solution(n, k, cmds):
#     answer = ''
#
#     arr = [Node() for _ in range(n)]
#     for i in range(1, n):
#         arr[i - 1].next = arr[i]
#         arr[i].prev = arr[i - 1]
#
#     cursor = arr[k]
#     deleted = []
#
#     for cmd in cmds:
#         if cmd[0] == 'U':
#             x = int(cmd[2:])
#             for _ in range(x):
#                 cursor = cursor.prev
#
#         if cmd[0] == 'D':
#             x = int(cmd[2:])
#             for _ in range(x):
#                 cursor = cursor.next
#
#         if cmd[0] == 'C':
#             cursor.removed = True
#             deleted.append(cursor)
#
#             up = cursor.prev
#             bottom = cursor.next
#
#             if up:
#                 up.next = bottom
#
#             if bottom:
#                 bottom.prev = up
#                 cursor = bottom
#             else:
#                 # 삭제되는 행이 마지막인 경우
#                 cursor = up
#
#         if cmd[0] == 'Z':
#             node = deleted.pop()
#             node.removed = False
#
#             up = node.prev
#             bottom = node.next
#
#             if up:
#                 up.next = node
#
#             if bottom:
#                 bottom.prev = node
#
#     for i in range(n):
#         if arr[i].removed:
#             answer += 'X'
#         else:
#             answer += 'O'
#     print(answer)
#     return answer


# # 시간초과
# from collections import deque
#
#
# def solution(n, k, cmds):
#     answer = ''
#
#     arr = [i for i in range(n)]
#
#     cursor = k
#     deleted = deque()
#
#     for cmd in cmds:
#         temp = cmd.split(' ')
#         operator = temp[0]
#
#         if operator == 'U':
#             x = int(temp[1])
#             cursor -= x
#
#         if operator == 'D':
#             x = int(temp[1])
#             cursor += x
#
#         if operator == 'C':
#             idx = cursor
#             name = arr[idx]
#             deleted.append((idx, name))
#
#             if cursor == len(arr) - 1:
#                 cursor -= 1
#             arr.pop(idx)
#
#         if operator == 'Z':
#             idx, name = deleted.pop()
#             if cursor >= idx:
#                 cursor += 1
#             arr.insert(idx, name)
#
#     temp = ['X' for i in range(n)]
#     for e in arr:
#         temp[e] = "O"
#     answer = ''.join(temp)
#     # print(answer)
#     return answer


# if __name__ == '__main__':
#     solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
