def duplicate_count(text):
    new_text = text.lower()
    result = 0
    for char in set(new_text):
        if new_text.count(char) > 1:
            result += 1
    return result


print(duplicate_count('aaacdevfF'))
print(duplicate_count('cdevfF'))
print(duplicate_count('bB11cdevfF'))
