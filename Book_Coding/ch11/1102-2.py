#보석과 돌 - defaultdict를 이용한 비교 생략
'''
j는 보석이며, s는 갖고 있는 돌이다, s에는 보석이 몇개나 들어 있을 까? 대소문자는 구분한다.
'''

import collections

def numJewelsInStones(self, J:str, S:str) -> int:
  freqs = collections.defaultdict(int)
  count=0

  #비교없이 돌 빈도수 계산
  for char in S:
    freqs[char] +=1

  
  #비교없이 보석 빈도수 합산
  for char in J:
    count += freqs[char]
  
  return count