def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(action, numbers):
    result = []
    for number in numbers:
        result.append(action(number))
    return result


numbers = [2, 3, 4]
print(generate_values(root, numbers))
