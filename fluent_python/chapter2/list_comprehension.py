import array

symbols='$¢£¥€¤'
#codes = []
#for symbol in symbols:
#    codes.append(ord(symbol))
print('Using list comprehensions')
codes = [ord(symbol) for symbol in symbols]
print(codes)

# LOCAL SCOPE
x='ABC'
codes=[ord(x) for x in x]
print(f'x={x} ,codes={codes}')

x='ABC'
codes=[last := ord(c) for c in x]
print(f'x={x} ,codes={codes}, last={last}')

# GENERATORS
print('Using list generators')
codes = (ord(symbol) for symbol in symbols)
print(f'Printing a generator {codes}')
t = tuple(ord(symbol) for symbol in symbols)
print(f'Printing as tuple ={t}')

