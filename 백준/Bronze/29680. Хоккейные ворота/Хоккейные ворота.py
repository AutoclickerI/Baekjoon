H,W,w1,w2=map(eval,input().split())
print(w1*W+(w1+w2)*H+((w2-w1)**2+H*H)**.5*W)