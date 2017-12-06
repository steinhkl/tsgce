
# for manual google querys and parsing of resulting htmls
import requests
from bs4 import BeautifulSoup

def parsegooglehtml(searchstring):
    r = requests.get("https://www.google.com/search", params={'q':searchstring,'nfpr':1})
    soup = BeautifulSoup(r.text, "lxml")
    res = soup.find("div", {"id": "resultStats"})
    return int(res.text.replace(".", "").split()[1])
    pass


def main(jsonlistofsentences):
    # create a dictionary for the results:
    parsehtmlresults = {}

    # here we work on our sentences
    for idx, form in enumerate(jsonlistofsentences["forms"]):
        # send all senteces to google and parse resulting HTML file
        jsonlistofsentences[idx]["googlehits"] = parsegooglehtml(form["sentence"])
        pass

    # Order by Number of results.
    jsonlistofsentences["forms"] = sorted(jsonlistofsentences["forms"], key=lambda x:x["googlehits"], reverse=True)

    # return sorted key:value pairs
    return parsehtmlresults


if __name__ == "__main__":
        main()
