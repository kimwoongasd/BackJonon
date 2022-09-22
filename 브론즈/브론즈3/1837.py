n, m = map(int, input().split())

tem = True
for i in range(2, m):
    if n % i == 0:
        print(f"BAD {i}")
        tem = False
        break

if tem:
    print("GOOD")