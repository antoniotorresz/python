import nmap
def main():
    nm = nmap.PortScanner()
    ip = raw_input("IP: ")
    nm.scan(hosts=ip, arguments="--top-ports 1000 --version-intensity 3")
    print("Executed command: {}".format(nm.command_line()))
    print(nm.scaninfo())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: {}".format(e))