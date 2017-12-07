
# for manual google querys and parsing of resulting htmls
import requests
from bs4 import BeautifulSoup
import pprint
from googleapiclient.discovery import build

def GoogleAPILimit(APIKey):
    # returns true if API Key Call Limit has not been reached yet.
    # TODO: check API Call Limit for Key.
    return True
    pass

def GoogleParseLimit():
    # returns true if you can still query google.
    r = requests.get("https://www.google.com/search", params={'q':'test my query limit','nfpr':1})
    if r.status_code == 503:
        return False
    else:
         return True
    pass

def parsegooglehtml(searchstring):
    r = requests.get("https://www.google.com/search", params={'q':searchstring,'nfpr':1})
    # parses HTML output.
    soup = BeautifulSoup(r.text, "lxml")

    # TODO: This probably does not work outside of germany
    if soup.find(text="Keine Ergebnisse für "):
        return 0
        pass

    # find the div which contains number of results
    res = soup.find("div", {"id": "resultStats"})
    try:
        # if there is more than 1 result the query will return: "About XXXX results"
        result = int(res.text.replace(".", "").split()[1])
    except:
        # otherwise it will return "1 Result"
        result = int(res.text.replace(".", "").split()[0])
    return result

    pass

def queryGoogleCSEApi(searchstring, devKey):
    # build API Service
    service = build("customsearch", "v1", developerKey=devKey)
    # Specify Custom Search Engine.
    cseKey = "014193703923044144161:os4pqh4une0"
    res = service.cse().list(q=searchstring,cx=cseKey,).execute()
    return (res.get('searchInformation').get('totalResults'))
    pass


def main(listofsentences):
    # create a dictionary for the results:
    parsehtmlresults = {}
    queryGoogleAPIresults = {}
    # we read devkey from file so it is not in github.
    devKey = open("google-api-key.txt").read().strip()
    # Check wether we have reached API Calllimit.
    APILimit = GoogleAPILimit(devKey)
    HTMLLimit = GoogleParseLimit()

    # here we work on our sentences
    for sentence in listofsentences:
        # make it quoted for exact matching search results.
        sentence = '"'+sentence+'"'
        # send all senteces to google and parse resulting HTML file
        if HTMLLimit:
            parsehtmlresults[sentence] = parsegooglehtml(sentence)
            pass
        if APILimit:
            queryGoogleAPIresults[sentence] = queryGoogleCSEApi(sentence, devKey)
            pass
        pass

    # Order by Number of results.
    parsehtmlresults = sorted(parsehtmlresults.items(), key=lambda x:x[1], reverse=True)
    #TODO: This sorting does not seem to work yet. But we probably wont need it anymore once we have a data structure.
    queryGoogleAPIresults = sorted(queryGoogleAPIresults.items(), key=lambda x:x[1], reverse=True)

    # TODO: Add Results to JSON Data.
    # THIS IS WHERE I WOULD PUT MY JSON IF I HAD ANY!

    # return sorted key:value pairs
    return parsehtmlresults


if __name__ == "__main__":
        main()
