# 회의실 배정 - 그리디
n = int(input())

meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

et = 0  # 회의 끝나는 시간
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
