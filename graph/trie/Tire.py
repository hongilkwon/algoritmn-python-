"""
    Tire 구현(리트코드 208번)
"""

import sys
from collections import deque

input = sys.stdin.readline


class Node:
    def __init__(self, data=None, ending=False):
        self.data = data
        self.children = {}
        self.ending = ending


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.data = word
        node.ending = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.ending

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def autocomplete(self, word):
        ret = []
        node = self.root
        for c in word:
            if node.ending:
                ret.append(node.data)
            if c not in node.children:
                return ret
            node = node.children[c]

        q = deque()
        q.append(node)

        while q:
            node = q.popleft()
            if node.ending:
                ret.append(node.data)

            for c in node.children:
                q.append(node.children[c])

        return ret

if __name__ == '__main__':
    trie = Trie()
    trie.insert('string')
    trie.insert('str')
    trie.insert('stress')
    trie.insert('star')
    trie.insert('singer')
    trie.insert('sign')
    trie.insert('starcraft')
    trie.insert('southkorea')
    trie.insert('south korea')

    print(trie.autocomplete("st"))