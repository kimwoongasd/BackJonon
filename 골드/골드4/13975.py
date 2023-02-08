import heapq
t = int(input())
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    while len(arr) > 1:
        a, b = heapq.heappop(arr),  heapq.heappop(arr)
        res += a + b
        heapq.heappush(arr, a + b)
        
    print(res)