projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for n, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print(f'{n+1}. The leader of {p} started {d} is {l}')



