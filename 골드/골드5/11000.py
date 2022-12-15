import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append([s, t])

arr.sort()
room = []
heapq.heappush(room, arr[0][1])

for i in range(1, n):
    # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
    if room[0] > arr[i][0]:
        # 새로운 회의실 개설
        heapq.heappush(room, arr[i][1])
        
    # 현재 회의실에 이어서 회의 개최 가능
    else:
        # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))

# 틀림
# from collections import deque
# n = int(input())
# arr = []
# for _ in range(n):
#     s, t = map(int, input().split())
#     arr.append([s, t])

# arr.sort(key=lambda x: (x[0], x[1]))

# dq = deque(arr)
# count = 1
# p_s, p_t = dq.popleft()
# 첫 번째 수업을 기준으로 한 강의실에 최대로 수업 할 경우의 수
# 그 외는 강의실 수를 늘려 준다.
# while dq:
#     x, y = dq.popleft()
#     if x >= p_t:
#         p_s = x
#         p_t = y
#     else:
#         count += 1
# print(count)