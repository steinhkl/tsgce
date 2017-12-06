# tsgce
Tiny Statistical Grammar Checking Engine


## Dependencies
### NLTK
[NLTK](http://www.nltk.org/)

``` bash
pip install nltk
```

### Pattern

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
pip install numpy
```

Other dependencies that may need to be installed:

``` bash
pip3 install bs4
pip3 install lxml
```
