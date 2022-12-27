import heapq

def dijkstra(start, end):
    tem = [2147000000] * (n + 1)
    tem[start] = 0
    hq = [(0, start)]
    while hq:
        s, node = heapq.heappop(hq)
        if s > tem[node]:
            continue
        for next_node, k in arr[node]:
            if tem[next_node] > tem[node] + k:
                tem[next_node] = tem[node] + k
                heapq.heappush(hq, (tem[next_node], next_node))

n, e = map(int, input().split())
arr = [[0]for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

v1, v2 = map(int, input().split())

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= 2147000000 and path2 >= 2147000000:
    print(-1)
else:
    print(min(path1, path2))