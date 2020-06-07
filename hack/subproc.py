import os
import subprocess

a = open(os.devnull, 'w')
#sp = subprocess.call(['python', 'os.py'], stdout=a, stderr=subprocess.STDOUT) #without uotput
sp = subprocess.call(['python os.py'], shell=True)
if sp == 0: 
    print("Proceso ejecutado")
else:
    print("No")