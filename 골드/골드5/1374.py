import heapq, sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    num, start, end = map(int, input().split())
    arr.append([num, start, end])
    
arr.sort(key=lambda x : x[1])
for x in arr:
    print(x)
hq = []
res = 0
# 강의 시작 시간을 기준으로 오름차순 정렬한 뒤, 이를 하나씩 탐색한다.
# 강의 끝나는 시간을 기준으로 최소힙을 구성해 시작 시간보다 일찍 끝나는 강의는 모두 뺀다.
# 매번 강의를 탐색할 때마다 최소힙의 개수를 구해 이의 최대값을 구한 뒤, 이를 출력한다.
for x in arr:
    s, e = x[1], x[2]
    while hq and s >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, e)
    res = max(res, len(hq))
    
print(res)


'''
lambda를 통한 정렬과 heapq push의 리스트 순서가 다르다
정렬에 따라 값이 달라진다.
'''
# n = int(sys.stdin.readline())

# heap = []
# q = []
# for _ in range(n):
#     num, start, end = map(int,sys.stdin.readline().split())
#     heapq.heappush(heap, [start,end,num])
# for x in heap:
#     print(x)
# start, end, num = heapq.heappop(heap)
# heapq.heappush(q, end)
# while heap:
#     start, end, num = heapq.heappop(heap)
#     if q[0] <= start:
#         heapq.heappop(q)
#     heapq.heappush(q, end)

# print(len(q))