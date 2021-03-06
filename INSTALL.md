# Installing tscge

To make use of our program you need to install some prequisites.  
The following has been verified on a freshly installed Ubuntu 17.10 Virtual Machine.


### Installing System Programs

Start by updating your System:
``` bash
sudo apt-get update && sudo apt-get -y upgrade
```

Then install the system prequisites:
``` bash
sudo apt-get -y install git python3 python3-pip libmysqlclient-dev libsvm-dev liblinear-dev
```
### Environment setup

clone the github repository
``` bash
git clone https://github.com/steinhkl/tsgce.git && cd tsgce
```

### Prequisites

Update Pip and install requirements:
``` bash
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade -r pip-requirements.txt
```

Install [pattern](https://github.com/clips/pattern) (development for Python3 Support):
``` bash
git clone https://github.com/clips/pattern && cd pattern
git fetch && git checkout development
sudo python3 ./setup.py install
cd ./../

```

### Configuration

Modify [Google API Key](https://console.developers.google.com/apis/)
``` bash
echo "YOU API KEY HERE" > google-api-key.txt
```

## Web Interface
``` bash
sudo apt-get install nodejs npm
cd ng5 Frontend/my-app/
sudo npm install
sudo npm install -g @angular/cli
``` 

