#상위 k빈도 요소 - 파이썬다운 방식
'''
상위 k번 이상 등장하는 요소를 추출하라
'''
import collections

def topKFrequent(self, nums, k):
  return list(zip(*collections.Counter(nums).most_common(k)))[0]