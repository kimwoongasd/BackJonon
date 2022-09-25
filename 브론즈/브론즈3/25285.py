n = int(input())

for i in range(n):
    h, w = map(int, input().split())
    h_m = h * 0.01
    
    bmi = w / (h_m * h_m)
    res = 0
    if h < 140.1:
        res = 6
    elif 140.1 <= h < 146:
        res = 5
    elif 146 <= h < 159:
        res = 4
    elif 159 <= h < 161 and (bmi >= 16.0 and bmi < 35.0):
        res = 3
    elif 159 <= h < 161 and (bmi < 16.0 or bmi >= 35.0):
        res = 4
    elif 161 <= h < 204 and (bmi >= 20.0 and bmi < 25.0):
        res = 1
    elif 161 <= h < 204 and ((bmi >= 18.5 and bmi < 20.0) or (bmi >= 25.0 and bmi < 30.0)):
        res = 2
    elif 161 <= h < 204 and ((bmi >= 16.0 and bmi < 18.5) or (bmi >= 30.0 and bmi < 35.0)):
        res = 3
    elif 161 <= h < 204 and (bmi < 16.0 or bmi >= 35.0):
        res = 4
    else:
        res = 4
    print(res)