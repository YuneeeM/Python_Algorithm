# 지붕잃고 외양간 고치기

answer = 0
so = []
m, s, c = map(int, input().split())

# 외양간에 살고 있는 소들의 위치
for i in range(c):
    so.append(int(input()))

# 소 정렬
so.sort()

# 소들간의 거리
di = []

# 소들간의 거리 구해서 추가
for i in range(1, len(so)):
    # 뒤에 소와 앞의 소의 차이
    temp = so[i] - so[i-1]
    di.append(temp)

# 소들간의 거리 정렬(큰 값이 앞에 오게)
di.sort(reverse=True)

# 판자의 기본 길이(실제 살고 있는 소들의 지붕)
answer = so[-1] - so[0] + 1

# 판자 개수-1 만큼 필요없는 지붕 차감
for i in range(m-1):
    answer -= di[i]-1


print(answer)
