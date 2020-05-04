#!/usr/bin/python3

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.database import  Mysql
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.network import Haproxy, Internet
from diagrams.onprem.client import Users
from diagrams.onprem.inmemory import Redis

graph_attr = {
    "fontsize": "45",
    "bgcolor": "white"
}

with Diagram("Infra as <Code> - Classic Design", filename="diagrama_infra_as_code_classic_design", graph_attr=graph_attr):

    with Cluster("Web Application"):
        with Cluster("Frontend Cluster"):
            frontend = [Server("fe-server-01"),
                       Server("fe-server-02"),
                       Server("fe-server-03")]

        backend_lb = Nginx("Backend-LB")

        with Cluster("Backend Cluster"):
            backend = [Server("be-server-01"),
                        Server("be-server-02"),
                        Server("be-server-03")]

        Mysql_db = Mysql("MySQL-DB")

        with Cluster("Redis Cluster"):
            master = Redis("Master")
            master - Redis("Replica")


        with Cluster("Metrics"):
            metrics = Prometheus("Metric")
            metrics << Grafana("Monitoring")

        frontend_lb = Nginx("Frontend-LB")
    internet = Internet("Internet")
    webuser = Users("User")

    webuser >> Edge(color="black", label="TCP/443") >> internet >> Edge(color="black", label="TCP/443") >> \
    frontend_lb >> Edge(color="darkgreen", label="TCP/80") >> frontend >> Edge(color="darkgreen", label="TCP/80") >> \
    backend_lb >> Edge(color="darkgreen", label="TCP/80") >> backend >> Edge(color="red", label="TCP/3306",style="dashed") >> Mysql_db \
    >>  backend >>  Edge(color="orange", style="dotted") >>metrics
    backend >> Edge(color="blue", style="dotted") >> master
    frontend >> Edge(color="orange", style="dotted") >> metrics
