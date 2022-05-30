from socket import has_dualstack_ipv6
from diagrams import Cluster, Diagram
from diagrams.aws.database import RDS
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS


with Diagram("axie diagrams", show=False):
    source = EKS("多开管理器")
    source2 = EKS("多开管理器")

    with Cluster("Axie 事件处理"):
        with Cluster("多开管理器"):
            accounts = [ECS("账号1"),
                       ECS("账号2"),
                       ECS("账号3")]

        with Cluster("通过游戏API获取当前游戏进行状态和数据"):
            state = SQS("游戏状态")
            data = RDS("游戏数据")
            info = [state, data]


        with Cluster("多进程YOLO服务 根据规则和AI\n获得点击位置"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]

    click_operate = Redshift("执行点击操作")

    source >> accounts >> state
    accounts >> data
    
    data >> handlers
    state >> handlers

    handlers >> click_operate
    click_operate >> source2
