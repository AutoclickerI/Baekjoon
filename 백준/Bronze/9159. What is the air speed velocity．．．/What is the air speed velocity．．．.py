*dist,=map(int,input().split())
time=[0,0]
v=[],[]
for _ in range(20):
    s,t=input().lower().split()
    t=float(t)
    time[s=='e']+=t
    v[s=='e'].append(dist[s=='e']/t)
print('Method 1')
print(f'African: {dist[0] * 10 / time[0]:.2f} furlongs per hour')
print(f'European: {dist[1] * 10 / time[1]:.2f} furlongs per hour')   

print('Method 2')
print(f'African: {sum(v[0]) / 10:.2f} furlongs per hour')
print(f'European: {sum(v[1]) / 10:.2f} furlongs per hour')  