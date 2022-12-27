import heapq

n = int(input())
card = []
for _ in range(n):
    a = int(input())
    heapq.heappush(card, a)
    
if len(card) == 1:
    print(0)
else:
    res = 0
    while len(card) > 1:
        x = heapq.heappop(card)
        y = heapq.heappop(card)
        res += x + y
        heapq.heappush(card, x + y)
    print(res)