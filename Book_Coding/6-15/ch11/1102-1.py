#보석과 돌 - 해시 테이블을 이용한 풀이
'''
j는 보석이며, s는 갖고 있는 돌이다, s에는 보석이 몇개나 들어 있을 까? 대소문자는 구분한다.
'''

def numJewelsInStones(self, J:str, S:str) -> int:
  freqs={}
  count=0

  #돌에 있는 빈도수 계산
  for char in S:
    if char not in freqs:
      freqs[char] = 1
    else:
      freqs[char]+=1

  #보석에 있는 빈도수 계산
  for char in J:
    if char in freqs:
      count+=freqs[char]
  
  return count
  
  