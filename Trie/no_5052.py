"""
    전화번호 목록

    일관성이 있는지 없는지를 구하는 프로그램을 작성

    한 번호가 다른 번호의 "접두어"인 경우가 없어야 한다
"""


# Trie를 이용한 풀이.
# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# class Node:
#     def __init__(self, ending= False):
#         self.children = {}
#         self.ending = ending
#         self.data = ''
#
#
# class Trie:
#     def __init__(self):
#         self.root = Node()
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = Node()
#             node = node.children[c]
#         node.data = word
#         node.ending = True
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return node.ending
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for c in prefix:
#             if c not in node.children:
#                 return False
#             node = node.children[c]
#         return True
#
#     def is_contains(self, word):
#         node = self.root
#         for c in word:
#             if node.ending:
#                 return True
#             node = node.children[c]
#         return False
#
#
# if __name__ == '__main__':
#
#     for _ in range(tc):
#         n = int(input())
#         phone_nums = []
#         trie = Trie()
#
#         for _ in range(n):
#             number = input().rstrip()
#             trie.insert(number)
#             phone_nums.append(number)
#
#         flag = True
#         for num in phone_nums:
#             if trie.is_contains(num):
#                 flag = False
#                 break
#
#         if flag:
#             print("YES")
#         else:
#             print("NO")


# import sys
#
# input = sys.stdin.readline
#
# tc = int(input())
#
# if __name__ == '__main__':
#     for _ in range(tc):
#         n = int(input())
#
#         phone_nums = []
#         for _ in range(n):
#             phone_nums.append(input().rstrip())
#         phone_nums.sort()
#         # print(phone_nums)
#
#         flag = True
#         for i in range(n-1):
#             l = len(phone_nums[i])
#             if phone_nums[i] == phone_nums[i+1][:l]:
#                 flag = False
#                 break
#
#         if flag:
#             print("YES")
#         else:
#             print("NO")
