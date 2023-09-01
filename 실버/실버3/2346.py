import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split()))) #1
res = []

while q:
    idx, num = q.popleft() #2
    res.append(idx+1) #3
    if num > 0: #4
        q.rotate(-1*(num-1))
    elif num < 0: #5
        q.rotate(abs(num))
print(*res)

#1 : enumerate도 튜플로 만들어 주는 연속적인 객체이니까 deque()안에 삽입 가능

#2 : 원하는 값을 항상 인덱스 0번에서 빼는것으로 구현하므로 인덱스와 값을 popleft()

#3 : 각 인덱스를 문제에 맞게 삽입

#4 : num이 양수일때 popleft에 의해 재정렬된 리스트를 rotate를 이용해 왼쪽 원소를 오른쪽으로 삽입 횟수는 양수일때는 num-1번만큼 반복

#5 : num이 음수일때는 popleft에 의해 재정렬된 리스트를 rotate를 이용해 오른쪽 원소를 왼쪽으로 삽입 음수일때는 num번만큼 반복