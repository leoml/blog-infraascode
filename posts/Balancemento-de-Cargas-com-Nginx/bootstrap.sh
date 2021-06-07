#!/bin/bash


if [[ `uname -n` = "iac-client01" ]]; then

  sudo apt update 
  echo "## Installing PIPPython3 ans Ansible ..."
  sudo apt install python3-pip sshpass aptitude sshpass  ansible -y

else

  sudo apt update -y

fi

#EOF