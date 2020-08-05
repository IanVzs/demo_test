#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pcre.h>
#include <wchar.h>

#define OVECCOUNT 30    /* should be a multiple of 3 */
#define EBUFLEN 128            
#define BUFLEN 1024

/*  gcc报错需要链接库pcre:    gcc regular.c -l pcre   */

int main()
{
      pcre *reCM, *reUN, *reTC, *reCDMA; // *reWChar; 
      const char *error;
      int erroffset;
      int ovector[OVECCOUNT];
      int rcCM, rcUN, rcTC, rcCDMA, i; 
/*        
      常用号段前三位
      中国移动CM：134.135.136.137.138.139.150.151.152.157.158.159.187.188 ,147(数据卡)
      中国联通UN：130.131.132.155.156.185.186 
      中国电信TC：133.153.180.189 
      CDMA ：133,153
*/
      char src[22];  
      char pattern_CM[] = "^1(3[4-9]|5[012789]|8[78])\\d{8}$";      //正则表达式
      char pattern_UN[] = "^1(3[0-2]|5[56]|8[56])\\d{8}$";
      char pattern_TC[] = "^18[09]\\d{8}$";
      char pattern_CDMA[] = "^1[35]3\\d{8}$";

      // wchar_t ch[] = L"C语言中文网";
      // wchar_t ch_re[] = L"C语言中文网";
      
      printf("Please input your telephone number \n");
      scanf("%s", src);
      printf("String : %s\n", src);
      printf("Pattern_CM: \"%s\"\n", pattern_CM);
      printf("Pattern_UN: \"%s\"\n", pattern_UN);
      printf("Pattern_TC: \"%s\"\n", pattern_TC);
      printf("Pattern_CDMA: \"%s\"\n", pattern_CDMA);
       
      reCM = pcre_compile(pattern_CM, 0, &error, &erroffset, NULL);  //将正则表达式编译成pcre内部表示结构
      reUN = pcre_compile(pattern_UN, 0, &error, &erroffset, NULL);
      reTC = pcre_compile(pattern_TC, 0, &error, &erroffset, NULL);
      reCDMA = pcre_compile(pattern_CDMA, 0, &error, &erroffset, NULL);

      // reWChar = pcre_compile(ch_re, 0, &error, &erroffset, NULL);
        
      if (reCM==NULL && reUN==NULL && reTC==NULL && reCDMA==NULL) {
       printf("PCRE compilation telephone failed at offset %d: %s\n", erroffset,  error);
        return 1;        
      }

      rcCM = pcre_exec(reCM, NULL, src, strlen(src), 0, 0, ovector, OVECCOUNT);  //匹配pcre编译好的模式，成功返回正数，失败返回负数
      rcUN = pcre_exec(reUN, NULL, src, strlen(src), 0, 0, ovector, OVECCOUNT);
      rcTC = pcre_exec(reTC, NULL, src, strlen(src), 0, 0, ovector, OVECCOUNT);
      rcCDMA = pcre_exec(reCDMA, NULL, src, strlen(src), 0, 0, ovector, OVECCOUNT);

      // rcWChar = pcre_exec(reWChar, NULL, ch, strlen(ch), 0, 0, ovector, OVECCOUNT);
      // printf("rcWChar: %d", rcWChar);
       
      if (rcCM<0 && rcUN<0 && rcTC<0 && rcCDMA<0) {      //若没匹配返回错误信息
       if (rcCM==PCRE_ERROR_NOMATCH && rcUN==PCRE_ERROR_NOMATCH &&
       rcTC==PCRE_ERROR_NOMATCH && rcTC==PCRE_ERROR_NOMATCH) {
       printf("Sorry, no match ...\n");        
        }
        else {
         printf("Matching error %d\n", rcCM);
         printf("Matching error %d\n", rcUN);
         printf("Matching error %d\n", rcTC);
         printf("Matching error %d\n", rcCDMA);
        }   
        
        free(reCM);
        free(reUN);
        free(reTC);
        free(reCDMA);
        // free(reWChar);
          
        return 1;
      }

      printf("\nOK, has matched ...\n\n");  //匹配成功把对应的正则表达式和号码打印出来

      if (rcCM > 0) {
       printf("Pattern_CM: \"%s\"\n", pattern_CM);
        printf("String : %s\n", src);
      }

      if (rcUN > 0) {
       printf("Pattern_UN: \"%s\"\n", pattern_UN);  
        printf("String : %s\n", src);    
      }

      if (rcTC > 0) {
       printf("Pattern_TC: \"%s\"\n", pattern_TC);
        printf("String : %s\n", src);
      }
       
      if (rcCDMA > 0) {
       printf("Pattern_CDMA: \"%s\"\n", pattern_CDMA);   
        printf("String : %s\n", src);
      }

      free(reCM);        //释放内存
      free(reUN);
      free(reTC);
      free(reCDMA);
        
      return 0;
}
