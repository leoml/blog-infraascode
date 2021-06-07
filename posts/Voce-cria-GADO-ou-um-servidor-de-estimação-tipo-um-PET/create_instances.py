#!/usr/bin/python3.6

import boto3
import time

machines_ids=()

hosttags = {'fe-infra-as-code-01': 'front-end', 
            'fe-infra-as-code-02': 'front-end', 
            'be-infra-as-code-01': 'back-end', 
            'be-infra-as-code-02': 'back-end',
            'db-infra-as-code-01': 'data-base'} 

ec2 = boto3.resource('ec2')

def cria_maquina(hname,htag):
  new_reservation = ec2.create_instances(
    ImageId='ami-02c8813f1ea04d4ab',
    KeyName='lml_boto_aws',
    InstanceType='t1.micro',
    MinCount=1, 
    MaxCount=1)
  current_instance_id = str(new_reservation)
  current_instance_id = (current_instance_id.split("'")[1])
  ec2.create_tags(Resources=[current_instance_id], Tags=[{'Key':'Component_name', 'Value': hname}])
  ec2.create_tags(Resources=[current_instance_id], Tags=[{'Key':'Component_tag', 'Value': htag}])

for hname,htag  in hosttags.items():
  cria_maquina(hname,htag)
