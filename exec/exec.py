import os

files_to_process = [
    r"/home/agata/Desktop/Python/exec/operation1.py",
    r"/home/agata/Desktop/Python/exec/operation2.py"
    ]

for file in files_to_process:
    print(f'File {os.path.basename(file)}:')
    with open(file, 'r') as f:
        source = f.read()
        exec(source)
