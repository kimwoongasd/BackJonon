res = 0
num = 0

for i in range(9):
    tem = int(input())
    
    if tem > res:
        res = tem
        num = i + 1
print(res)
print(num)