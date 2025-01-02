cars=['audi', 'bmw', 'mercedes', 'toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


#2. 
car='audi'
print (car.title()=='Audi')

#3.
if car!='BMW':
    print('tis not a Beemer')

#4.
answ = 200
if answ != 100:
    print('Sike!!!thats the wrong number!')


#5. 
person1=23
person2=17
print(person1 and person2>=18)

person3=23
person4=17
print((person3>=18) or (person4>=18))


#6. 
toppings = ['mushroom', 'onions', 'chicken']
print('chicken' in toppings)


#7. 
ban_user=['andrea', 'salan', 'arron', 'aaron', 'jack']
usr='don'
if usr not in ban_user:
    print(f'{usr.title()}, you are invited to comment in our forum')


#8.
car='subaru'
if car=='subaru':
    print ("is car =='subaru'?  I predict true.")
else:
    print("\nIs car == 'audi'? I predict false.")


#9.
req_toppings = ['mushroom', 'onions', 'chicken']
for req_topping in req_toppings:
    if req_topping=='onions':
        print('sorry! all out of onions!')
    else:
        print(f'Adding topping: {req_topping.title()}')


#10.
req_toppings1=[]
if req_toppings1:
    for req_topp in req_toppings1:
        print(f'Adding toppings: {req_topp.title()}')
    print('\nfinished adding toppings. Pizza ready to be served.')
else:
    print('are you sure you want a plain pizza?')


#11.
avai_toppings = ['mushroom', 'onions', 'chicken', 'bacon', 'cheese']
req_toppi=['mushroom', 'chicken', 'pineapple']

for req_topp in req_toppi:
    if req_topp in avai_toppings:
        print(f'adding topping: {req_topp.title()}')
    else:
        print(f'{req_topp.title()} not available. Choose another.')
print('Your pizza is ready')
