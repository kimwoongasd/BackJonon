x, y = map(int, input().split())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
day = y - 1

for i in range(1, x):
    if i in a:
        day += 31
    elif i in b:
        day += 30
    else:
        day += 28

d = day % 7
print(c[d])
