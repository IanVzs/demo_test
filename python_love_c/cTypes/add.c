#include <stdio.h>


//函数声明
int add_int(int, int);
float add_float(float, float);

//函数实现
int add_int(int num1, int num2){
    int res_int;
    for(int loop_num = 10000000; loop_num>0; loop_num--){
        res_int = num1 + num2;
    }
    return res_int;
}
float add_float(float num1, float num2){
    float res_int;
    int loop_num = 10000000;
    for(int loop_num = 10000000; loop_num>0; loop_num--){
        res_int = num1 + num2;
    }
    return res_int;
}
