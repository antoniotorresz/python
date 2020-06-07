from subprocess import check_output
import subprocess

#Getting info from windows pc

a = check_output('lscpu', stderr=subprocess.STDOUT)

n = open('/home/ant/Escritorio/test.txt', 'w')
n.write(a)
print("All data getted")
n.close()