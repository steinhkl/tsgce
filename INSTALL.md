# Installing tscge

To make use of our program you need to install some prequisites.  
The following has been verified on a freshly installed Ubuntu 17.10 Virtual Machine.


## Installing System Programs

Start by updating your System:
``` bash
sudo apt-get update && sudo apt-get -y upgrade
```

Then install the system prequisites:
``` bash
sudo apt-get -y install git python3 python3-pip libmysqlclient-dev libsvm-dev liblinear-dev
```

clone the github repository
``` bash
git clone https://github.com/steinhkl/tsgce.git && cd tsgce
```

Update Pip and install requirements:
``` bash
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade -r pip-requirements.txt
```

Install pattern (development for Python3 Support):
``` bash
git clone https://github.com/clips/pattern && cd pattern
git fetch && git checkout development
sudo python3 ./setup.py install
cd ./../

```

Modify Google API Key
``` bash
nano google-api-key.txt
delete the line "!REPLACE THIS LINE WITH YOUR API KEY!"
insert your key
save with: ctrl + o
exit with: ctrl + x
```

Run a test with:
``` bash
./start.py "I are a test sentence"
```
