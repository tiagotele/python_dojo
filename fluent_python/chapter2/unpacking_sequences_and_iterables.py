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
