for _ in[0]*int(input()):
    input()
    s=input()
    if len(s)in[1,3]:
        print(-1)
    elif len(s)==2:
        if s in['00','11']:
            print(1)
        else:
            print(0)
    else:
        # check ans==0
        s0,e0,s1,e1=s.find('0'),s.rfind('0'),s.find('1'),s.rfind('1')
        if min(s0,e0,s1,e1)<0:
            print(2)
        elif e0-s0==e1-s1:
            print(0)
        else:
            # change to 0
            dps0=[min(s0,i)for i in range(len(s))]
            dpe0=[max(e0,i)for i in range(len(s))]
            dps1=[s1 if s1!=i else s.find('1',i+1) for i in range(len(s))]
            dpe1=[e1 if e1!=i else s.rfind('1',0,i) for i in range(len(s))]
            for ss0,ee0,ss1,ee1 in zip(dps0,dpe0,dps1,dpe1):
                if ee0-ss0==ee1-ss1:
                    print(1)
                    break
            else:
                # change to 1
                dps0=[s0 if s0!=i else s.find('0',i+1) for i in range(len(s))]
                dpe0=[e0 if e0!=i else s.rfind('0',0,i) for i in range(len(s))]
                dps1=[min(s1,i)for i in range(len(s))]
                dpe1=[max(e1,i)for i in range(len(s))]
                for ss0,ee0,ss1,ee1 in zip(dps0,dpe0,dps1,dpe1):
                    if ee0-ss0==ee1-ss1:
                        print(1)
                        break
                else:
                    print(2)