#include"grader.h"
#include"memory.h"
#define G(i,a)for(i=a;i<50;i++)
void play(){int i,j,c[50];G(i,0)c[i]=faceup(i+1);G(i,0)G(j,i+1)if(c[i]==c[j]){faceup(i+1);faceup(j+1);}}