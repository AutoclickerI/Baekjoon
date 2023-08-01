A=T=J=Q=K=10
def checkmin(i):
    tmp=[*dl]
    if i>=len(s):
        return max(tmp)
    while tmp and max(tmp)>21:
        tmp.pop()
    if not tmp:
        return -1
    while max(tmp)<17:
        tmp=[k+j for k in tmp for j in([eval(s[i])]if s[i]!='A'else[1,11])if k+j<22]
        while tmp and max(tmp)>21:
            tmp.pop()
        if not tmp:
            return -1
        i+=1
    return max(tmp)
                                           
while(s:=input())[1]!='O':
    try:
        al=[]
        if s[0]!='A':
            al+=eval(s[0]),
        else:
            al+=1,11
        al=[i+j for i in al for j in[[eval(s[2])],[1,11]][s[2]=='A']if i+j<22]
        dl=[]
        if s[1]!='A':
            dl+=eval(s[1]),
        else:
            dl+=1,11
        dl=[i+j for i in dl for j in[[eval(s[3])],[1,11]][s[3]=='A']if i+j<22]
        i=4
        while i<len(s) and al:
            if checkmin(i)<=max(al):
                raise
            al=[k+j for k in al for j in[[eval(s[i])],[1,11]][s[i]=='A']if k+j<22]
            i+=1
        assert max(dl)>max(al+[-1])
        print('No')
    except:
        print('Yes')