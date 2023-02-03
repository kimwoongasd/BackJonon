import sys 
input=sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

# 박스 무게가 크레인이 들수있는 무게보다 크다면
if crane[0] < box[0]:
    print(-1)
    sys.exit(0)

time = 0
while len(box):
    for x in crane:
        for y in box:
            # 크레인이 박스를 들 수 있다면 1개 제거하고 break
            if x >= y:
                box.remove(y)
                break
    time += 1
print(time)