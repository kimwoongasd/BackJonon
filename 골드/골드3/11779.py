import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if distance[node] < weight:
            continue
        for adj_node, adj_weight in arr[node]:
            cost = weight + adj_weight
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                prev_node[adj_node] = node
                heapq.heappush(q, (cost, adj_node))

n = int(input())
m = int(input())
arr = [[] * (n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

start, end = map(int, input().split())

distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)

dijkstra(start)
print(distance[end])

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))