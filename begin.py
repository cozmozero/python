def get_choices():
    player_choice=input('enter your choice (rock, paper, scissors): ')
    comp_choice='paper'

    choices={'player':player_choice, 'comp':comp_choice}

    return choices

response=get_choices()
print(response)



