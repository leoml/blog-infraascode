#!/usr/bin/python3

from diagrams import Diagram
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.network import Nginx,Linkerd
from diagrams.onprem.database import Cassandra
from diagrams.onprem.client import  User

graph_attr = {
    "fontsize": "45",
    "bgcolor": "white"
}

with Diagram("Infra as <Code> - Nós", filename="diagrama_infra_as_code_nos", graph_attr=graph_attr):
    User("User")
    Nginx("Nginx")
    Cassandra("CDB")
    Linkerd("Linkerd")
