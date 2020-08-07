def find_outlier(integers):
    even_list = []
    odd_list = []
    for i in integers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if len(even_list) > len(odd_list):
        return odd_list[0]
    return even_list[0]


print(find_outlier([2, 10, 56, 3, 4, 16]))
print(find_outlier([1, 9, 6, 3, 5, 15]))
