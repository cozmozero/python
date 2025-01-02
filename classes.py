#1. creating a class -
class Dog:
    '''modeling a dog'''

    def __init__(self, name, age, breed):
        '''initialize name and age attributes'''
        self.name=name
        self.age=age
        self.breed=breed

    def sit(self):
        '''simulate a dog sitting in response to a command'''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''simulate a dog roling over in response to a command'''
        print(f'{self.name} rolled over!')
    

#2. creating an instance - 
my_dog=Dog('Jojo', 2, 'Retriever')

print(f'My dogs name is {my_dog.name} and he is {my_dog.age} years old, and he is a {my_dog.breed}.')

my_dog.sit()
my_dog.roll_over()



#3. a new instance - 
new_dog=Dog('Mojo', 3, 'Husky')

print(f'My dogs name is {new_dog.name} and he is {new_dog.age} years old, and he is a {new_dog.breed}.')
new_dog.sit()
new_dog.roll_over()


#4. ex-1
class Restaurant:
    '''creating a restaurant'''

    def __init__(self, restro_name, cuisine_type):
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type

    def describe_restro(self):
        print(f'{self.restro_name} is my restaurant, it serves {self.cuisine_type} food. You are very much welcome to visit us.')

    def open_restro(self):
        print(f'{self.restro_name} is now open for business!!!')

my_restr=Restaurant('SkyNess', 'Indian')
my_restr.describe_restro()
my_restr.open_restro()


#5. ex-2
new_restr=Restaurant('Longin For Food', 'Italian')
new_restr.describe_restro
new_restr.open_restro

yr_restro=Restaurant('DimSum', 'Chinese')
yr_restro.describe_restro()
yr_restro.open_restro()

xl_restro=Restaurant('Letsagoooo', 'Continental')
xl_restro.describe_restro()
xl_restro.open_restro()


#6. ex-3
class User:

    def __init__(self, fName, lName, age, id, nationality, subject):
        self.fName=fName
        self.lName=lName
        self.age = age
        self.id=id
        self.nationality=nationality
        self.subject=subject

    def describe_User(self):
        print(f'The users description:')
        print(f'{self.fName} {self.lName} {self.age} {self.id} {self.nationality} {self.subject}')       


    def greet_user(self):
        print(f'Hello, {self.fName.title()} {self.lName.title()}. Welcome to the USA!')

     
new_Usr = User('Joe', 'doe', 21, 101011, 'French', 'French Cuisine')
new_Usr.describe_User()
new_Usr.greet_user()



#7. classes and instances - 
class Car():
    ''' attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        '''return a neatly formatted desc name'''

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''print a statement showing the car's milage'''
        odo_reading = 'This car has ' + str(self.odometer_reading) + ' miles on it.'
        return odo_reading
    
    def update_odo(self, mileage):
        '''setting odo reading to given value
        also reject the change if it attempts to roll the odo back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Warning! You cant roll back the odo reading.')

    def increment_odo(self, miles):
        '''adding the given amount to odo reading'''
        self.odometer_reading+=miles
    
my_new_car = Car('bmw', 'm4 comp', 2024)
my_newest_car = Car('toyota', 'supra', 2025)
print(my_newest_car.get_descriptive_name())


# manually changing the odo/attribute value
my_newest_car.odometer_reading=1000
print(my_newest_car.read_odometer())


# using method to update the odometer/attribute value
my_newest_car.update_odo(1010)
print(my_newest_car.read_odometer())
my_newest_car.update_odo(101)

# incrementing the odometer/attribute value through a method
my_used_car=Car('toyoto', 'hilux', 2001)
print(my_used_car.get_descriptive_name())
my_used_car.update_odo(210091)
print(my_used_car.read_odometer())
my_used_car.increment_odo(23054)
print(my_used_car.read_odometer())



# taken from class inheritance below - from #9. 
class Battery():
    '''attempting to model a battery of an EV'''

    def __init__(self, battery_size=100):
        '''initialize the battery's attribute'''
        self.battery_size=battery_size

    def describe_battery(self):
         '''prints battery size '''
         print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        '''print statement about battery's range'''
        if self.battery_size ==100:
            range = 300
        elif self.battery_size ==150:
            range = 400
        
        message = 'This car can go approx. ' + str(range)
        message += 'miles on a full charge.'

        print (message)


#8. Inheritance - 
class ElectricCar(Car):
    ''' represent aspect of a car, specific to EVs'''
    def __init__(self, make, model, year):
        '''initialize attributes of the Parent Class'''
        super().__init__(make, model, year)
        self.battery=Battery()

    def describe_battery(self):
        '''prints battery size '''
        print(f'The {self.make.title()} {self.model.title()} has a battery size of {self.battery}-kWh.')

    def fill_gas(self):
        '''EVs dont need gas.'''
        print('EVs dont need no gas.')

my_tesla=ElectricCar('tesla', 'model 3', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas()


#9. instances as attributes -
class Battery():
    '''attempting to model a battery of an EV'''

    def __init__(self, battery_size=100):
        '''initialize the battery's attribute'''
        self.battery_size=battery_size

    def describe_battery(self):
         '''prints battery size '''
         print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        '''print statement about battery's range'''
        if self.battery_size ==100:
            range = 300
        elif self.battery_size ==150:
            range = 400
        
        message = 'This car can go approx. ' + str(range)
        message += 'miles on a full charge.'

        print (message)

my_tesla.battery.get_range()



#10. importing classes - 

from cars_class_to_import import Car

my_new2_car= Car ('ford', 'mustang', 2025)
print(my_new2_car.get_descriptive_name())

my_new2_car.odometer_reading=55
my_new2_car.read_odometer()


#11. storing multiple Classes in a module - 
from cars_class_to_import import ElectricCar

my_rivian = ElectricCar ('rivian', 'lucid', 2022)

print(my_rivian.get_descriptive_name())
my_rivian.battery.describe_battery()
my_rivian.battery.get_range()


#12. importing multiple classes - 
from cars_class_to_import import Car, ElectricCar

my_beetle=Car ('vw', 'beetle', 2010)
print(my_beetle.get_descriptive_name())

my_mi= ElectricCar('mi', 'su7', 2025)
print(my_mi.get_descriptive_name())


#13. importing entire modules - 
import cars_class_to_import as C
my_lambo= C.Car('lamborghini', 'revulto', 2025)
print(my_lambo.get_descriptive_name())

my_audi= C.ElectricCar('audi', 'r8-e', 2024)
print(my_audi.get_descriptive_name())


#14. importing all classes from module - 
from cars_class_to_import import * #not used much


#15. importing a module into another module - 
from cars_class_to_import import Car
from electric_car import ElectricCar

my_lambo2= Car('lamborghini', 'aventador svj', 2025)
print(my_lambo2.get_descriptive_name())

my_mustang= ElectricCar('ford', 'mustang mach-e', 2024)
print(my_mustang.get_descriptive_name())



#16. py standard library - 
from collections import OrderedDict

fav_lang = OrderedDict()

fav_lang['jen'] = 'python'
fav_lang['sarah'] = 'c'
fav_lang['edward'] = 'ruby'
fav_lang['phil'] = 'python'

for name, lang in fav_lang.items():
    print(name.title() + "'s fav language is " + lang.title())



#17. styling classes - 


