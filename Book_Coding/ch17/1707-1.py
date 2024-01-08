# 색정렬 - 네덜란드 국기 문제를 응용한 풀이
'''
빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제저리 정렬을 수행하라
'''

from typing import List


def sortColors(self, nums: List[int]) -> None:
    red, white, blue = 0, 0, len(nums)

    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1
