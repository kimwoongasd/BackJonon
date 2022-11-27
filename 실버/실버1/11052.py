n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
card = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1):
        card[j] = max(card[j], card[j - i] + arr[i])
print(card[n])
print(card)