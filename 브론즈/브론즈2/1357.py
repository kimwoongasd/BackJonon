a, b = map(str, input().split())

def rev(x):
    tem = ""
    for y in str(x):
        tem = y + tem
    return int(tem)

print(rev(rev(a) + rev(b)))