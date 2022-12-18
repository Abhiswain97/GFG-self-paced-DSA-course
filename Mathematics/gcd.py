a, b = list(map(int, input().split()))

# Using repeated substraction
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

# Using modulo 
def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)

print(f"GCD of {a}, {b} = {gcd(a, b)}")
print(f"GCD of {a}, {b} = {gcd2(a, b)}")