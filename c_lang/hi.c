#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int lengthOfLongestSubstring(char *s)
{
    int offset[128] = {1,2,3};
    int max_len = 0;
    int len = 0;
    int index = 0;
    int i;
    int a;
    for( i=0; i<=128 ; i++){
        printf("%d", offset[i]);
    }
    printf("\n0xff: %d\n", 0xff);
    a = sizeof(offset);
    printf("\n sizeof: %d\n", a);
    memset(offset, 0xff, sizeof(offset));
    for( i=1; i<=10 ; i++){
        printf("%d", offset[i]);
    }
    while (*s != '\0') {
        printf("index: %d\n", index);
        printf("s: %s\n", s);
        printf("*s: %d\n", *s);
        printf("offset[*s]: %d\n", offset[*s]);
        if (offset[*s] == -1) {
            len++;
        } else {
            if (index - offset[*s] > len) {
                len++;
            } else {
            len = index - offset[*s];
            }
        }
        if (len > max_len) {
            max_len = len;
        }
        offset[*s++] = index++;
    }
    if (*s == 0){
        printf("*s is int 0!");
    } else if (*s == '\n') {
        printf("just str 0");
    }
    printf("out *s: %d\n", *s);

    return max_len;
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "Usage: ./test string\n");
        exit(-1);
    }

    printf("%d\n", lengthOfLongestSubstring(argv[1]));
    return 0;
}

