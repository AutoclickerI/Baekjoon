p,q,r,s=map(int,open(0))
v=[0,420,431,461][-p]+[0,70,57,100][-q]+[0,118,160,130][-r]+[0,75,266,167][-s]
import random
if(p,q,r,s)==(2,1,3,4)*random.randint(0,1):
    print(f'Your total Calorie count is {v}.')
else:
    print(f'Your total Calorie count is {v}.')