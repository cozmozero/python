#1. 
# msg = input('enter info here:')
# print(msg)

# nam='You must enter your full Name here.'
# nam+='\nEnter your name: '

# name=input(nam)

# ag='\nEnter your age: '
# age=int(input(ag))

# print(f'\nHello, {name.title()}, youre {age} yeard old!')

# if age >=18:
#     print (f"Congratulations, {name.title()}, you're eligible to vote in the coming Elections 2024.")
# else:
#    print (f"Unfortunately, {name.title()}, you're NOT eligible to vote in the coming Elections 2024.") 



#2. even/odd

num = input('Enter number to find out whether it is Even or Odd: ')
nums=int(num)

if nums%2==0:
    print('Even')
else:
    print('Odd')



#3. while loop
curr_num=1
while curr_num<=11:
    print(curr_num)
    curr_num+=1


#4. break
curr_num2=1
while curr_num2<=11:

    if curr_num2==5:
        break
    else:
        print(curr_num2)
        curr_num2+=1


# prompt = 'Enter the city name you would like to visit?'
# prompt += 'Enter quit to quit.'

# while True:
#     city = input(prompt)

#     if city=='quit':
#         break
#     else:
#         print(f'I would love to visit {city.title()}.')


#4. continue
curr_num2=1
while curr_num2<=11:
    curr_num2+=1

    if curr_num2%2==1:
        continue
    print(curr_num2)
        


#5.
unconfirmedUsers=['alice', 'brad', 'chloe', 'dan']
confUser=[]

while unconfirmedUsers:
    currentUsr=unconfirmedUsers.pop()

    print(f'verifying user:{currentUsr.title()}')
    confUser.append(currentUsr)

print('\nConfirmed users:')
for confirmedUsr in confUser:
    print(confirmedUsr.title())

print(unconfirmedUsers)
print(confUser)



#6.
pets=['dog', 'cat', 'cow', 'cat', 'horse', 'cat', 'rabbit', 'wolf', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#7.
final_response={}
itr1=0
itr2=0

#set a flag
polling_active=True

while polling_active:
    #prompting the user name and response
    name = input('Enter your name: ')
    user_response=input('Who did you vote for? ')

    #storing the response
    final_response[name]=user_response

    #find out if anyone is taking the poll
    repeat=input('Would you like to let another person respond? (yes/no) ')
    if repeat=='no':
        polling_active=False

#poling is complete. Show the result
print('\n---Poll Results---')
for name, response in final_response.items():
    print(f'{name} : {response}')
    
    if response=='trump':
        itr1+=1
    if response=='harris':
        itr2+=1

print('\n---Total Poll Results---')
print('Trump: ', itr1)
print('Harris: ', itr2)





