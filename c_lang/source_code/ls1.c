/*************************************************************************
    > File Name: ls1.c
    > Author: 
    > Mail: 
 ************************************************************************/

#include<stdio.h>
#include<sys/types.h>
#include<dirent.h>

void do_ls(char[]);

int main(int argc, char *argv[])
{
    if(argc==1)
    	do_ls(".");
    else
	    while(--argc){
	        printf("%s:\n",*++argv);
	        do_ls(*argv);
	    }
    
    return 0;
}

void do_ls(char dirname[])
{
    DIR *dir_ptr;
    struct dirent *direntp;

    if((dir_ptr=opendir(dirname))==NULL)
        fprintf(stderr,"ls1:cannot open %s\n",dirname);
    else
    {
        while((direntp=readdir(dir_ptr))!=NULL && strcmp(direntp->d_name, ".") != 0 \
		&& strcmp(direntp->d_name, "..") != 0)
            printf("%s\n",direntp->d_name);
        closedir(dir_ptr);
    }
}
