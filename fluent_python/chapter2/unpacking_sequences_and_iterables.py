import os

lax_coordinates = (33.9425, --118.408056)
latitude, longitude = lax_coordinates
print(f'latitude={latitude}')
print(f'longitude={longitude}')
divmod(20,8)
t=(20,8)
print(f'result divmod(*t) = {divmod(*t)}')
quotient, remainder = divmod(*t)
print(f'quotient, remainder = {quotient, remainder}')

f, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(f'f={f}')
print(f'filename={filename}')

# Using *  to grab excess items

a, b, *rest = range(5)
print(f'all={a, b, rest}')
a, b, *rest = range(3)
print(f'all={a, b, rest}')
a, b, *rest = range(2)
print(f'all={a, b, rest}')
a, *body, c, d = range(5)
print(f'all={a, body, c, d}')
*head, b, c, d = range(5)
print(f'all={head, b, c, d}')

# Using * in functiona calls and sequence literals

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*[1,2], 3, *range(4,7)))

print(*range(4), 4)
print([*range(4), 4])
print({*range(4), 4, *(5,6,7)})

