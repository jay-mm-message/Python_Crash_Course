motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

motocycles2 = []
motocycles2.append('honda')
motocycles2.append('yamaha')
motocycles2.append('suzuki')


print(f":1: {motocycles}")
print(f":2: {motocycles2}")

del motocycles[0]
print(f":3: {motocycles}")
print(f":4: {motocycles2}")

first_owned = motocycles2.pop(0)
print(f":5: {motocycles}")
print(f":6: {motocycles2}")

print(f"first_owned: {first_owned}.") 

