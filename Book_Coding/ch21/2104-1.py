# 테스크 스케줄러 - 우선순위 큐 이용
'''
A에서 Z로 표현된 테스트가 있다. 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고,
n번의 간격 내에는 동일한 태스크를 실행할 수 없다. 더 이상 태스크를 실행할 수 없는 경우 아이들 상태가 된다.
모든 태스크를 실행하기 위한 최소 간격을 출력하라.
'''

from typing import List
import collections


def leastInterval(self, tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        # 개수 순 호출
        for task, _ in counter.most_common(n+1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하인 아이템을 목록에서 완전히 제거
            counter += collections.Counter()

        if not counter:
            break

        result += n - sub_count + 1

        return result
