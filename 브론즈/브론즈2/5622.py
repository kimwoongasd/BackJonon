n = input()

tem = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time = 0

for x in n:
    t = 1
    
    for i in range(len(tem)):
        if x in tem[i]:
            t = t + i + 2
    time += t

print(time)