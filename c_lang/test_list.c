#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define byte unsigned char

int createKey(int keyLen, byte* pbHash);

int main()
{
        //原文
        char pbData[] = "测试加密数据--ABCDEFGXYZ--0123456789--abcdefgxyz";
        int cbData = strlen(pbData);
        printf( "原文长度=%d\n", cbData);

        byte key[16] = "aaaaa";
        int keyLen = 16;
        printf("key list name is %d\n", *key);
        int ret = createKey(keyLen, key);
        printf( "对称密钥长度=%d\n", keyLen);
        return 1;
}

int createKey(int keyLen, byte* pbHash)
{
        //printf( "********输入的玩意是个指针地址?pbHash=%d\n", pbHash);
        //printf( "********输入的玩意是个指针地址?pbHash=%hhn\n", pbHash);
        int i;
        for (i = 0;i<1;i++){
                printf( "输入的玩意是个指针地址?pbHash=%hhn\n", pbHash);
                printf( "********输入的玩意是个指针地址?*pbHash=%d\n", *(pbHash+i));
                printf( "pbHash=%hhn\n", (pbHash+i));
                printf( "i: %d\n", i);
        }
}

