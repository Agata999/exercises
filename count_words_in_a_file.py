import os


file = '/home/agata/Documents/test.txt'

text = open(file, 'r')
print(text.read(6))


def counting_words(file):
    with open(file, 'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


if os.path.isfile(file):
    print(f'There are {counting_words(file)} words in the file {file}')

os.path.isfile(file) and print(f'There are {counting_words(file)} words in the file {file}')
