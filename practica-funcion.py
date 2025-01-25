price_coffe = [('capuchino',1.5),('Expresso',2.5),('Moka',1.9)]

def most_expensive_coffe(price_list):
    mayor_price = 0
    most_expensive_coffe = ''

    for coffe,price in price_list:
        if  price > mayor_price:
            mayor_price = price
            most_expensive_coffe = coffe
        else:
            pass

    return (most_expensive_coffe,mayor_price)
coffe, price = most_expensive_coffe(price_coffe)

print(f'The most expensive coffe is the {coffe} with a price of ${price}')