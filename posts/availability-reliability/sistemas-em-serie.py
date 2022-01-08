#! /usr/bin/python3

from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.security import WAF
from diagrams.aws.database import Aurora

with Diagram("Infra as <Code> - Sistemas em série", show=True):

    with Cluster("Infra as <Code> - Sistemas em série"):
        with Cluster("Front-end"):
            front_end = [EC2("Front-end-01")]

        with Cluster("Back-end"):
            back_end =  [EC2("Back-end-01")]



        waf = WAF("WAF") 
        db =  Aurora("DB")
        fe_lb = ELB("Front-end-LB") 
        be_lb = ELB("Back-end-LB") 


    waf >> fe_lb >> front_end >> be_lb >> back_end >> db
