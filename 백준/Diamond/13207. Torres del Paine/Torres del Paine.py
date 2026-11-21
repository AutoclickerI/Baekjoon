from decimal import*
getcontext().prec=199
V='=lambda f'
exec(f'''x_lb,y_lb,x_rt,y_rt=map(D:=Decimal,input().split());x1,y1,x2,y2,x3,y3=map(D,input().split());Z=D('1E-100');x2+=Z;y2+=Z;x3+=Z*2;y3+=Z*2
ccw{V[:-1]}*l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(len(l)))/2
AB{V}:(y2-y1)/(x2-x1)*(f-x1)+y1
AB_1{V}:(x2-x1)/(y2-y1)*(f-y1)+x1
BC{V}:(y3-y2)/(x3-x2)*(f-x2)+y2
BC_1{V}:(x3-x2)/(y3-y2)*(f-y2)+x2
CA{V}:(y3-y1)/(x3-x1)*(f-x1)+y1
CA_1{V}:(x3-x1)/(y3-y1)*(f-y1)+x1
cl{V},F,p=x_lb,n=0:(3,F(y_lb),y_lb)if f(p)<y_lb else(n,p,f(p))if y_lb<=f(p)<=y_rt else(1,F(y_rt),y_rt)
ara=(x_rt-x_lb)*(y_rt-y_lb)
def A(l,n):
 p,q=sorted(l);p3,p1,p2=p;q3,q1,q2=q;a=(ccw([q1,q2],[x_rt,y_lb],[x_rt,y_rt],[p1,p2])if q3==3 else ccw([q1,q2],[x_rt,y_rt],[x_lb,y_rt],[p1,p2]))if q3-p3==2 else(ccw([q1,q2],[x_lb,y_rt],[p1,p2])if q3==1 else ccw([q1,q2],[x_rt,y_rt],[p1,p2])if q3==2 else ccw([q1,q2],[x_rt,y_lb],[p1,p2])if p3==2 else ccw([q1,q2],[x_lb,y_lb],[p1,p2]))
 return ara-abs(a)if a*ccw([q1,q2],[[x1,y1],[x2,y2],[x3,y3]][n],[p1,p2])>0 else abs(a)
a=A([cl(AB,AB_1),cl(AB,AB_1,x_rt,2)],2)+A([cl(BC,BC_1),cl(BC,BC_1,x_rt,2)],0)+A([cl(CA,CA_1),cl(CA,CA_1,x_rt,2)],1)+abs(ccw([x1,y1],[x2,y2],[x3,y3]))-ara
print(f'{{a if ccw([x1,y1],[x2,y2],[x3,y3])>0 else ara-a:.15f}}');'''*int(input()))