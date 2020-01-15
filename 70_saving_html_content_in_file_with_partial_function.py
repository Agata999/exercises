import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)
    open(file_path, "w+")
    with open(file_path, "wb") as f:

        f.write(r.content)


save_url_to_dir = functools.partial(save_url_file, dir='/home/agata/Documents', msg='Please wait - the file {} will be downloaded')

url = 'http://concerts-finder.herokuapp.com'
file = 'carousel.html'
save_url_to_dir(url=url, file=file)

url = 'http://concerts-finder.herokuapp.com/top10/'
file = 'top.html'
save_url_to_dir(url=url, file=file)
