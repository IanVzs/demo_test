#include<stdio.h>
#include<wchar.h>
#include<locale.h>
 
wchar_t wc;
int main()
{
    setlocale(LC_ALL,"");//设置为本地区域
    while (1) {
        wc = getwchar();
        if(wc != L'\n')
            wprintf(L"%c==0X%4X\n",wc,wc);
    }
}
