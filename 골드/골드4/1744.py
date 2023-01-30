n = int(input())
# 양수 저장 리스트
pn = []
# 음수 저장 리스트
nn = []
s = 0

# 규칙
# 0, 양수 = 덧셈 0, 음수 = 곱셈
# 1, 양수 = 덧셈 1, 음수 = 덧셈 즉, 1 = 덧셈
# 양수, 양수 = 곱셈 음수, 음수 = 곱셈 양수, 음수 = 덧셈

for _ in range(n):
    a = int(input())
    if a > 1:
        pn.append(a)
    elif a == 1:
        s += 1
    else:
        nn.append(a)
# 양수 내림차순
pn.sort(reverse=True)
# 음수 오름차순
nn.sort()

# 리스트의 숫자가 2개로 나누어 떨어진다면 2개씩 곱
# 이니라면 마지막 숫자를 제외하고 곱

if len(pn) % 2 == 0:
    for i in range(0, len(pn), 2):
        s += (pn[i] * pn[i + 1])
else:
    for i in range(0, len(pn) - 1, 2):
        s += (pn[i] * pn[i + 1])
    s += pn[-1]
    
if len(nn) % 2 == 0:
    for i in range(0, len(nn), 2):
        s += (nn[i] * nn[i + 1])
else:
    for i in range(0, len(nn) - 1, 2):
        s += (nn[i] * nn[i + 1])
    s += nn[-1]
print(s)

# 규칙을 찾지 못하여 못풀었다