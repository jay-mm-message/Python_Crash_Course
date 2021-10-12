motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')
motorcycles.append('suzuki')

print(f":1: {motorcycles}")
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f":2: {too_expensive.title()} is too expensive for me.")
print(f":3: {motorcycles}")
