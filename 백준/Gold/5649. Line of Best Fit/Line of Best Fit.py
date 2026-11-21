from statistics import*
print('%.03f %.03f'%linear_regression(*zip(*[map(int,l.split())for l in open(0)][1:])))