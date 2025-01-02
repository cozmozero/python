#1.
alien_0={'color':'green',
         'points':10}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

new_pt = alien_0['points']
print(f'Congrats! You just earned {new_pt} points.')

#2.
alien_0['x_pos']=0
alien_0['y_pos']=23
print(alien_0)

#3.
alien_1={}
alien_1['color']='yellow'
alien_1['points']='10'
alien_1['x_pos']='5'
alien_1['y_pos']='30'
print(alien_1)
alien_1['y_pos']='35'
print(alien_1)


#4.
print(alien_1.get('speed', 'No speed value assigned!'))


#5.
for key, value in alien_1.items():
    print(f'key:{key}')
    print(f'value:{value}')

#6.
avai_toppings = {
    'top_1':'mushroom', 
    'top_2':'onions', 
    'top_3':'chicken', 
    'top_4':'bacon', 
    'top_5':'cheese'
    }
for toppings, items in avai_toppings.items():
    print(f'Here are the toppings: {toppings} with their items: {items.title()}')

    if toppings in avai_toppings:
        name_tops = avai_toppings[toppings].title()
        print(name_tops)


for toppings in avai_toppings.values():
    print(f'toppings list: {toppings.title()}')

for toppings in avai_toppings.keys():
    print(f'toppings list: {toppings.title()}')


if 'pineapple' not in avai_toppings.values():
    print('please add pineapple to the toppings list')


#7.
for toppings in sorted(avai_toppings.values()):
    print(f'{toppings} is available in order')


#8. 
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for lang in set(fav_languages.values()):
    print(lang.title())


#9. 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
           
aliens=[alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


#10. 
#empty list
aliens1=[]

#make 30 aliens
for alien in range(0, 30):
    new_a={'color': 'green', 'points':10, 'speed': 'slow'}
    aliens1.append(new_a)
print(aliens1)

#showing the first 5
for aliens in aliens1[:5]:
    print(aliens)
print('...')

#showing how many aliens created
print(f'total number of aliens: {len(aliens1)}')


#11. chainging colors using if
for alien in aliens1[:15]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['points']=20
        alien['speed']='fast'
for aliens in aliens1:
    print(aliens)
    

#12. 
pizza={
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#summarizing the order
print(f'you ordered a {pizza['crust']} crust pizza '
      'with the following toppings:')
for toppings in pizza['toppings']:
    print('\t' + toppings)


#13.
fav_lang = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, language in fav_lang.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for lang in language:
        print(f'\t{lang.title()}')


#13. 
usr_L = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
 }

for usr_Name, usr_info in  usr_L.items():
    print(f'\nUsername: {usr_Name}')
    fullNam=f'{usr_info['first']} {usr_info['last']}'
    locatio=usr_info['location']
    
    print('\tFull Name: ' f'{fullNam.title()}')
    print('\tLocation: 'f'{locatio.title()}')

