# 팰린드롬 페어 - 트라이 구현
'''
단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합 (i,j)를 구하라
'''
from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-1]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    # 단어 존재 여부 판별
    def search(self, index, word) -> bool:
        result = []
        node = self.root
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def PalindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results
