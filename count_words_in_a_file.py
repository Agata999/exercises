import os


def counting_words(path):
    with open(path, 'r', encoding='utf-16') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


path = r'c:\temp\test.txt'

if os.path.isfile(path):
    print(f'There are {counting_words(path)} words in the file {path}')

os.path.isfile(path) and print(f'There are {counting_words(path)} words in the file {path}')
