
# for manual google querys and parsing of resulting htmls
import requests
from bs4 import BeautifulSoup

def parsegooglehtml(searchstring):
    r = requests.get("https://www.google.com/search", params={'q':searchstring,'nfpr':1})
    soup = BeautifulSoup(r.text, "lxml")
    res = soup.find("div", {"id": "resultStats"})
    return int(res.text.replace(".", "").split()[1])
    pass


def main(listofsentences):
    # create a dictionary for the results:
    parsehtmlresults = {}

    # here we work on our sentences
    for sentence in listofsentences:
        # send all senteces to google and parse resulting HTML file
        parsehtmlresults[sentence] = parsegooglehtml(sentence)
        pass

    # Order by Number of results.
    parsehtmlresults = sorted(parsehtmlresults.items(), key=lambda x:x[1], reverse=True)

    # return sorted key:value pairs
    return parsehtmlresults


if __name__ == "__main__":
        main()
