fruits = ['apple','banana','orange','grapes']

for f in fruits:
    print(f)

cart = []

while True:

    print('1. Add')
    print('2. Remove')
    print('3. Display')
    print('4. exit')

    ch = int(input('Enter action: '))

    if ch == 1:
        fruit = input('choose fruit to add: ')

        if fruit in fruits:
            cart.append(fruit)
            print(fruit,' is added')
        else:
            print(fruit,' is not available')

    elif ch == 2:
        fruit = input('choose fruit to remove from cart: ')

        if fruit in cart:
            cart.remove(fruit)
            print(fruit,' is removed')
        else:
            print(fruit,' is not there in cart')

    elif ch == 3:
        print('CART')

        for i in cart:
            print(i,end=' ')
        
        print()

    elif ch == 4:
        print('exiting')
        break
    else:
        print('choose correct option')