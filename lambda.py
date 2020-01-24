text_list = ['x', 'xxx', 'xxxx', 'xxxxx', '']
f = lambda x: len(x)
print(f('napis'))

print(list(map(lambda x: len(x), text_list)))
