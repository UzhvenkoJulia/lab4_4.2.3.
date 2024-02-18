def is_power_of_five(n):
    while n % 5 == 0:
        n /= 5
    return n == 1
