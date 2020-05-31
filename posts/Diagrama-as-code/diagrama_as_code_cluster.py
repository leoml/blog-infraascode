#!/usr/bin/python3

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.database import  Mysql
from diagrams.onprem.network import Nginx

graph_attr = {
    "fontsize": "45",
    "bgcolor": "white"
}

with Diagram("Infra as <Code> - Cluster", filename="diagrama_infra_as_code_cluster", graph_attr=graph_attr):

    with Cluster("VLAN APP-WEB"):
        with Cluster("Cluster Servidores"):
            servers = [Server("Server1"),
                Server("Server2"),
                Server("Server3")]
        with Cluster("VLAN DataBase"):
            mysqldb = Mysql("MySQL")

    slb = Nginx ("Server-LB")
    slb >> servers >> mysqldb
