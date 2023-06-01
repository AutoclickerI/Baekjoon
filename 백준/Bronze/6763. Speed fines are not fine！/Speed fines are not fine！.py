n=-int(input())+int(input())
f='10'if n<21 else'27'if n<31 else'50'
print('Congratulations, you are within the speed limit!'if n<1 else f'You are speeding and your fine is ${f}0.')