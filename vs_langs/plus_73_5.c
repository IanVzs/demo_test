#include <math.h>
#include <sys/time.h>
#include <stdio.h>

//double t_diff(const struct timeval *start, const struct timeval *end)
void t_diff(const struct timeval *start, const struct timeval *end)
{
        time_t s_go;
        double t_s_so;
        double start_time, end_time;
        s_go = start->tv_sec * 1000000;
        s_go = s_go + start->tv_usec;
        t_s_so = (double)s_go/1000000;
        start_time = t_s_so;
        
        s_go = end->tv_sec * 1000000;
        s_go = s_go + end->tv_usec;
        t_s_so = (double)s_go/1000000;
        end_time = t_s_so;
        //printf("start_time: %lf, end_time: %lf\n", start_time, end_time);
        printf("all cost s: %lf,   u: <-\n", end_time-start_time);
}

void go(int *a, int *b){
        int i, v=0, I;
        //I = pow(73, 5);
        I = pow(73, 5);
        for (i = 0; i < I; i++){
                v++;
        }
        *a = I;
        *b = v;
}

int main(){
        int a, b;
        //double time_cost;
        struct timeval start, end;
        printf("*********************C********************\n");
        gettimeofday(&start, NULL);
        go(&a, &b);
        gettimeofday(&end, NULL);
        printf("loop result: %d\n", b);
        printf("pow result: %d\n", a);
        //time_cost = t_diff(&end, &start);
        t_diff(&start, &end);
}
