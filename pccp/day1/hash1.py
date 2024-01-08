# hash [key-value]
'''
특징
- 순서를 보장하지 않음
- 데이터 중복을 허용하지 않음
- 데이터 조회가 선형 데이터보다 빠름
- python에서 set과 dictionary는 hashtable
'''
# set의 집합연산
s1 = {1, 2, 'a', 'b'}
s2 = {2, 3, 'b', 'c'}
print(s1)
print(s2)
print(s1 | s2)  # 합칩합 or
print(s1 & s2)  # 교집합 and
print(s1 - s2)  # 차집합 -
