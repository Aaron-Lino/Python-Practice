from random import shuffle

#initial list
sticks = ['-','--','---','----']

#mix sticks
def mix(list):
    shuffle(list)
    return list

#ask for a try
def try_your_luck():
    attempt = ''

    while attempt not in ['1','2','3','4']:
        attempt = input("Choose a number from 1 to 4: ")

    return int(attempt)

#attempt test
def check_attempt(list,attempt):
    if list[attempt -1] == '-':
        print('you loose')
    else:
        print('you win... for now')

    print(f'the stick you got is {list[attempt -1]}')

sticks_mixed = mix(sticks)
seleccion = try_your_luck()

check_attempt(sticks_mixed, seleccion)