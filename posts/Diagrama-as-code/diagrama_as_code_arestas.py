#!/usr/bin/python3

from diagrams import Diagram
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Haproxy, Internet
from diagrams.onprem.database import Mysql
from diagrams.onprem.network import Nginx,Linkerd
from diagrams.onprem.client import User

graph_attr = {
    "fontsize": "45",
    "bgcolor": "white"
}

with Diagram("Infra as <Code> - Arestas", direction="TB", filename="diagrama_infra_as_code_arestas", outformat="png", graph_attr=graph_attr):

    with Cluster("Cluster Servidores"):
        servers_fe = [Server("Server1"),
               Server("Server2"),
               Server("Server3")]
    web_user = User("User")
    web_lb = Nginx("Nginx")
    mysql_db = Mysql("MySql-DB")
    www_net = Internet("Internet")

    web_user>>Edge(color="black", label="TCP/443")>>www_net >>Edge(color="green", label="TCP/443")  >> \
     web_lb >>  Edge(color="orange", label="TCP/80", style="dotted" ) >> servers_fe >>  Edge(color="red", label="TCP/3306" , style="dashed") >> mysql_db
