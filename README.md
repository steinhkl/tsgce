# tsgce
Tiny Statistical Grammar Checking Engine


## Dependencies
### NLTK
[NLTK](http://www.nltk.org/)

```
pip install nltk
```

### Pattern

This Programm depends on the development branch of the [pattern](https://github.com/clips/pattern/) module. To install it, use following commands:

```
git clone https://github.com/clips/pattern
cd pattern
git fetch
git checkout development
python setup.py install
```

It is possible, that and ModuleNotFoundError pops while installing pattern. So if "ModuleNotFoundError: No module named 'numpy'" pops up, simply install it by running pip:
```
pip install numpy
```
