#include<stdio.h>

int* fun(int* x)    //传入指针  
{
    int* tmp = x;     //指针tmp指向x
    return tmp;       //返回tmp指向的地址
}

int main()
{
    int b = 2;
    int* p = &b;   //p指向b的地址
    printf("%d", *fun(p));//输出p指向的地址的值
    return 0;
}
