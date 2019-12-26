import urllib.request
import os

data_dir = '/home/agata/Documents'
pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'courses', 'url': 'http://www.kursyonline24.eu/'}]

for page in pages:

    try:
        file_name = f'{page["name"]}.html'
        path = os.path.join(data_dir, file_name)

        print(f'Processing: {page["url"]}  => {file_name} ...')
        urllib.request.urlretrieve(page["url"], path)
        print('...done')

    except Exception:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')
