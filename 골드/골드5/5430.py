import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    arr = input().rstrip()[1:-1].split(',')
    dq = deque(arr)
    # 거꾸로 뒤집은 횟수
    r = 0
    # 에러가 발생하면 1 아니면 0
    f = 0
    if n == 0:
        dq = []

    for x in p:
        if x == "R":
            r += 1
        else:
            if len(dq) < 1:
                print("error")
                f = 1
                break
            else:
                if r % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    if f == 0:
        if r % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")