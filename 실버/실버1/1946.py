import sys
input = sys.stdin.readline
t = int(input()) # 테스트 횟수

for _ in range(t):
    n = int(input()) # 지원자 수
    arr = [] # 지원자 순위를 담을 리스트
    for _ in range(n):
        a, b = map(int, input().split()) # 서류, 면접 성적 순위
        arr.append((a, b))
        
    arr.sort(key=lambda x: x[0]) # 서류 순위 순으로 정력

    prv = arr[0][1] # 비교 기준이 되는 순위
    count = 1
    for i in range(1, n):
        if arr[i][1] < prv:
            count += 1
            prv = arr[i][1]
    print(count)