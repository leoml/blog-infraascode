#! /usr/bin/python3.6

import yaml
import sys

if ( len(sys.argv) == 0 ) : 
    print ("SORRY!! No file receivid.")
    sys.exit(1)


with open((sys.argv[1]), 'r') as stream:
  try:
    yaml.safe_load(stream)
    print("[OK] - File (%s) validate with success! " % sys.argv[1])
  except yaml.YAMLError as exc:
    print("[Error] - File (%s) not valid!" %  sys.argv[1])
    print(exc)

#EOF
