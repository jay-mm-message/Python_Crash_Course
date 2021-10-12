motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)

motocycles[0] = 'honda'
print(motocycles)

motocycles.append('ducati')
print(motocycles)


motocycles2 = []
print(motocycles2)
motocycles2.append('honda')
motocycles2.append('yamaha')
motocycles2.append('suzuki')
print(motocycles2)


motocycles2.insert(0, 'ducati')
print(motocycles2)


del motocycles2[0]
print(motocycles2)
