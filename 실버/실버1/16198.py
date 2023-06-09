def dfs(s):
    global res
    
    if len(arr) == 2:
        res = max(res, s)
        return
    
    # 반복문을 통해 에너지 구슬을 확인
    for i in range(1, len(arr) - 1):
        # i번째 구슬을 제거했을 때 나오는 에너지
        tem = arr[i - 1] * arr[i + 1]
        
        # 백트래킹
        v = arr.pop(i) # 에너지 구슬 제거
        dfs(s + tem) # 제거된 구슬로 에너지를 재귀적으로 탐색
        arr.insert(i, v) # 제거한 에너지 구슬 추가


n = int(input())
arr = list(map(int, input().split()))
res = 0
dfs(0)
print(res)