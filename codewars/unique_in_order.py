def unique_in_order(iterable):
    unique_list = []
    if iterable.count(iterable[0]) == len(iterable):
        unique_list.append(iterable[0])
    for i in range(0, len(iterable)):
        if iterable[i-1] != iterable[i]:
            unique_list.append(iterable[i])
    return unique_list


print(unique_in_order('aaaabbbbcccccaaaaaDDDD'))
print(unique_in_order('aaa'))
print(unique_in_order('11114444fvvv'))
