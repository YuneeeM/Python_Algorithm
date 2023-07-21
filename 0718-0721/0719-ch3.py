import sys
import random as r
sys.stdin = open("0718/input3.txt", "rt")  # 파일 읽어오기

'''
뮤직비디오(결정알고리즘)☆

dvd에는 총 n개의 곡이 들어 있음,
라이브에서는 순서가 그래도 유지 -> 즉 1번 노래와 6번 노래를 같은 dvd에 녹화하기 위해 
1번과 5번 사이의 모든 노래도 같은 dvd에 녹화해야함
한노래를 쪼개서 두개의 dvd에 녹화하면 안된다.

'''


def Count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())

music = list(map(int, input().split()))
maxx = max(music)

lt = 1
rt = sum(music)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)
