# 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    ch[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])
    
    while pq:
        w, tem = heapq.heappop(pq)
        # 현재 도시까지 가는데 드는 비용이 더 적으면 넘어간다.
        if ch[tem] < w:
            continue
        
        # 도시와 연결되어 있는 도시들을 확인
        for a, b in arr[tem]:
            # 다음 도시까지 가는데 드는 비용을 확인
            total = w + b
            # 다음 도시까지 가는데 드는 비용과 이전에 그 도시까지 걸린 비용을 비교
            if total < ch[a]:
                # 다음 도시까지 가는데 드는 비용을 초기화
                ch[a] = total
                heapq.heappush(pq, [total, a])

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
ch = [int(1e9)] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    arr[x].append([y, z])
    
p_x, p_y = map(int, input().split())

dijkstra(p_x)
print(ch[p_y])
 
 
# 폴로이드 워샬 - 시간초과
# n = int(input())
# m = int(input())
# arr = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     arr[i][i] = 0

# for i in range(m):
#     x, y, z = map(int, input().split())
#     arr[x][y] = z

# p_x, p_y = map(int, input().split())

# for i in range(1, n + 1):
#     for j in  range(1, n + 1):
#         for k in range(1, n + 1):
#             arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

# print(arr[p_x][p_y])