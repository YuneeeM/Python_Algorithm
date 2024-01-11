#보석과 돌 - counter로 계산 생략
'''
j는 보석이며, s는 갖고 있는 돌이다, s에는 보석이 몇개나 들어 있을 까? 대소문자는 구분한다.
'''

import collections

def numJewelsInStones(self, J:str, S:str) -> int:
  freqs = collections.Counter(S) #돌의 빈도수 계산
  count = 0

  #비교없이 보석 빈도 수 합산
  for char in J:
    count += freqs[char]

  return count
