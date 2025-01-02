magic_Spells=['fireball', 'ice crystal', 'lightning bolt', 'tsunami']
for spell in magic_Spells:
    print(spell.title())


#2. 
pizza=['chicago', 'italian', 'NY']
for pizz in pizza:
    print(f'I like {pizz} pizza.')
print('pizza is awesome\n')


#3. 
pets = ['cat', 'dog', 'horse', 'cow', 'goat', 'sheep', 'parrot']
for pet in pets:
    print(f'A {pet} would make a great pet.')
print('All these animals are domestic and can be made pet.\n')


#4.
squares=[]
for value in range(1, 10):
    print(value)
    square=value**2
    squares.append(square)
print(squares)


squs=[]
for value in range(1, 10):
    squs.append(value**2)
print(squs)


squsLi=[val**2 for val in range(1, 11)]
print(squsLi)

cube1=[x**3 for x in range(1, 10)]
print(cube1)


#5. 

cub=[]
for value1 in range(1, 11):
    cub.append(value1**3)
print(cub)


#6. 
nums=[]
for num in range(1, 21):
    nums.append(num)
print(nums)

mill=[]
for mil in range(1, 1_000_001):
    mill.append(mil)
#print(mill)
print(min(mill))
print(max(mill))
print(sum(mill))

odd=[]
for od in range(1, 21, 3):
    odd.append(od)
print(odd)


mul=[]
for mu in range(1, 31, 3):
    mul.append(mu)
print(mul)


cubb=[]
for x in range(1, 11):  
    cubb.append(x**3)
print(cubb)



cubComp=[comp**3 for comp in range(1, 11)]
print(cubComp)


cub=[cu**3 for cu in range(1,10)]
print(cub)



#7. 
newPets = ['cat', 'dog', 'horse', 'cow', 'goat', 'sheep', 'parrot']
print(f'The first three pets in the list are: {newPets[:3]}')
print(f'The middle three pets in the list are: {newPets[2:5]}')
print(f'The first three pets in the list are: {newPets[-3:]}')



#8.
my_pizza=['chicago', 'italian', 'NY']
friends_pizza=my_pizza[:]
my_pizza.append('Americana')
friends_pizza.append('Caesar')
print('my fav pizza are:')
for pizza in my_pizza:
    print(pizza)

print('my friends fav pizza are:')
for pizza in friends_pizza:
    print(pizza)

for pizza in my_pizza:
    print(pizza)

for pizza in friends_pizza:
    print(pizza)