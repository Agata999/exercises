ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = [(start, stop) for start in ports for stop in ports if start != stop]
print(connections)
print(len(connections))

single_connections = [(start, stop) for start in ports for stop in ports if start < stop]
print(single_connections)
print(len(single_connections))
