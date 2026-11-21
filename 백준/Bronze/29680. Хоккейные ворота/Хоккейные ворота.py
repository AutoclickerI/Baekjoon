H,W,x,y=map(eval,input().split())
print(x*W+(x+y)*H+((y-x)**2+H*H)**.5*W)