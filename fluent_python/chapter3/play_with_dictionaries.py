import sys
from collections import abc
print(sys.version)
my_dict = {}
print(isinstance(my_dict, abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, frozenset([30, 40]))
try:
    print(hash(tl))
except TypeError as e:
    print(e)

a = dict(one=1, two=2, three=3)
b = {'three': 3, 'two': 2, 'one': 1}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
e = dict({'three': 3, 'one': 1, 'two': 2})

dial_codes = [
(880, 'Bangladesh'),
(5, 'Brazil'),
(86, 'China'),
(91, 'India'),
(62, 'Indonesia'),
(81, 'Japan'),
(234, 'Nigeria'),
(92, 'Pakistan'),
(7, 'Russia'),
(1, 'United States'),
]       

country_dial = {country: code for code, country in dial_codes}
print(dial_codes)
print(country_dial)

custom = {code: country.upper()
        for country, code in sorted(country_dial.items())
        if code < 70
}
print(custom)

from random import shuffle
print(f'Before = {country_dial}')
shuffle(dial_codes)
country_dial = {country: code for code, country in dial_codes}
print(f'After = {country_dial}')
