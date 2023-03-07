import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))
    
s = 0
e = k
cnt = 0

while s < n:
    # 중복 제거
    tem = set()
    for i in range(s, e):
        # i가 n을 넘어가도 첫번째 부터 순서가 오도록 설정
        tem.add(arr[i % n])
    
    tem.add(c)
    cnt = max(cnt, len(tem))
    s += 1
    e += 1
    
print(cnt)        