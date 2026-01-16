import sys
import math
input=sys.stdin.readline

class LR:
    def __init__(self,init_lr,lr_lambda):
        self.lr=init_lr
        self.lr_lambda=lr_lambda
    def step(self):
        self.lr*=self.lr_lambda
    def __mul__(self,b):
        return self.lr*b

def sigmoid(z):
    if 0<z:
        return 1/(1+math.exp(-z))
    else:
        return math.exp(z)/(1+math.exp(z))
while k:=int(input()):
    obs=[[*map(int,input().split())]for _ in[0]*k]
    a=b=0
    lr=LR(.1,1)
    for _ in range(200000):
        ga=gb=0
        for x,w in obs:
            z=a+b*x
            p=sigmoid(z)

            diff=w-p
            ga+=diff
            gb+=diff*x

        ga/=k
        gb/=k

        a+=lr*ga
        b+=lr*gb/100
        lr.step()

    print(f'{a:.4f} {b:.4f}')