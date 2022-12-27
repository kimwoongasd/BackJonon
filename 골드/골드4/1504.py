# 다익스트라 알고리즘
import heapq, sys
input = sys.stdin.readline
inf = 2147000000

# start와 end 두 인자를 받아와 dist[end]를 return하는 함수
# start -> end로 가는 최소값이 중요
def dijkstra(start, end):
    tem = [inf] * (n + 1)
    tem[start] = 0
    hq = [(0, start)]
    while hq:
        # len이 dist[node]보다 크다면 => 지금까지 온 거리가 dist[node]보다 크다면?
        # => 최소값을 구하는 것이므로 볼 필요가 없으니 continue
        s, node = heapq.heappop(hq)
        if s > tem[node]:
            continue
        for next_node, k in arr[node]:
            # 다음에 갈 노드의 현재까지 최소 거리 값이 현재 노드까지 온 거리 + 다음 노드까지 갈 거리보다 크다면
            if tem[next_node] > tem[node] + k:
                tem[next_node] = tem[node] + k
                heapq.heappush(hq, (tem[next_node], next_node))
    return tem[end]
    
n, e = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

v1, v2 = map(int, input().split())

# 1부터 v1까지, v1에서 v2를 거쳐 end(N)까지 가는 경로
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
# 부터 v2까지, v2에서 v1을 거쳐 end(N)까지 가는 경로
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= inf and path2 >= inf:
    print(-1)
else:
    print(min(path1, path2))