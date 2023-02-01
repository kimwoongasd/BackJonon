n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    target += x
print(target)
'''
풀이
저울추의 무게를 비교하기 위해 오름차순으로 정렬한다.

저울추의 무게와 비교할 변수를 만들어 양의 정수의 최솟값인 1로 초기화시킨다.

변수는 반복문을 통해 저울추의 무게를 더해준다.

변수와 저울추의 무게를 비교하고 저울추의 무게가 더 크다면 변수의 값은 저울추로 만들 수 없는 양의 정수의 최솟값이 된다. 
'''