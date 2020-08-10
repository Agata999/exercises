def rgb(r, g, b):
    ref = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }

    decimal_tuple = (r, g, b)
    results = []

    for n in decimal_tuple:

        if n < 0:
            n = 0
        elif n > 255:
            n = 255

        int_number, remainder = divmod(n, 16)
        if int_number in range(10):
            results.append(str(int_number))
        else:
            results.append(ref[str(int_number)])

        if remainder in range(10):
            results.append(str(remainder))
        else:
            results.append(ref[str(remainder)])
    return "".join(results)


print(rgb(0, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))
