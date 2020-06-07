#Script to get basic HTTP headers from a web page using GET method
import requests
import argparse

parser = argparse.ArgumentParser(description= "Header detector for web pages.")
parser.add_argument('-t', '--target', help="url of web page to get its headers")
parser = parser.parse_args()

def main():
    if parser.target:
        print(parser.target)
        try:
            url = requests.get(url = parser.target)
            headers = dict(url.headers)
            for x in headers:
                print("'{}' : {}\n".format(x, headers[x]))
        except Exception as e:
            print("Error: {}".format(e))
    else:
        print("No target...")

if __name__ == "__main__":
    main()
 