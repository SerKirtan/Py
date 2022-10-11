planets = ['Mercury', 'Venus', 'Earth', 'Mars','Jupiter','Saturn','Uranus','Neptune']
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
print(planets)
print(len(planets))

planets.append('Pluto')
# The planets sorted in alphabetical order
print(sorted(planets))

planets.pop()
print("\n",planets)
print(planets.index('Earth'))