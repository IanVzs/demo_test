#include <stdio.h>

void main()
{
    char a = 255;
    char b = 127;
    unsigned char c = 255;
    
    printf("a: %d\n", a);
    printf("b: %x\n", b);
    printf("a 16: %x\n", a&0xff);
    printf("c 16: %x\n", c);
}
