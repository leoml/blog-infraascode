#!/usr/bin/python3
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server

# < diagrama >
with Diagram("Infra as <Code> - Diagrama" , filename="diagrama_infra_as_code_diagrama", outformat="jpg"):
    Server("web")

