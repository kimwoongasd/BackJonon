n = input()
tem = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in tem:
    n = n.replace(x, "*")

print(len(n))