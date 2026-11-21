def f(n):
    return f'''{n} bottle{'s'*(n>1)} of beer on the wall, {n} bottle{'s'*(n>1)} of beer.
Take one down and pass it around, {f'{n-1} bottle{'s'*(n>2)}'if n>1 else 'no more bottles'} of beer on the wall.
'''
K=n=int(input())
while n:
    print(f(n))
    n-=1
print(f'''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {K} bottle{'s'*(K>1)} of beer on the wall.''')