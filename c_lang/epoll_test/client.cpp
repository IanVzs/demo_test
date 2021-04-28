#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <string>
#include <iostream>

using namespace std;

void err_exit(const char *s){
    printf("error: %s\n",s);
    exit(0);
}

int create_socket(const char *ip, const int port_number)
{
    struct sockaddr_in server_addr = {0};
    /* 设置ipv4模式 */
    server_addr.sin_family = AF_INET;           /* ipv4 */
    /* 设置端口号 */
    server_addr.sin_port = htons(port_number);
    /* 设置主机地址 */
    if(inet_pton(PF_INET, ip, &server_addr.sin_addr) == -1){
        err_exit("inet_pton");
    }

    /* 建立socket */
    int sockfd = socket(PF_INET, SOCK_STREAM, 0);
    if(sockfd == -1){
        err_exit("socket");
    }

    if(connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1){
        err_exit("connect");
    }

    return sockfd;
}

int main(int argc, const char *argv[]){
    if(argc < 3){
        printf("usage:%s ip port\n", argv[0]);
        exit(0);
    }
    /* 获取服务器参数 */
    const char * ip = argv[1];
    const int port = atoi(argv[2]);
    //创建套接字
    int sock = create_socket(ip, port);
    //向服务器（特定的IP和端口）发起请求
    
    while(1){
        string buff;
        getline(cin, buff);
        if(buff == "exit") break;
        write(sock, buff.c_str(), buff.size());
        char end = '\n';
        write(sock, &end, 1);
    }
    close(sock);
    return 0;
}