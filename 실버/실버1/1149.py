n = int(input())
rgb = []

ch = [[0] * 3 for _ in range(n)]

for _ in range(n):
    a, b, c = map(int, input().split())
    rgb.append([a, b, c])
ch[0] = rgb[0]  
for i in range(1, n):
    ch[i][0] = rgb[i][0] + min(ch[i - 1][1], ch[i - 1][2])
    ch[i][1] = rgb[i][1] + min(ch[i - 1][0], ch[i -1][2])
    ch[i][2] = rgb[i][2] + min(ch[i - 1][0], ch[i -1][1])

print(min(ch[n - 1]))