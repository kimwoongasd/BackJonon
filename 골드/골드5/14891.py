from collections import deque
# 재귀를 이용하여 왼쪽 오른쪽을 확인
def rotate_right(x, d):
    # 더이상 조사가 불가능한 경우
    if x > 4 or arr[x - 1][2] == arr[x][6]:
        return

    # 오른쪽 확인
    if arr[x - 1][2] != arr[x][6]:
        # 인접한 톱니바퀴가 회전 가능한지 확인
        rotate_right(x + 1, -d)
        # 회전
        arr[x].rotate(d)


def rotate_left(x, d):
    # 더이상 조사가 불가능한 경우
    if x < 1 or arr[x][2] == arr[x + 1][6]:
        return

    if arr[x][2] != arr[x + 1][6]:
        rotate_left(x - 1, -d)
        arr[x].rotate(d)
        
arr = []
arr.append([0])
for _ in range(4):
    a = deque(list(map(int, input())))
    arr.append(a)
    
for _ in range(int(input())):
    x, d = map(int, input().split())

    # 기준 톱니바퀴의 왼쪽 오른쪽 회전가능한지 확인하고 회전
    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    arr[x].rotate(d)

ans = 0
for i in range(4):
    ans += arr[i + 1][0] * (2 ** i)

print(ans)

# 틀림
# arr = []
# for _ in range(4):
#     a = deque(list(map(int, input())))
#     arr.append(a)

# n = int(input())
# for _ in range(n):
#     x, y = map(int, input().split())
    
#     if y == 1:
#         tem = -y
#         arr[x - 1].appendleft(arr[x - 1].pop())
#         for i in range(x, 4):
#             if tem == 1 and arr[i - 1][2] != arr[i][6]:
#                 arr[i].appendleft(arr[i].pop())
#                 tem = -tem
#             elif tem == -1 and arr[i - 1][2] != arr[i][6]:
#                 arr[i].append(arr[i].popleft())
#                 tem = -tem
#         if 0 < x - 1 < 3:
#             for j in range(x - 1, -1, -1):
#                 if tem == 1 and arr[j][2] != arr[j + 1][6]:
#                     arr[j].appendleft(arr[j].pop())
#                     tem = -tem
#                 elif tem == -1 and arr[j][2] != arr[j + 1][6]:
#                     arr[j].append(arr[j].popleft())
#                     tem = -tem
#     else:
#         tem = -y
#         arr[x - 1].append(arr[x - 1].popleft())
#         for i in range(x, 4):
#             if tem == 1 and arr[i - 1][2] != arr[i][6]:
#                 arr[i].appendleft(arr[i].pop())
#                 tem = -tem
#             elif tem == -1 and arr[i - 1][2] != arr[i][6]:
#                 arr[i].append(arr[i].popleft())
#                 tem = -tem
#         if 0 < x - 1 < 3:
#             for j in range(x - 1, -1, -1):
#                 if tem == 1 and arr[j][2] != arr[j + 1][6]:
#                     arr[j].appendleft(arr[j].pop())
#                     tem = 1
#                 elif tem == -1 and arr[j][2] != arr[j + 1][6]:
                    
#                     arr[j].append(arr[j].popleft())
#                     tem = -tem
#     # for i in range(4):
#     #     print(arr[i])
# res = 0
# for i in range(4):
#     if arr[i][0] == 1:
#         if i == 0:
#             res += 1
#         elif i == 1:
#             res += 2
#         elif i == 2:
#             res += 4
#         else:
#             res += 8
#     # print(arr[i][0])

# print(res)