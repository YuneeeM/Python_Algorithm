# 요세푸스 순열
from collections import deque
N, K = map(int, input().split())

# 사람 번호
q = [i for i in range(1, N+1)]
# 제거된 사람 출력
ans = []
# 순번
idx = 0

while q:
    # 현위치 포함하여 K번 가야 하기 때문에 -1
    for i in range(K-1):
        if len(q) != 0:
            q.append(q.pop(0))
    if len(q) != 0:
        ans.append(q.pop(0))

print(' '.join(map(str, ans)))

# -----------------------------------------------------------------------------------------

# 리스트의 pop(0) == .popleft() 동일 명령어

N, K = map(int, input().split())

# 사람 번호
q = [i for i in range(1, N+1)]  # [1 2 3 4 5]
q = deque(q)  # deque적용 된 것만 popleft()를 사용 가능하기 때문에 적용

# 제거된 사람 출력
ans = []
# 순번
idx = 0

while q:
    # 현위치 포함하여 K번 가야 하기 때문에 -1
    for i in range(K-1):
        q.append(q.popleft())
    print(q.popleft(), end=' ')
