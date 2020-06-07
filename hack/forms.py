
import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help = "Web Site Url.")
parser.add_argument("-s", "--search", help="Option to search.")
parser = parser.parse_args()

def main():
    if parser.search:
        #Creating browser object
        search = mechanize.Browser()
        search.set_handle_robots(False)
        search.set_handle_equiv(False)
        search.addheaders = [('User-Agent', 'Firefox')]
        search.open(str(parser.url))
        search.select_form(nr=0)
        search['q'] = parser.search
        search.submit()
        p = BeautifulSoup(search.response().read(), 'html5lib')

        for link in p.find_all('a'):
            print(str(link.get('href').replace('/url?q=', '')))
    else:
        print("No arguments given")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("Exiting...")
        exit()

        