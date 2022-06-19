number = int(input('Which number do you want to check? '))
is_even = number % 2 == 0

if is_even:
    print('Your number is even')
else:
    print('Your number is ODD')