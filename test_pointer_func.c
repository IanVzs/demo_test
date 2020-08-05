#include<stdio.h>
#include<stdlib.h>
/*  int * p "int *" 用于声明这是个指针类型，且指过去的值是个int类型
  而非这是个int型的指针。。。。。准确说是指向int型的指针。 */

int* fun(int* x)    //传入指针  
{
    int* tmp = x;     //指针tmp指向x
    return tmp;       //返回tmp指向的地址
}

int* wildfun(int* x)    //传入指针  
{
    int* tmp = x;     //指针tmp指向x
    int  var = 20;
    tmp = &var;     //指针tmp指向1
    return tmp;       //返回tmp指向的地址
}
static int intcms(void *para);
void no_main(void);

int main()
{
    int b = 2;
    int* p = &b;   //p指向b的地址
    printf("fun: %d\n", *fun(p));//输出p指向的地址的值
    printf("----------\n");
    printf("wildfun: %d\n", *wildfun(p));//输出p指向的地址的值
    printf("%p\n", p);
    printf("%d\n", *fun(p));//输出p指向的地址的值
    printf("%p\n", fun(p));
    
    no_main();
    return 0;
}


/**
 *
 *
 * >>>
 * fun: 2
 * ----------
 * wildfun: 20
 * >>>
 * なに？！
 * **/
/* 结构体指针也来个吧 */
typedef struct{
    int a;
    int b;
} date;

static int intcms(void *para){
    int a = ((date *)para)->a;
    printf("IN intcms a is %d\n",a);
}
 
void no_main(){
    date *dates = (date *)malloc(sizeof(date));
    dates->a = 9;
    dates->b = 2;
    intcms(dates);
    free(dates);
}
