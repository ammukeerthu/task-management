## Setting up environment

### Install dependencies

Install Python 3.6

```sh
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
sudo yum install -y python36u python36u-pip
ln -s /usr/bin/python3.6 /usr/bin/python3
ln -s /usr/bin/pip3.6 /usr/bin/pip3
```

Install Python SDKs, frameworks and packages
```sh
sudo pip3 install -r requirements.txt
```

Execution of script
```sh
sudo python3 server.py
```
