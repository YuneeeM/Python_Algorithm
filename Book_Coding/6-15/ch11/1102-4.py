#보석과 돌 - 파이썬 다운 방식
'''
j는 보석이며, s는 갖고 있는 돌이다, s에는 보석이 몇개나 들어 있을 까? 대소문자는 구분한다.
'''

def numJewelsInStones(self, J:str, S:str) -> int:
  return sum(s in J for s in S)