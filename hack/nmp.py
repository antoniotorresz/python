import nmap
def main():
    nm = nmap.PortScanner()
    ip = input("Enter Ip")
    nm.scan(hosts=ip, arguments="--top-ports 1000 --version-intensity 3")
    print("Executed command: {}".format(nm.command_line()))
    #print(nm.scaninfo())
    print("Protocols: {}".format(nm[ip].all_protocols()))
    print("Machine status: {}".format(nm[ip].state()))
    print(nm[ip]["tcp"])

    for port in nm[ip]['tcp'].keys():
        #print(port)
        for data in nm[ip]['tcp'][port]:
            print("{} : {}".format(data, nm[ip]['tcp'][port]))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error: {}".format(e))