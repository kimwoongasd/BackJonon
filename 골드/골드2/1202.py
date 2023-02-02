import heapq, sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(arr, [m, v])
bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()

res = 0
tem = []
for bags in bag:
    while arr and arr[0][0] <= bags:
        heapq.heappush(tem, -heapq.heappop(arr)[1])
    
    if tem:
        res -= heapq.heappop(tem)
print(res)

'''
풀이
먼저 보석 리스트와 가방 리스트를 오름차순으로 정렬하고
각 가방을 기준으로 보석이 가방에 넣을 수 있는지 확인한다.
가방에 넣을 수 있는 보석 중 가치가 가장 큰 걸 넣어주면 된다.

가장 가치가 큰 것만 뽑아주면 되니까 최대 힙을 사용하여 시간 단축
'''