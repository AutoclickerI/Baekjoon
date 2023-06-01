#include <stdio.h>
int main(){
	long a,b,c,n,tmp,w;
    scanf("%ld",&n);
	while(n--){
		scanf("%ld %ld %ld",&a,&b,&c);
		if(a>b){
			tmp=a,a=b,b=tmp;
		}
		if(b>c){
			tmp=b,b=c,c=tmp;
		}
		if(a>b){
			tmp=a,a=b,b=tmp;
		}
		if(c<a+b-2)w=c;
		else w=a+b-2;
		if((a==0)&&(b%2)||(a==1)&&(b==c)&&(b%2)||(a>1)&&(1-a%2)&&(1-b%2)&&(1-w%2)||(a>1)&&((a+b+w)%4==3))printf("B\n");
		else printf("R\n");
	}
}