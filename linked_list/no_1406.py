"""
    에디터(LinkedList)

    사고과정.

    명령어가 주어지고 앞뒤로 이동하면서, 짧은 시간내에 많은 삽입 삭제를 한다?
    => 더블 링크드 리스트
"""


# import sys
#
# input = sys.stdin.readline
#
#
# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#
#
# head = Node('head')
# cursor = head
#
# s = input().rstrip()
#
# for c in s:
#     new_node = Node(c)
#     cursor.next = new_node
#     new_node.prev = cursor
#     cursor = new_node
#
# m = int(input())
#
# if __name__ == '__main__':
#     for _ in range(m):
#         operator = input().rstrip()
#
#         if operator[0] == 'L':
#             if cursor.prev:
#                 cursor = cursor.prev
#
#         if operator[0] == 'D':
#             if cursor.next:
#                 cursor = cursor.next
#
#         if operator[0] == 'B':
#             if cursor.prev:
#                 prev = cursor.prev
#                 next = cursor.next
#
#                 if next:
#                     prev.next = next
#                     next.prev = prev
#                 else:
#                     prev.next = None
#
#                 cursor = prev
#
#         if operator[0] == 'P':
#             new_node = Node(operator[-1])
#             next = cursor.next
#
#             if next:
#                 new_node.next = next
#                 next.prev = new_node
#
#             cursor.next = new_node
#             new_node.prev = cursor
#             cursor = new_node
#
#     # 출력
#     print_node = head.next
#     while print_node:
#         print(print_node.data, end='')
#         print_node = print_node.next
