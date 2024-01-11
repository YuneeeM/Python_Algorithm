import collections
#중복 문자 제거 - 스택을 이용한 문자 제거
'''
중복된 문자를 제외하고 사전식 순서로 나열하라
'''

def removeDuplicateLetters(self, s:str)-> str:
  counter, seen, stack = collections.counter(s),set(),[]

  for char in s:
    counter[char]-=1
    if char in seen:
      continue
    #뒤에 붙일 문자가 남아 있으면 스택에서 제거
    while stack and char < stack[-1] and counter[stack[-1]] > 0:
      seen.remove(stack.pop())
    stack.append(char)
    seen.add(char)
    
  return ''.join(stack)