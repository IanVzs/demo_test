#include<stdio.h>

struct SIMPLE
{
        int a;
        char b;
        double c;
        char string[100];
};
struct COMPLEX
{
        char string[100];
        struct SIMPLE a;
};

int main(){
        int a;
        double b;
        char c;
        printf("sizeof(int)=%lu \n",sizeof(a));
        printf("sizeof(double)=%lu \n",sizeof(b));
        struct SIMPLE simple;
        struct COMPLEX comple;
        printf("sizeof(SIMPLE)=%lu \n",sizeof(simple));
        printf("sizeof(COMPLEX)=%lu \n",sizeof(comple));
} 
