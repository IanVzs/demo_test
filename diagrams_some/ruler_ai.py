from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.gcp.database import BigTable
from diagrams.aws.network import ELB
from diagrams.aws.integration import SQS
from diagrams.gcp.analytics import Dataflow

with Diagram("Ruler AI", show=True):
    lb = ELB("lb")

    game_server = ECS("Game Server")
    ai_server = ECS("AI Server")
    commands = BigTable("Commands")

    with Cluster("DB Cluster"):
        redis = RDS("NPC State")

    with Cluster("Backend Server"):
        with Cluster("Writer"):
            state_flow = Dataflow("Collector")
            game_server >> lb >> state_flow >> redis
        
        with Cluster("Reader"):
            planner = Dataflow("Planner")
            redis >> planner
            ai_server >> planner >> ai_server
            planner >> commands
            # game_server >> planner >> game_server

with Diagram("Ruler AI Proactive", show=True):
    lb = ELB("lb")

    game_server = ECS("Game Server")
    game_server_cp = ECS("Game Server")
    ai_server = ECS("AI Server")
    
    commands = BigTable("Commands")
    executor = SQS("Executor")
    commands >> executor >> game_server_cp

    with Cluster("Data Crawler"):
        workers = [
            ECS("worker1"),
            ECS("worker2"),
            ECS("worker3")
        ]
        game_server >> workers 

    with Cluster("DB Cluster"):
        redis = RDS("NPC State")

    with Cluster("Backend Server"):
        with Cluster("Writer"):
            state_flow = Dataflow("Collector")
            workers >> lb >> state_flow >> redis
        
        with Cluster("Reader"):
            planner = Dataflow("Planner")
            redis >> planner
            ai_server >> planner >> ai_server
            planner >> commands

