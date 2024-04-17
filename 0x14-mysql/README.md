#### MYSQL for server installation:

1. wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb

2. sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb (Select bionic or 5.7)

3. sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B7B3B788A8D3785C

4. sudo apt-get update

5. sudo apt-cache policy mysql-server (Version 5.7 should now be present in dpkg)

6. sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

#### Task 1:
mysql -u root -p

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;

#### Task 2:

CREATE DATABASE tyrell_corp;

USE tyrell_corp;

CREATE TABLE nexus6 (
    column1 INT,
    column2 VARCHAR(255)
);

INSERT INTO nexus6 (column1, column2) VALUES (1, 'example');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;

#### Task 3:

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'any_password';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;


#### Task 4:

CHANGE MASTER TO
MASTER_HOST = '100.25.220.4', -- Replace with the actual IP address of web-01
MASTER_USER = 'replica_user',
MASTER_PASSWORD = 'your_replica_user_password',
MASTER_LOG_FILE = 'mysql-bin.000001', -- Use the value from web-01
MASTER_LOG_POS = 154; -- Use the value from web-01
START SLAVE;
SHOW SLAVE STATUS\G