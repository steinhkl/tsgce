# tsgce
Tiny Statistical Grammar Checking Engine

## Installing
### Dependencies
#### NLTK
[NLTK](http://www.nltk.org/)

``` bash
pip3 install nltk
```

#### Pattern

This Programm depends on the development branch of the [pattern](https://github.com/clips/pattern/) module. To install it, use following commands:

``` bash
git clone https://github.com/clips/pattern
cd pattern
git fetch
git checkout development
python setup.py install
```

It is possible, that and ModuleNotFoundError pops while installing pattern. So if "ModuleNotFoundError: No module named 'numpy'" pops up, simply install it by running pip:
``` bash
pip3 install numpy
```

#### Other dependencies

``` bash
pip3 install bs4
pip3 install lxml
pip3 install google-api-python-client
```

## Google API key

This Program uses the Google API and requires an API Key. You can create a Project and add an API Key at   https://console.developers.google.com/apis/

Put the key in google-api-key.txt .

## Google CSE

I am not sure if you need to create your own CSE but I don't think so.  
However: You can create a Custom Search Engine at https://cse.google.com/   
After adding it make sure to select "Search the entire web but emphasize included sites" for the Option "Sites to search"  
You can then modify biggercorpora.py  line 48.
