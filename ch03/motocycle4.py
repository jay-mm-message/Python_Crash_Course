motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

motocycles2 = []
motocycles2.append('honda')
motocycles2.append('yamaha')
motocycles2.append('suzuki')

print(motocycles)
print(motocycles2)

del motocycles[0]
print(motocycles)
print(motocycles2)

first_owned = motocycles2.pop(0)
print(motocycles)
print(motocycles2)

print(f"first_owned: {first_owned}.")
