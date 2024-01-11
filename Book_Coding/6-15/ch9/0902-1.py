#중복 문자 제거 - 재귀를 이용한 분리
'''
중복된 문자를 제외하고 사전식 순서로 나열하라
'''

def removeDuplicateLetters(self, s:str) -> str:
  #집합으로 정렬
  for char in sorted(set(s)):
    suffix = s[s.index(char):]
    #전체 집합과 접미사 집합이 일치할 때 분리 진행
    if set(s) == set(suffix):
      return char + self.removeDuplicateLetters(suffix.replace(char,''))
  return 's'