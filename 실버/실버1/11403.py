# 플로이드-워셜 알고리즘
# 점 i에서 점 k로의 경로가 있고, 점 k에서 점 j로의 경로가 있다면
# 점 i에서 점 j로의 경로가 존재한다.
n = int(input())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for k in range(n): # 경유지 노드
    for i in range(n): # 출발 노드
        for j in range(n): # 도착 노드
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

for x in arr:
    print(*x)