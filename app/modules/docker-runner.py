#!/usr/bin/env python3                                                                            
import subprocess
import shlex
import json

# Define command and options wanted
service = "docker"
command = service +" "+ <COMMAND_GOES_HERE>

# Create list with arguments for subprocess.run
args = shlex.split(command)

# Run subprocess.run and save output object
proc = subprocess.run(args, check=True, capture_output=True, text=True)

proc.stdout
print(proc.stdout)