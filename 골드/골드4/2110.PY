# 문제를 잘 이해하지 못하여 못 풀었다....
n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
    
arr.sort()

# 최소와 최대 거리(가장 큰 값 - 가장 작은 값)
s = 1
e = arr[-1] - arr[0]

res = 0

# 이분법
while s <= e:
    mid = (s + e) // 2
    # 초기 위치는 고정
    old = arr[0]
    # 공유기 수
    count = 1
    
    for i in range(1, n):
        if arr[i] >= old + mid:
            count += 1
            old = arr[i]
    
    # count가 c와 같을 때 최대값을 구해야하므로 s를 올려준다
    if count >= c:
        s = mid + 1
        res = mid
    else:
        e = mid - 1
print(res)

# 풀이
# 집을 정렬해서 최소 거리와 최대 거리를 계산하고 이들의 중간값을 계산
# 중간값을 기준으로 집의 개수를 셌을 때 C보다 크다면, 최소값을 중간값 + 1로 갱신하고,
# 중간값을 기준으로 집의 개수를 셌을 때 C보다 작다면, 최댓값을 중간값 - 1로 갱신한다.
# 이걸 계속 반복하는 데, 최솟값과 최댓값이 같아질 때까지 반복한다.