def unique_in_order(iterable):
    unique_list = []
    prev = None
    for char in iterable:
        if char != prev:
            unique_list.append(char)
        prev = char
    return unique_list


print(unique_in_order('aaaabbbbcccccaaaaaDDDD'))
print(unique_in_order('aaa'))
print(unique_in_order('11114444fvvv'))
