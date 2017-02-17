#!/usr/bin/env bash
PACKAGEDIR=/vagrant/package

##############################
# installation de Java
##############################
if [ ! -d $PACKAGEDIR ]; then
    echo "CREATING PACKAGE DIRECTORY"
    mkdir $PACKAGEDIR
fi

if [ ! -f $PACKAGEDIR/jdk-8u112-linux-x64.tar.gz ]; then
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.tar.gz -P $PACKAGEDIR
fi
cp -f $PACKAGEDIR/jdk-8u112-linux-x64.tar.gz .
tar xvf jdk-8u112-linux-x64.tar.gz
echo 'ADDED BY VAGRANT' >> .bashrc
echo 'export JAVA_HOME=/home/vagrant/jdk1.8.0_112' >> .bashrc
echo 'PATH=$PATH:$JAVA_HOME/bin' >> .bashrc
echo 'export PATH' >> .bashrc

##################################
# installation de spark
##################################
if [ ! -f $PACKAGEDIR/spark-1.6.3-bin-hadoop2.6.tgz ]; then
    wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.3-bin-hadoop2.6.tgz -P $PACKAGEDIR
fi
cp -f $PACKAGEDIR/spark-1.6.3-bin-hadoop2.6.tgz .
tar xvf spark-1.6.3-bin-hadoop2.6.tgz
echo 'export SPARK_HOME=/home/vagrant/spark-1.6.3-bin-hadoop2.6' >> .bashrc
echo 'PATH=$PATH:$SPARK_HOME/sbin' >> .bashrc
echo 'export PATH' >> .bashrc
chown -R vagrant:vagrant /home/vagrant/spark-1.6.3-bin-hadoop2.6


###################################
# Clean up
###################################
rm *.gz
rm *.tgz
