#!/bin/bash

# Prompt for MySQL root password
read -sp "Enter MySQL root password or create new one: " root_password
echo

# Prompt for new user credentials
read -p "Choose a new user username: " user
echo
if [ -z "$user" ]; then
    echo "Error: Username cannot be empty."
    exit 1
fi

read -sp "Choose a new user password: " user_pass
echo
if [ -z "$user_pass" ]; then
    echo "Error: Password cannot be empty."
    exit 1
fi

# Database name
db_name="lmia_db"
tb_name="lmia_tb"

# Execute MySQL commands
mysql -u root -p"${root_password}"  <<MYSQL_SCRIPT
ALTER USER 'root'@'localhost' IDENTIFIED WITH sha256_password BY '${root_password}';
CREATE DATABASE IF NOT EXISTS \`${db_name}\`;
CREATE USER IF NOT EXISTS '${user}'@'localhost' IDENTIFIED WITH sha256_password BY '${user_pass}';
GRANT ALL PRIVILEGES ON \`${db_name}\`.* TO '${user}'@'localhost';
FLUSH PRIVILEGES;

USE \`${db_name}\`;
CREATE TABLE IF NOT EXISTS \`${tb_name}\` (
    year INT,
    province VARCHAR(255),
    stream VARCHAR(50),
    employer VARCHAR(255),
    address VARCHAR(255),
    occupation VARCHAR(255),
    incorporate_status VARCHAR(50),
    requested_lmia INT,
    requested INT
);

MYSQL_SCRIPT
echo "Database '${db_name}' and user '${user}' have been created successfully."
echo "Credential file (variables.conf) created"

# Output the result
cat <<EOF > variables.conf
db_password = ${user_pass} 
dbname = ${db_name} 
dbuser = ${user}
tbname = ${tb_name}
EOF

