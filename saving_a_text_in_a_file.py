def log_it(*args):
    path = '/home/agata/Documents/log_it.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')