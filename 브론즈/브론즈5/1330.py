a, b = map(int, input().split())

res = ""

if a > b:
    res = ">"
elif a < b:
    res = "<"
else:
    res = "=="

print(res)