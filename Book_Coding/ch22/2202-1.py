#괄호를 삽입하는 여러가지 방법 - 분할 정복을 이용한 다양한 조합
'''
숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라
'''
from typing import List


def difWaysToCompute(self, input:str) -> List[int]:
    def compute(left,right,op):
        results=[]
        for l in left:
            for r in right:
                results.append(eval(str(l)+op+str(r)))
            return results
    if input.isdigit():
        return [int(input)]
    
    results=[]
    for index, value in enumerate(input):
        if value in "-+":
            left=self.difWaysToCompute(input[:index])
            right=self.difWaysToCompute(input[index+1:])

            results.extend(compute(left,right,value))
    return results
