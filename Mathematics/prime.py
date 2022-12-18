n = int(input())

# O(sqrt(n))
def is_prime(n):
    if n == 1: return False
    if n == 2: return True

    i = 2
    while (i*i <= n):
        if n % 2 == 0 or n % 3 == 0: 
            return False
        if n % i == 0:
            return False
        i += 1

    return True

if is_prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
