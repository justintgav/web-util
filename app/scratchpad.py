#!/usr/bin/python3
import subprocess


process = subprocess.Popen(['python3', 'dlnap/dlnap/dlnap.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
if not err:
    tmp = out.decode().replace("[a]",'').splitlines()[1:]
    devices = dict()
    for x in tmp:
        dev_str = x.split('@')
        devices[dev_str[0].strip()] = dev_str[1].strip()
        
    print(devices)