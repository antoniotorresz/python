import Wappalyzer._Wappalyzer as Wappalyzer
import Wappalyzer._WebPage as WebPage
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('u', '--url', help="Web site to get its technologies.")
parser = parser.parse_args()

def main():
    wap = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url(str(parser.url)) #source code from webpage
        techs = wap.analyze(web)

        for t in techs: 
            print("Tech: {}".format(t))
    except Exception as e:
        print("Error: {}".format(e))
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ki:
        print("Quiting...")
        exit()