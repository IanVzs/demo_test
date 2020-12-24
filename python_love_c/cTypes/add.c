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
// 配合unsigned char 和 char 互相转化, 可以完成更多的字符回传
// 这方法仅"能用"级别
int ulist2str(char *str, byte *ulist, int len);
int str2ulist(char *str, byte *ulist);

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

/*********转换长度差为2倍************/
int str2ulist(char *str, byte *ulist)
{
    /*******unsigned char列表转换为字符串*********/
    int i = strlen(str), j = 0, conter = 0;
    char c[2];
    unsigned int bytes[2];
    for (j = 0; j < i; j += 2)
    {
        if(0 == j%2)
        {
            c[0] = str[j];
            c[1] = str[j + 1];
            sscanf(c, "%02x", &bytes[0]);
            ulist[conter] = bytes[0];
            conter++;
        }
    }
    return 0;
}

int ulist2str(char *str, byte *ulist, int len)
{
    /*******字符串转换为unsigned char列表*********/
    int i;
    for (i = 0; i < len; i++)
    {
        sprintf(str + i*2, "%02x", ulist[i]);
    }
    return 0;
}
