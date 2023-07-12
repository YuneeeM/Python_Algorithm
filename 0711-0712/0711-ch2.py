import sys
sys.stdin = open("0711/input.txt", "rt")  # 파일 읽어오기

'''
K번째 수

N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하세요

입력예제
2
6253
527389
여기서 첫번째줄의 테스트 케이스가 2개임을 나타냄
2번째 줄에 6개(N)의 숫자중 2~5까지(s~e) 중 3번째(k) 은 뭐냐

'''
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" % (t+1, a[k-1]))
