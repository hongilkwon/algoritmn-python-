"""
    Tire 구현(리트코드 208번)
"""

# import sys
#
# input = sys.stdin.readline
#
#
# class Node:
#     def __init__(self, ending= False):
#         self.children = { }
#         self.ending = ending
#
#
# class Trie:
#     def __init__(self):
#         self.root = Node(ending=True)
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = Node()
#             node = node.children[c]
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
