#!/usr/bin/env bash

##############################
# installation de Java
##############################
if [ ! -d /vagrant/package ]; then
    echo "CREATING PACKAGE DIRECTORY"
    mkdir /vagrant/package
fi

if [ ! -f /vagrant/package/jdk-8u112-linux-x64.tar.gz ]; then
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.tar.gz -P /vagrant/package/
fi
cp -f /vagrant/package/jdk-8u112-linux-x64.tar.gz .
tar xvf jdk-8u112-linux-x64.tar.gz
echo 'ADDED BY VAGRANT' >> .bashrc
echo 'export JAVA_HOME=/home/vagrant/jdk1.8.0_112' >> .bashrc
echo 'PATH=$PATH:$JAVA_HOME/bin' >> .bashrc
echo 'export PATH' >> .bashrc


