motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

print(motocycles)
pop_motocycle = motocycles.pop()
print(motocycles)
print(pop_motocycle)

motocycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop()
print(f"The last motocycle I owned was a {last_owned.title()}")