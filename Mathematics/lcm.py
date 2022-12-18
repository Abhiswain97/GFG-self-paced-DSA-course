from gcd import gcd2

def lcm(a, b):
    return (a * b)/gcd2(a, b)

a, b = list(map(int, input().split()))
print(f"LCM of {a} & {b} = {lcm(4, 6)}")