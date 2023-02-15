arr = [0] * 4000001
num = []
for i in range(2, 4000001):
    if arr[i] == 0:
        num.append(i)
        for j in range(i * 2, 4000001, i):
            arr[j] = 1

n = int(input())

cnt = 0
s = 0
e = 0

while e <= len(num):
    total = sum(num[s:e])
    
    if total == n:
        cnt += 1
        e += 1
    elif total < n:
        e += 1
    else:
        s += 1

print(cnt)

'''
풀이
에라토스테네스의 체 : 주어진 n까지의 소수를 미리 구한다
투포인터 : start, end 두 개의 포인터를 이용해서 원하는
값보다 작은 경우 end += 1을 큰 경우에는 start += 1을 적용해서 end가 N이 될때까지 수행합니다.

end 값을 끝애서 부터 실행하는 방법을 사용하였는데 오답이였다
'''