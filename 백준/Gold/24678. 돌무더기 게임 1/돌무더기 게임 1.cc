#include <stdio.h>
int main(){
	long a,b,c,n;
    scanf("%ld",&n);
	while(n--){
		scanf("%ld %ld %ld",&a,&b,&c);
		a=a%2+b%2+c%2;
		if(a<2)printf("R\n");
		else printf("B\n");
	}
}