#include <stdio.h>

typedef struct Mima{
    char *mi;
    char *source;
}Mi;

//函数声明
int add_int(int, int);
float add_float(float, float);
int type_test(int t_int, char t_char, char *t_charstar, int t_intarr);
Mi getMi();
char *get_string();

int type_test(int t_int, char t_char, char *t_charstar, int t_intarr)
{
    printf("t_int %d\n", t_int);
    printf("t_char %x\n", t_char);
    printf("t_charstar %s\n", t_charstar);
    printf("t_intarr %d\n", t_intarr);
    return 0;
}

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

int main()
{
    int t_int = 1;
    char t_char;
    char t_charstar[32] = "sadhihasdha";
    int t_intarr;
    char t_charr[2][2];
    char pchar;
    int sign = 0;
    Mi result;
    char *emmm;

    sign = type_test(t_int, t_char, t_charstar, t_intarr);
    if (!sign) {
        printf("\npchar in main: %d\n", sign);
    }
    result = getMi();
    printf("\n mi: %s, source: %s\n", result.mi, result.source);
    emmm = get_string(t_char);
    printf("\nget_string: emmm: %s\n", emmm);
}


Mi getMi()
{
    Mi result;
    result.mi = "123456";
    result.source = "abcdef";
    return result;
}
char *get_string(char *hi){
    printf("---*****---hi: %s---*****---\n", hi);
    return hi;
}
