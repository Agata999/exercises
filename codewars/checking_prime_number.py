def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


print(is_prime(24))
print(is_prime(7))
print(is_prime(9))
print(is_prime(10))
print(is_prime(13))
print(is_prime(-13))
