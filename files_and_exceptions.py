#1. reading an entire fle - 
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


#2. reading line by line - 
filepath = 'pi_digits.txt'

with open(filepath) as file_obj:
    for line in file_obj:
        print(line)



#3. making a list of lines
filename='pi_digits.txt'

with open (filename) as file_objN:
    lines = file_objN.readlines()

pi_string=''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


#3.1 - finding bday contained in pi
filen='pi_million.txt'

with open (filen) as fil_obj1:
    lines = fil_obj1.readlines()

pi_str = ''
for line in lines:
    pi_str+=line.strip()

bday=input('Enter your bday in ddmmyy: ')
if bday in pi_str:
    print('your bday is there in pi. Congrats.')
else:
    print('we couldnt find your bday in pi. Sorry.')





#4. writing onto a file
filename_write='pi_million_new.txt'

with open (filename_write, 'w') as file_objN:
    file_objN.write('I love python and JS')


#5. using replace() method to replace a string in a file 
# filename_ex = 'pi_million_new.txt'
# write_msg = 'this is a new file for practise'

# with open (filename_ex, 'w') as new_file_ex:
#         new_file_ex.write(write_msg)



#6. writing 
new_fil='pi_million_new.txt'

with open(new_fil, 'r+') as newly:
    newly.write('new stuff to add\n')
    newly.write('new stuff added\n')


#7. appending to a file
new_fil1='pi_million_new.txt'

with open(new_fil1, 'a') as newli:
    newli.write('this is a new appending wrtiting \n')
    newli.write('we are appending stuff here \n')


#8. input and saving to a file - 
# new_s='new_s.txt'
# namess=input('enter your name: ')

# while namess==False:    
#     if namess:
#         with open ('new_s', 'a') as new_usr:
#             new_usr.write(namess,'\n')
#         print(f'hello {namess}. Nice to meet you.')
    
#     else:
#         print('plz enter your name')

    

#9. try-except blocks 
try:
    print(5/5)
except ZeroDivisionError:
    print('you can divide by 0')


#10. a code doing only div
print('give me a number:')
print ('enter q to quit.')

while True:
    f_num = input('\n First Number: ')
    if f_num =='q':
        break
    s_num=input('\n2nd Number: ')
    try: 
        ans = int(f_num)/int(s_num)
    except ZeroDivisionError:
        print('unfortunately, you cant divide by 0')
    else:
        print (ans)


#11. file not found error - 
# filenameNew = 'new_file.txt'

# with open (filenameNew) as fnN:
#     contents = fnN.read()
 

#now using try-except for this block 
filenameNew = 'new_file.txt'

try:
    with open(filenameNew) as nfN:
        contents = nfN.read()
except FileNotFoundError:
    msg = 'Sry file not found!'
    print(msg)
print('hello. this will continue the code.')


#12. analyzing text of long files - 
filenameNew1 = 'voyage.txt'

try:
    with open(filenameNew1) as nfN1:
        contents = nfN1.read()
except FileNotFoundError:
    msg = 'Sry file not found!'
    print(msg)
else:
    #count number of words in the text
    words=contents.split()
    num_words = len(words)
    print(num_words)


#13. working with multiple files - 
def counting_words(f_name):
    '''count the approx words in the file'''
    try:
        with open(f_name) as fn:
            content = fn.read()
    except FileNotFoundError:
        msg='sry, file not found!!'
        print(msg)
    else:
        '''count the approx no. of words in the file'''
        word=content.split()
        length = len(word)
        print(length)

file=['voyage.txt', 'voyage1.txt', 'voyage2.txt', 'voyage3.txt']
for word in file:
    counting_words(word)


#14. pass keyword - 
def counting_words_new(f_name):
    '''count the approx words in the file'''
    try:
        with open(f_name) as fn:
            content = fn.read()
    except FileNotFoundError:
        msg='sry, file not found!!'
        pass
    else:
        '''count the approx no. of words in the file'''
        word=content.split()
        length = len(word)
        print(length)

file=['voyage.txt', 'voyage1.txt', 'voyage2.txt', 'voyage3.txt']
for word in file:
    counting_words_new(word)


#15.


print ('enter a number for addition:')
print ('press z to quit the program')

while True:
    ad_num = input('enter a number: ')
    if ad_num == 'z':
        break
    ad_num2 = input('enter 2nd number: ')

    try:
        answ= int(ad_num) + int(ad_num2)
    except ValueError:
        print('enter correct values.')
    else:
        print(answ)


#16. storing data - using json
# import json as js

# nums = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]

# filen = 'nums.json'
# with open (filen, 'a') as ff:
#     js.dump(nums, ff)


#17. reading data using json - 
import json as js

filess='nums.json'

with open(filess) as fs:
    loaded=js.load(fs)

print(loaded)


#17. saving and reading user-generated data - 
import json as js
usern=input('enter your name: ')

filene = 'user_name.json'

with open (filene, 'w') as fu:
    js.dump(usern, fu)
    print ('Hello, ' + usern)


#18. greeting a user -
filennn = 'user_name.json'
with open (filennn) as old_usr:
    usr=js.load(old_usr)
    print (f'welcome back {usr}')


#19. combining the above two programs - 
import json as js
filene = 'user_name.json'

try:
    with open (filene) as fu:
        usr=js.load(fu)
except FileNotFoundError:
        usr=input('Plz enter name: ')
        with open (filene, 'a') as ff:
            js.dump(usr, ff)
            print (f'hello, {usr}')
else:
    print ('Hello again, ' + usr)



#20. refactoring - 
def greet_user():
    '''greet user by name'''
    filene = 'user_name.json'

    try:
        with open (filene) as fu:
            usr=js.load(fu)

    except FileNotFoundError:
            usr=input('Plz enter name: ')
            with open (filene, 'a') as ff:
                js.dump(usr, ff)
                print (f'hello, {usr}')

    else:
        print ('Hello again, ' + usr)

greet_user()


#21. refactoring the above code again - 
def get_stored_user():
    '''get stored user info'''
    filene = 'user_name.json'

    try:
        with open (filene) as fu:
            usr=js.load(fu)

    except FileNotFoundError:
        return None
    
    else:
        return usr

def greet_new_usr():
    '''prompt user for new username'''
    u_name = input('enter user name: ')
    f_name = 'user_name.json'

    with open (f_name) as fn:
        js.dump(u_name, fn)
    return u_name

def greet_usr():
    '''greet user by name'''

    userna=get_stored_user()
    if userna:
        print('welcome back once again, ' + userna)
    else:
        usr= greet_new_usr()
        # usr=input('Plz enter name: ')
        # with open (filene, 'a') as ff:
        #     js.dump(usr, ff)
        #     print (f'hello, {usr}')

greet_usr()




#22. ex-11
