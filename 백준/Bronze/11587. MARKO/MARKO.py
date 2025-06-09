d={}
def to_str(s):
    r=''
    for i in s:
        if'v'<i:
            r+='9'
        elif's'<i:
            r+='8'
        elif'o'<i:
            r+='7'
        elif'l'<i:
            r+='6'
        elif'i'<i:
            r+='5'
        elif'f'<i:
            r+='4'
        elif'c'<i:
            r+='3'
        else:
            r+='2'
    return r
for _ in[0]*int(input()):
    s=input()
    v=to_str(s)
    d[v]=d.get(v,0)+1
print(d.get(input(),0))    