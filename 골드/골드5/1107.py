n = int(input())
m = int(input())
if m != 0 :
    arr = list(map(int, input().split()))
else:
    arr = []

# 지금 채널 100이니까 100을 뺴주고 시작
res = abs(n - 100)

for i in range(1000001):
    for j in str(i):
        if int(j) in arr:
            break
    
    else:
        # 123을 눌렀다면 버튼 3개를 눌렀으니 더 해준다
        res = min(res, abs(n - i) + len(str(i)))
print(res)