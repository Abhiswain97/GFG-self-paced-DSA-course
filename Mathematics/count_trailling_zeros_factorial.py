n = int(input())

i = 1
mul_5 = []
while i * 5  < n:
    mul_5.append(i * 5)
    i *= 5
res = [n//i for i in mul_5]
print(f"Trailing zeros in {n}! = {sum(res)}")
