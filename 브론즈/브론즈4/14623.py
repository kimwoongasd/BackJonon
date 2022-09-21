a = input()
b = input()

def binary(x):
    num = 0
    for i in x:
        if int(i) == 1:
            num = (num * 2) + 1
        else:
            num *=2

    return num

def b_to_number(x):
    res = ""
    
    tem = x
    while True:
        res = str(tem % 2) + res
        tem //= 2
        
        if tem == 0:
            break

    return res

aa = binary(a)
bb = binary(b)

c = aa * bb
print(b_to_number(c))