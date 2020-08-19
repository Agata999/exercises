def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return [signature[i] for i in range(0,n)]
    res = signature
    for i in range(3, n):
        res.append(res[i-1] + res[i-2] + res[i-3])
    return res


print(tribonacci([1, 2, 3], 10))
print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 0], 0))
print(tribonacci([0, 1, 0], 3))
