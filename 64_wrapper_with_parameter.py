from datetime import datetime as dt
import functools
import os


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path, 'a')) as f:
                f.write(f'Action {logged_action} executed on {path} on {dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', '/home/agata/Documents/file_create.txt')
def create_file(path):
    print(f'Creating file {path}')
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', '/home/agata/Documents/file_delete.txt')
def delete_file(path):
    print(f'Deleting file {path}')
    os.remove(path)


create_file('/home/agata/Documents/file.txt')
delete_file('/home/agata/Documents/file.txt')
create_file('/home/agata/Documents/file.txt')
delete_file('/home/agata/Documents/file.txt')
