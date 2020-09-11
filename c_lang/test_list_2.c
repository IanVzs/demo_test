#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define byte unsigned char

void letMeSee(char *data_char, byte* data_crlist);
void letMeSeeAgin(char *data_char, byte* data_crlist);
int print_list(char *name, byte *d, int len);
int str2ulist(char *str, byte *ulist, int *n);
int ulist2str(char *str, byte *ulist, int len);

int main()
{
        //原文
        char data_char[16] = "e6b58be8af";
        byte data_crlist[16] = "测试345";
        // letMeSee(data_char, data_crlist);
        letMeSeeAgin(data_char, data_crlist);
        return 1;
}

void letMeSee(char *data_char, byte* data_crlist)
{
    int conter = 0;
    printf("data_char: %s\n", data_char);
    print_list("data_crlist: ", data_crlist, 5);

    ulist2str(data_char, data_crlist, 5);
    printf("\nafter ulist2str data_char: %s\n", data_char);
    str2ulist(data_char, data_crlist, &conter);
    print_list("after str2ulist data_crlist: ", data_crlist, 5);
}
void letMeSeeAgin(char *data_char, byte* data_crlist)
{
    int conter = 0;

    str2ulist(data_char, data_crlist, &conter);
    printf("data_char: %s\n", data_char);
    print_list("data_crlist: ", data_crlist, 5);
    printf("conter: %d\n", conter);
    print_list("after str2ulist data_crlist: ", data_crlist, conter);
    ulist2str(data_char, data_crlist, 5);
    printf("\nafter ulist2str data_char: %s\n", data_char);
}

int print_list(char *name, byte *d, int len)
{
    int i;
    printf("%s[%d]=", name, len);
    for (i = 0; i < len; i++)
        printf("%02x", d[i]);
    printf("\n");
    return 0;
}

int str2ulist(char *str, byte *ulist, int *n)
{
    /*******unsigned char列表转换为字符串*********/
    int i = strlen(str), j = 0, conter = 0;
    char c[2];
    unsigned int bytes[2];
    printf("111, i: %d, j: %d\n\n", i, j);
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
    *n = conter;
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
