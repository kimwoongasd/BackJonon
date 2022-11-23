n = int(input())
arr = [0] * (n + 5)
for i in range(n):
    a = int(input())
    arr[i] = a

ch = [0] * (n + 5)
ch[0] = arr[0]
ch[1] = arr[0] + arr[1]
ch[2] = max(arr[1] + arr[2], arr[0] + arr[1], arr[0] + arr[2])


for i in range(3, n + 1):
    ch[i] = max(ch[i - 1], ch[i - 2] + arr[i], ch[i - 3] + arr[i - 1] + arr[i])
print(ch[n])