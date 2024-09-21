#include <stdio.h>
int main(){int n,q;scanf("%d %d", &n, &q);for(int i=0;i<q;i++)printf("%d\n",n+i%2-1);}