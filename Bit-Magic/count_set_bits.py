# Brian - Kerningham algorithm

def count(n):
    res = 0
    
    while n > 0:
        n = n & (n - 1)
        res += 1
    
    return res

n = int(input("Enter the number: "))

print(f"Set bits = {count(n)}")