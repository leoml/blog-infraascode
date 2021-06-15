#!/bin/bash

MAX="0"
while [ $MAX -lt 500 ];do
  curl -H "Host: iphashraddr.infraascode.com.br"  http://iphashraddr.infraascode.com.br/index.html &>/dev/null
  curl -H "Host: iphash.infraascode.com.br"  http://iphash.infraascode.com.br/index.html &>/dev/null
  curl -H "Host: roundrobin.infraascode.com.br"  http://roundrobin.infraascode.com.br/index.html &>/dev/null
  curl -H "Host: wroundrobin.infraascode.com.br"  http://wroundrobin.infraascode.com.br/index.html &>/dev/null
  MAX=$[$MAX+1]
done

#EOF
