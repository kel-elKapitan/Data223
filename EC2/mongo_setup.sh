#!/bin/bash

# Update the packages
sudo apt-get update

# Install gnupg which is needed to import the MongoDB public GPG Key
# gnupg is a complete and free implementation of the OpenPGP standard
sudo apt-get install gnupg

# download MongoDB's GPG key and add it to a specific keyring file
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor

# Create a list file for MongoDB
# The list file tells apt-get where to download the MongoDB packages
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Reload the local package database
sudo apt-get update

# Install the MongoDB packages
sudo apt-get install -y mongodb-org

# Although you can specify any available version of MongoDB,
# apt-get will upgrade the packages when a newer version becomes available.
# To prevent unintended upgrades, you can pin the package at the currently installed version:

echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-database hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-mongosh hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections


# Start MongoDB
sudo systemctl start mongod





sudo systemctl restart mongodb