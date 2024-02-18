def is_power_of_five(n):
    while n % 5 == 0:
        n /= 5
    return n == 1

def is_power_of_two(n):
    return n & (n - 1) == 0 and n != 0
