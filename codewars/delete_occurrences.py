def delete_nth(order, max_e):
    new_list = []
    for num in order:
        if new_list.count(num) < max_e:
            new_list.append(num)
    return new_list


print(delete_nth([1, 1, 1, 2, 4, 4, 5], 2))
print(delete_nth([1, 1, 1, 2, 4, 4, 5], 1))
print(delete_nth([1, 1, 1, 2, 4, 4, 5], 0))
