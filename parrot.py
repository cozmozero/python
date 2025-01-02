# prompt="\n Enter 'quit' to end the program" 
# prompt+='\n Tell me something, and i will repeat it back to you: '

# active=True
# message=''
# lists=[]

# while message!='quit':
#     message=input(prompt)
    
#     if message!='quit':
#         active=False

#     lists.append(message)
# print(lists)



# 2. V2
prompt="\n Enter 'quit' to end the program" 
prompt+='\n Tell me something, and i will repeat it back to you: '

active=True
lists=[]

while active:
    message=input(prompt)
    
    if message=='quit':
        active=False

    else:
        print(message)

    lists.append(message)
print(lists)


# #3. v3
# prompt="\n Enter 'quit' to end the program" 
# prompt+='\n Tell me something, and i will repeat it back to you: '

# active=True
# lists=[]

# while active:
#     message=input(prompt)
    
#     if message=='quit':
#         active=False

#     elif message==101:
#         active=False

#     else:
#         print(message)

#     lists.append(message)
# print(lists)