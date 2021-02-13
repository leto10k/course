def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price*discount/100
    print(price_with_discount)

discounted(100,5)

def get_summ(one, two, delimiter = '&'):
    return(f'{one}{delimiter}{two}')

text = get_summ('Learn','python')
print(text.upper())

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

a = format_price(56.24)
print(a)
print('Я изменил')