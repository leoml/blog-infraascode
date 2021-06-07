#!/bin/bash

echo  "-= ESTATÍSTICAS DE ACESSOS =-"
echo "----------------------------"
echo "-= IPHash =-"
cat /var/log/nginx/nginx-iphash-access.log |awk -F " " '{ print $4}'|sort | uniq -c
echo "-= WRoundrobin =-"
cat /var/log/nginx/nginx-wroundrobin-access.log |awk -F " " '{ print $4}'|sort | uniq -c
echo "-= Roundrobin =-"
cat /var/log/nginx/nginx-roundrobin-access.log |awk -F " " '{ print $4}'|sort | uniq -c

