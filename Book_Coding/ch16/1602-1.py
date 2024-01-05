# 팰린드롬 페어 - 팰린드롬을 브루트 포스로 계산
'''
단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합 (i,j)를 구하라
'''
from typing import List


def PalindromePairs(self, words: List[str]) -> List[List[int]]:
    def is_palindrome(word):
        return word == word[::-1]

    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1+word2):
                output.append([i, j])
    return output
