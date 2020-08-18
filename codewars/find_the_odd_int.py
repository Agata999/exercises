def find_the_odd_numbers(seq):
    return ', '.join([str(i) for i in set(seq) if seq.count(i) % 2 != 0])


print(find_the_odd_numbers([2, -2, 3, 4, 2, -2, 4]))
print(find_the_odd_numbers([2, -2, 3, 4, 2, -2, 4, 4, 3]))
print(find_the_odd_numbers([2, -2, 3, 4, 2, -2, 4, 4, 3, 2]))
