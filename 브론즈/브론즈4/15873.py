n = input()

# res = 0
# tem = 0
# for x in n:
#     if int(x) == 0:
#         res -= tem
#         tem *=10
#         res += tem
        
#     tem = int(x)
#     res += int(x)
    
# print(res)

if len(n) == 4:
    print(20)
elif len(n) == 2:
    print(int(n[0]) + int(n[1]))
else:
    if n[1] == "0":
        print(10 + int(n[2]))
    else:
        print(10 + int(n[0]))