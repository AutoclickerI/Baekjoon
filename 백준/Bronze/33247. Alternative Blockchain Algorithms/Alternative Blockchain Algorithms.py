g=c=0
for i in[*open(0)][1:]:i,p,m=map(int,i.split());c+=m;c>-1<g==p or exit(print(['INVALID','NO_MONEY'][c<0]));g=i
print(c)