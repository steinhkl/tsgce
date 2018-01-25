# tsgce
Tiny Statistical Grammar Checking Engine

## Usage

To use the Programm you have to run the Webserver and the Frontend.
Then you go to http://localhost:4200/ and put in your sentence.

### Run Webserver

``` bash
./webserver.py
```

### Run Frontend

``` bash
cd ng5 Frontend
cd my-app
ng serve
```

## Installing

See Install instructions in [the installation Guide](INSTALL.md)

## Google API key

This Program uses the Google API and requires an API Key. You can create a Project and add an API Key at https://console.developers.google.com/apis/

Put the key in google-api-key.txt .

## Google CSE

I am not sure if you need to create your own CSE but I don't think so.  
However: You can create a Custom Search Engine at https://cse.google.com/   
After adding it make sure to select "Search the entire web but emphasize included sites" for the Option "Sites to search"  
You can then modify biggercorpora.py  line 48.

##Frontend Fixes
If ng serve is not working try
npm update -g @angular/cli

if its still not working try to install nodjs via package-manager
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
and do npm update -g @angular/cli again
 



