s=input()
v=s.replace('(','+2*(').replace('[','+3*(').replace(*'])').replace('()','1')
try:
    eval(s.replace(')','),').replace(']','],'))
    print(eval(v))
except:print(0)