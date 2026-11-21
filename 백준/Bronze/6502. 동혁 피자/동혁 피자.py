for i in[*open(t:=0)][:-1]:
    t+=1
    r,w,h=map(int,i.split())
    print('Pizza',t,['fits','does not fit'][w*w+h*h>4*r*r],'on the table.')