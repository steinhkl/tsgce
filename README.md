# tsgce
Tiny Statistical Grammar Checking Engine

## Installing

See Install instructions in INSTALL.md

## Google API key

This Program uses the Google API and requires an API Key. You can create a Project and add an API Key at   https://console.developers.google.com/apis/

Put the key in google-api-key.txt .

## Google CSE

I am not sure if you need to create your own CSE but I don't think so.  
However: You can create a Custom Search Engine at https://cse.google.com/   
After adding it make sure to select "Search the entire web but emphasize included sites" for the Option "Sites to search"  
You can then modify biggercorpora.py  line 48.
