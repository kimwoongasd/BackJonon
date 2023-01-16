import heapq, sys
input = sys.stdin.readline
inf = 2147000000

def dijkstra(start, end):
    tem = [inf] * n
    tem[start] = 0
    hp = [(0, start)]
    while hp:
        s, node = heapq.heappop(hp)
        if s > tem[node]:
            continue
        for next_node, k in arr[node]:
            if tem[next_node] > tem[node] + k:
                tem[next_node] = tem[node] + k
                heapq.heappush(hp, (tem[next_node], next_node))
    return tem[end]

n, m, x = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a - 1].append((b - 1, t))

res = [0] * n
for i in range(n):
    res[i] = dijkstra(i, x - 1)
for i in range(n - 1, -1, -1):
    res[i] += dijkstra(x - 1, i)
print(max(res))