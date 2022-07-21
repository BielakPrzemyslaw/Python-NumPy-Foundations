tools = {
    'a' : 'reamer',
    'b' : 'turning',
    'c' : 'milling'
}

tools
#print {'a': 'reamer', 'b': 'turning', 'c': 'milling'}

tools['a']
#print reamer

tools['d'] = 'tap'
tools
#print {'a': 'reamer', 'b': 'turning', 'c': 'milling', 'd': 'tap'}

tools.keys()
#print dict_keys(['a', 'b', 'c', 'd'])

tools.values()
#print dict_values(['reamer', 'turning', 'milling', 'tap'])

list(tools.keys())
#print ['a', 'b', 'c', 'd']

tools.get('a')
#print 'reamer'