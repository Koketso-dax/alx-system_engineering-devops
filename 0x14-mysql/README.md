# mySQL for server installation:

wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb

sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

# Select bionic (5.7)

sudo apt-get update

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B7B3B788A8D3785C

sudo apt-get update

sudo apt-cache policy mysql-server

sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*