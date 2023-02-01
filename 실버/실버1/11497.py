t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    # 가장 큰 값을 기준으로 양쪽에 점점 작게 배치를 하면 크기의 차이를 가장 많이 줄일 수 있다
    # 즉, 인덱스 값이 2씩 차이나는 값들 중 가장 큰 값이 최대 높이 차가 된다.
    for i in range(n - 2):
        res = max(res, abs(arr[i] - arr[i + 2]))
    print(res)
    
# 문제를 이해하지 못하여 풀지 못했다