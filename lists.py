#1. 

names =['lyn', 'adi', 'niki', 'leon']
print(names[0].title())
print(names[1])
print(names[2])
print(names[3])


#2.

print(f'Hello, {names[0]}, how are you doing today?')
print(f'Hello, {names[2]}, how are you doing today?')
print(f'Hello, {names[1]}, how are you doing today?')
print(f'Hello, {names[3]}, how are you doing today?')


#3.
trans=['motorcycle', 'car', 'boat', 'plane']
print(f'I would like to own and ride a top-of-the-line Honda {trans[0]} one day!')


#4.
bikes=['Honda', 'Bajaj', 'Hero', 'KTM']
print(bikes[0])
bikes[0]='Kawasaki'
print(bikes[0])
bikes.append('Honda')
print(bikes)


#5.
cars=[]
cars.append('Toyota')
cars.append('Ford')
cars.append('Nissan')
cars.append('Suzuki')
print(cars)

cars.insert(0, 'VW')
print(cars) 

del cars[3]
print(cars)

deletedCar=cars.pop()
print(deletedCar)

deletedCar1=cars.pop(1)
print(deletedCar1)

deletedCar2='VW'
cars.remove(deletedCar2)
print(deletedCar2)


#6. 
dinner_invite=['elon musk', 'joe rogan', 'nikola tesla']
print(f'Hello, {dinner_invite[0]}, you are invited to dinner tonight at 7PM at the Grand Regalia.')
print(f'Hello, {dinner_invite[1]}, you are invited to dinner tonight at 7PM at the Grand Regalia.')
print(f'Hello, {dinner_invite[2]}, you are invited to dinner tonight at 7PM at the Grand Regalia.')

print(f"Unfortunately, {dinner_invite[2]} couldn't make it to the dinner because of an experiment that he needed to take care of.")

dinner_invite[2]='jakob somet'
print(f'Hello, {dinner_invite[2]}, you are invited to dinner tonight at 7PM at the Grand Regalia.')

dinner_invite.insert(0, 'nick fury')
dinner_invite.insert(3, 'jason hardy')
dinner_invite.insert(5, 'john doe')
dinner_invite.insert(6, 'joe doe')
print(dinner_invite)

print('Becuase of logistics issue, i can only fit two people on the table for the dinner. Sorry for the inconvenience caused.')
del_guest=dinner_invite.pop(5)
print(f'sorry, {del_guest}, but we will have to reschedule our dinner on some further date.\n')
del_guest=dinner_invite.pop(4)
print(f'sorry, {del_guest}, but we will have to reschedule our dinner on some further date.\n')
del_guest=dinner_invite.pop(3)
print(f'sorry, {del_guest}, but we will have to reschedule our dinner on some further date.\n')
del_guest=dinner_invite.pop(2)
print(f'sorry, {del_guest}, but we will have to reschedule our dinner on some further date.\n')
del_guest=dinner_invite.pop(0)
print(f'sorry, {del_guest}, but we will have to reschedule our dinner on some further date.\n')

del dinner_invite[0]
del dinner_invite[0]
print(dinner_invite)


#7. 
locations = ['NY', 'LA', 'Tokyo', 'Sydney', 'Paris', 'Singapore']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

locations.reverse()
print(locations)

print(len(locations))

print('Here are the number of people invited to dinner:', len(dinner_invite))


#8.
location1=locations[7]
print(location1)



