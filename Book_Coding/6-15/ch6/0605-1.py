#그룹 애너그램 - 정렬하여 딕셔너리에 추가
import collections
'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
'''

def groupAnagrams (self, strs: list[str]) -> list[list[str]]:
  anagrams = collections.defaultdict(list)

  for word in strs:
    #정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)
  return list(anagrams.values())