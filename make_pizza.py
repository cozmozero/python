def make_pizza1(size='M', *toppings):
    print(f'\nMaking a {size} Pizza with: ')
    for topping in toppings:
        print(f'--- {topping.title()}')