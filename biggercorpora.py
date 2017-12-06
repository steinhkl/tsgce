
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
        # parse HTML output.
        soup = BeautifulSoup(r.text, "lxml")

        # Don't be fooled by suggested results.
        # TODO: This probably does not work outside of germany
        # edit to text="No resulst for " if google returns unlikely numbers.
        if soup.find(text="Keine Ergebnisse für "):
            print("No results found")
            return 0
            pass

        # find the div which contains number of results
        res = soup.find("div", {"id": "resultStats"})
        try:
            # if there is more than 1 result the query will return:
            # "About XXXX results"
            result = int(res.text.replace(".", "").split()[1])
        except:
            # otherwise it will return "1 Result"
            result = int(res.text.replace(".", "").split()[0])
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
