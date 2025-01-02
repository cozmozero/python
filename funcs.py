def greet_user():
    #display a greeting msg
    print('hello!')

greet_user()



# with param - 
def greet_usr(username):
    print(f'hello, {username}!')

greet_usr('sky')


#3. ex-1 
def display_message():
    print("hello all, i'm learning Python's function in this chapter.")

display_message()


#4. ex-2
def fav_book(title):
    print(f'One of my favorite books is {title}.')

fav_book('A Song of Ice and Fire')


#5. positional
def describing_pets(type, name):
    print(f'\nI have a {type}')
    print(f"My {type}'s name is {name.title()}")

describing_pets('cat', 'jojo')
describing_pets('dog', 'borko')


#6. keyword - 
def describ_pets(type, name):
    print(f'\nI have a {type}')
    print(f"My {type}'s name is {name.title()}")

describ_pets(name='jojo', type='cat') #order doesnt matter as param as defined with args


#7. with default values - 
def describ_pets1(name, type='dog'):
    print(f'\nI have a {type}')
    print(f"My {type}'s name is {name.title()}")

describ_pets1('jojo')


#8. ex-3
def make_shirt(size, text):
    print(f'Size of shirt is: {size}, and the printed message is: {text}')

make_shirt(34, 'Straight Outta Tartarus')
make_shirt(text='Straight Outta Tartarus', size=34)


#9. ex-4
def make_shirt1(size='L', text='I LOVE PYTHON'):
    print(f'Size of shirt is: {size}, and the printed message is: {text}')

make_shirt1()
make_shirt1(size='M')
make_shirt1(text='Straight Outta Tartarus')


#10. ex-5
def describe_city(city, country='US'):
    print(f'{city} is in {country}')

describe_city('NYC')
describe_city('Chicago')
describe_city('London', 'England')


#11. return values - 
def get_formatted_text(fname, lname):
    #retrn a full name
    full_name = f'{fname} {lname}'
    return full_name.title()

person=get_formatted_text('john', 'doe')
print('\n', person)


#12. optional arguments - 
def get_formatted_name(fname='', mname='', lname=''):
    #retrn a full name
    if mname:
           full_name = f'{fname} {mname} {lname}'
    
    else: 
        full_name = f'{fname} {lname}'

    return full_name.title()

persona=get_formatted_name('john', 'doe')
persona1=get_formatted_name('joe', 'nash', 'doe')
print(persona)
print(persona1)



#13. returning a dictionary - 
def get_formatted_dict(fname, lname, age=None):
    #retrn a full name as dict
    full_name = {'f_name': fname,
                 'l_name': lname
                 }
    
    if age: #optional param
        full_name['age']=age

    return full_name

person=get_formatted_dict('john', 'doe', 56)
print(person)


#14. functions with a while loop - 
def get_formatted_dict1(fname, lname, age=None):

    full_name=f'{fname} {lname}'

    if age: #optional param
        full_name['age']=age

    return full_name

while True:
    print('\nState your name: ')
    print('Press q to quit prompt.')
    
    fname=input('First Name: ')
    if fname=='q':
        break
    
    lname=input('Last Name: ')
    if lname=='q':
        break

    greet_name=get_formatted_dict1(fname, lname)
    print('\nHello,', greet_name.title())
    break


#15. ex-6
def city_country(city_name, country_name):
    city={'city': city_name,
          'country': country_name} 
    
    return city

op=city_country('Delhi', 'India')
print(op)


# #16. ex-7
# def make_album():
#     album={}



#17. PASSING A LIST

users=['hanna', 'liah', 'liam', 'jake', 'john', 'joe']

def greet_users(names):
    #printing a simple greeting
    for name in names:
        msg=f'Hello, {name.title()}. Nice to meet you.'
        print(msg)

greet_users(users)


#18. modifying a list 

#designs that need to be printed
unprinted=['case', 'robots', 'cars', 'satellite']
printed=[]

#simulate printing each design -> then move them to printed list
while unprinted:
    current_design=unprinted.pop()
    print(f'Printing model: {current_design.title()}')
    printed.append(current_design)

#display all models
print('\nThe following models have been printed: ')
for design in printed:
    print(design.title())


# 19. now writing the above code in functions - 

def print_models(unprinted_mod, printed_mod):
    while unprinted_mod:
        current_design=unprinted_mod.pop()
        print(f'Printing model: {current_design.title()}')
        printed_mod.append(current_design)

def show_completed(printed_mod):
    print('\nThe following models have been printed: ')
    for design in printed:
        print(design.title())

unprinted_mod=['bikes', 'robots', 'cars', 'satellite', 'gundam']
printed_mod=[]

print_models(unprinted_mod, printed_mod)
show_completed(printed_mod)
print(unprinted_mod)
print(printed_mod)



#20. preventing a func from modifying a list

print_models(unprinted_mod[:], printed_mod) #slicing the main list
show_completed(printed_mod)
print(unprinted_mod)
print(printed_mod)


#21. arbitrary arguments in functions - 

def make_pizza(*toppings):
    print('\nMaking the Pizza with: ')
    for topping in toppings:
        print(f'--- {topping.title()}')

make_pizza('cheese')
make_pizza('mushrooms', 'green peppers', 'extra cheese', 'pepperoni')



#22. arbi and pos args

def make_pizza1(size='M', *toppings):
    print(f'\nMaking a {size} Pizza with: ')
    for topping in toppings:
        print(f'--- {topping.title()}')

make_pizza1('M', 'cheese')
make_pizza1('L', 'mushrooms', 'green peppers', 'extra cheese', 'pepperoni')



#23. Arbitrary keyword args

def user_profile(f, l, **info):
    #build a dict using every user info
    info['first'] = f
    info['last'] = l
    return info

new_profile=user_profile('albert', 'einstein',
                         location='US',
                         field='physics')
print(new_profile)



#24. Storing Functions to Modules - 

import make_pizza as pizza

pizza.make_pizza1('XXL', 'cheese')
pizza.make_pizza1('XL', 'mushrooms', 'green peppers', 'extra cheese', 'pepperoni')



#25. impoorting specific functions from a module - 

from make_pizza import make_pizza1 as pizza

pizza('XXL', 'cheese', 'pineapple')
pizza('XL', 'mushrooms', 'green peppers', 'extra cheese', 'pepperoni')

