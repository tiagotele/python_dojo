value = 9223372036854775801
previous = 9

while value > previous:
    previous = value
    value = value + 1
    print(f"Previous = {previous}, value = {value}")

print(f"Biggest = {value}")
