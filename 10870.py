def fibonacci_numbers(n):
    if n < 3:
        return ls[n]
    else:
        fibonacci_numbers(n - 1)
        ls[n] = ls[n - 1] + ls[n - 2]
        
n = int(input())
ls = [0 for _ in range(n + 3)]
ls[1] = 1
ls[2] = 1
if n == 0:
    print(0)
else:
    fibonacci_numbers(n)
    print(ls[n])