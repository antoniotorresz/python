import os
from time import sleep

dir_name = "Created by py"
print(os.getcwd()) #Get current working path
os.chdir("/") #Equivalent to write cd command in terminal
print(os.getcwd())
print(os.listdir(os.getcwd())) # Equivalent to write ls in terminal
os.chdir("/home/ant/Escritorio")
print(os.getcwd())
os.mkdir(dir_name) # mkdir command creates a new folder
sleep(5)
os.rmdir("{}/{}".format(os.getcwd(), dir_name)) # rmdir command removes a new folder
sleep(3)
os.rename('busq.html', 'Changed.html') #Rename a file
sleep(3)
os.rename('Changed.html', 'busq.html')

#Print characteristics of a file
print(os.stat('busq.html'))
os.system("ping 192.168.1.69") #Executes any command with unix syntax
