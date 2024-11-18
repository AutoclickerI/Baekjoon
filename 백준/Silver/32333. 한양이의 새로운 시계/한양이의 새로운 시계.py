l=sorted((i*60+j,k)for i,j,k in[map(int,i.split())for i in[*open(0)][1:]])

t=0

def print_animal(s,e):
    db=['rat', 'cow', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'chicken', 'dog', 'pig', 'lion', 'giraffe', 'cat']
    start=s//96
    end=e//96
    print(*db[start:end+1])

f=0
c=0
for s,d in l:
    if f:
        c+=1
    elif 1439<max(s,t)+d:
        f=1
        c+=1
    else:
        t=max(s,t)
        print_animal(t,t+d)
        print('%02d:%02d %02d:%02d'%(t//60,t%60,(t+d)//60,(t+d)%60))
        t+=d
if f:
    print(c)