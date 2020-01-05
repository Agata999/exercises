def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 2
print(f'The start number is {number}')
transformations = [double, root, negative, div2]
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print(f'The result for {transformation.__name__} and the temporary value is now {tmp_return_value}')

print('*'*30)

number = 3
print(f'The start number is {number}')
transformations = [root, root, div2, double]
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print(f'The result for {transformation.__name__} and the temporary value is now {tmp_return_value}')
