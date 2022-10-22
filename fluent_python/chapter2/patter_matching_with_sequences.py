metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.68, 139.69)),
    ('Delhi NCR', 'IN', 21.935, (28.61, 77.20)),
    ('Mexi City', 'MX', 20.142, (19.43, -99,13)),
    ('New Yowrk-Neward', 'IS', 20.104, (40.80, -74.02)),
    ('São Paulo', 'BR', 19.649, (-23.54, -46.63)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
main()
