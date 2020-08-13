def alphabet_position(text):
    letters = [char.lower() for char in text if char.isalpha()]
    return ' '.join(str(ord(letter)-96) for letter in letters)


print(alphabet_position('xDjELrAeCDoXIPlGwpgvAEkKLXNIvtEMfLHIOfJVweEiIXeylEuwbMKvreNIsownvFPHanqaekbWGOKpvLMlCpLwkStxFLLaxYWR'))
print(alphabet_position('x7ELr XIP'))
