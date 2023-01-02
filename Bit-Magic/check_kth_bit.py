def is_kth_set(n, k):
    return "yes" if n & (1 << (k -1)) else "no"

print(is_kth_set(2, 2))