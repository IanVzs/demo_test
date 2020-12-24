#include	<signal.h>
#include	<unistd.h>
#include	<stdio.h>
#include	<stdlib.h>
#include	<string.h>
#include	<netinet/ip.h>
#include	<sys/socket.h>
#include	<sys/select.h>
#include	<fcntl.h>
#include	<sys/types.h>
#include	<sys/time.h>
#include	<errno.h>

#include	"sniffer.h"
#include	"tools.h"
#define ETH_P_IP 0x0800

int	exec_cmd(char *buffer, int len)
{
	if (strncmp(buffer, "quit", 4) == 0)
		return (1);
	return (0);
}

int	command_interpreter(int sd)
{
	int	len;
	char buf[512];

	len = read(0, buf, 512);
	if (len > 0)
	{
		if (exec_cmd(buf, len) == 1)
			return (1);
	}
	return (0);
}

void display_time_and_date()
{
	INITCOLOR(RED_COLOR);
	printf("[%s]", __DATE__); 
	INITCOLOR(GREEN_COLOR);
	printf("[%s]  ", __TIME__); 
	INITCOLOR(ZERO_COLOR);
}

void getting_started()
{
	CLEARSCREEN(); 
	display_time_and_date();
	printf("Getting started of Network sniffer\n\n");  
}
/* 主函数入口 */
int	main()
{
	/* 声明部分 */
	int	sd;
	int	res;
	int	saddr_size;
	int	data_size;
	struct sockaddr saddr;
	unsigned char *buffer; /* 保存数据包的数据 */
	t_sniffer sniffer; /* 保存数据包的类型和日志文件等信息 */
	fd_set fd_read;

	buffer = malloc(sizeof(unsigned char *) * 65536); 

	/* 以可写的方式在当前文件夹中创建日志文件 */
	sniffer.logfile = fopen("log.txt", "w");
	fprintf(sniffer.logfile,"***LOGFILE(%s - %s)***\n", __DATE__, __TIME__);
	if (sniffer.logfile == NULL)
	{
		perror("fopen(): ");
		return (EXIT_FAILURE);
	}

	sniffer.prot = malloc(sizeof(t_protocol *));  

	/* 创建原始套接字，ETH_P_ALL 表示侦听负载为 IP 数据报的以太网帧 */
	sd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_IP)); 
	if (sd < 0)
	{
		perror("socket(): ");
		return (EXIT_FAILURE);
	}
	getting_started();
	signal(SIGINT, &signal_white_now);
	signal(SIGQUIT, &signal_white_now);

	/* 循环侦听以太网帧，并调用 ProcessPacket 函数解析 */
	while (1)
	{
		FD_ZERO(&fd_read);
		FD_SET(0, &fd_read);
		FD_SET(sd, &fd_read);

		/* 多路复用检测可读的套接字和标准输入 */
		res = select(sd + 1, &fd_read, NULL, NULL, NULL);
		if (res < 0)
			{
				close(sd);
				if (errno != EINTR)
				perror("select() ");
				return (EXIT_FAILURE);
			}
		else
			{
				/* 如果是标准输入可读，进入命令行处理程序 command_interpreter，暂时只支持 'quit' 命令 */
				if (FD_ISSET(0, &fd_read)) 
				{
					if (command_interpreter(sd) == 1)
					break;
				}

				/* 如果是套接字可读，则读取以太网数据帧的内容，并调用 ProcessPacket 函数解析出数据包的类型 */
				else if (FD_ISSET(sd, &fd_read))
					{
						/* 读取以太网数据帧的内容 */
						saddr_size = sizeof(saddr);
						data_size = recvfrom(sd, buffer, 65536, 0, &saddr,(socklen_t*)&saddr_size); /* 读取以太网数据帧的内容 */
						if (data_size <= 0)
							{
								close(sd);
								perror("recvfrom(): ");
								return (EXIT_FAILURE);
							}

						ProcessPacket(buffer, data_size, &sniffer); /* 调用 ProcessPacket 函数解析出数据包的类型 */
					}
			}
	}
	
	close(sd);
	return (EXIT_SUCCESS);
}

void ProcessPacket(unsigned char* buffer, int size, t_sniffer *sniffer)
{
	buffer = buffer + 6 + 6 + 2; /* 根据以太网帧结构，前 6B 是目的 MAC 地址，接下来的是源 MAC 地址，接下来 2B 是帧长度，其余的是负载（上层的 IP 数据报） */
	struct iphdr *iph = (struct iphdr*)buffer;
	++sniffer->prot->total; /* 数据包总数加 1 */

	/* 根据 TCP/IP 协议规定的 IP 数据报头部的 protocol 字段的值，判断上层的数据包类型 */
	switch (iph->protocol)
		{
			/* 1 表示 icmp 协议 */
			case 1: 
				++sniffer->prot->icmp;
				print_icmp_packet(buffer, size, sniffer);
				break;
				
			/* 2 表示 igmp 协议 */
			case 2:
				++sniffer->prot->igmp;
				break;
				
			/* 6 表示 tcp 协议 */
			case 6:
				++sniffer->prot->tcp;
				print_tcp_packet(buffer , size, sniffer);
				break;
				
			/* 17 表示 udp 协议 */
			case 17:
				++sniffer->prot->udp;
				print_udp_packet(buffer , size, sniffer);
				break;
      
			default:
				++sniffer->prot->others;
				break;
		}

	display_time_and_date(); /* 显示时间 */

	/* 打印 sniffer 中的信息 */
	printf("TCP : %d   UDP : %d   ICMP : %d   IGMP : %d   Others : %d Total : %d\n",
	 sniffer->prot->tcp, sniffer->prot->udp,
	 sniffer->prot->icmp, sniffer->prot->igmp,
	 sniffer->prot->others, sniffer->prot->total);
}