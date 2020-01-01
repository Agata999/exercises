ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = ((start, stop) for start in ports for stop in ports if start != stop)
counter = 0
for (start, stop) in connections:
    print(f'Connection: {start} -> {stop}')
    counter += 1
print(f'{counter} connections')

print('-'*30)

single_connections = ((start, stop) for start in ports for stop in ports if start < stop)
counter = 0
for (start, stop) in single_connections:
    print(f'Connection: {start} -> {stop}')
    counter += 1
print(f'{counter} single connections')
