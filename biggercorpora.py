
# for manual google querys and parsing of resulting htmls
import requests
from bs4 import BeautifulSoup

def parsegooglehtml(searchstring):
    searchstring = '"'+searchstring+'"'
    r = requests.get("https://www.google.com/search", params={'q':searchstring,'nfpr':1})
    # check for rate limit
    if r.status_code == 503:
        print("You have reached the rate limit. Please wait.")
        return -1
        pass
    else:
        # else parse output
        soup = BeautifulSoup(r.text, "lxml")
        res = soup.find("div", {"id": "resultStats"})
        try:
            result = int(res.text.replace(".", "").split()[1])
        except:
            result = 1
        return result

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
