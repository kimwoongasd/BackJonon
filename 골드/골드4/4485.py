import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra():
    dp[0][0] = 0
    heapq.heappush(hp, (arr[0][0], 0, 0))
    
    while hp:
        cost, x, y = heapq.heappop(hp)
        
        if x == n - 1 and y == n - 1:
            break
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                new_cost = cost + arr[xx][yy]
                if new_cost < dp[xx][yy]:
                    dp[xx][yy] = new_cost
                    heapq.heappush(hp, (new_cost, xx, yy))

count = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    dp = [[INF] * n for _ in range(n)]
    hp = []
    dijkstra()
    print(f"Problem {count}: {dp[n - 1][n - 1]}")
    count += 1