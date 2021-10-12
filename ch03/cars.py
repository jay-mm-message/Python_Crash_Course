cars = []
cars.append('bmw')
cars.append('audi')
cars.append('toyota')
cars.append('subaru')

print(f"1> origin: {cars}")
cars.sort()
print(f"2> sort: {cars}")
cars.sort(reverse=True)
print(f"3> reverse=true sort: {cars}")