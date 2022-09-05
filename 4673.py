def number(x):
    tem = 0
    for num in str(x):
        tem += int(num)
        
    return x + tem

non_self_number = []

for i in range(1, 10001):
    num = number(i)
    if num not in non_self_number:
        non_self_number.append(num)
        
for i in range(1, 10001):
    if i not in non_self_number:
        print(i)