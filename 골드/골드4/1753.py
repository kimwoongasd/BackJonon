import heapq, sys
input = sys.stdin.readline
inf = 2147000000

def dijkstra(start):
    global tem
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    tem[start] = 0
    hq = [(0, start)]
    while hq:
        s, node = heapq.heappop(hq)
        if s > tem[node]:
            continue
        for next_node, k in arr[node]:
            #현재 정점 까지의 가중치 tem[node] + 현재 정점에서 다음 정점(next_node)까지의 가중치 k
            if tem[next_node] > tem[node] + k:
                #다음 노드까지의 가중치가 현재 기록된 값 보다 작으면 조건 성립
                tem[next_node] = tem[node] + k
                heapq.heappush(hq, (tem[next_node], next_node))
    

v, e = map(int, input().split())
arr = [[] for _ in range(v + 1)]
k = int(input())
for _ in range(e):
    x, y, w = map(int, input().split())
    arr[x].append([y, w])
    
tem = [inf] * (v + 1)
dijkstra(k)
for i in range(1, v + 1):
    if tem[i] == inf:
        print("INF")
    else:
        print(tem[i])