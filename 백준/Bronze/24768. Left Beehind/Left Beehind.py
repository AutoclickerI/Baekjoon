while(s:=input())!='0 0':
    x,y=map(int,s.split())
    if x+y==13:print('Never speak again.')
    elif x>y:print('To the convention.')
    elif x<y:print('Left beehind.')
    else:print('Undecided.')