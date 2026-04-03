
available_toppings = ['Cheese', 'Tomato', 'mushrooms', 'pepperoni', 'pineapple', 'Cheken']
requested_toppings = ['Tomato', 'Meet', 'Cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'We add topping {requested_topping}')
    else:
        print(f'Sorry, We dont have {requested_topping}')

