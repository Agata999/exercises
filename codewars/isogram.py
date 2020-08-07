def is_isogram(string):
    return len(string) == len(set(string.lower()))


print(is_isogram("adam"))
print(is_isogram("maniok"))
