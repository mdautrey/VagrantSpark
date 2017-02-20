#!/usr/bin/env bash
PACKAGEDIR=/vagrant/package
HW_ARCH=64
if [ "$HW_ARCH" -eq 64 ]; then
    JDK_URL=http://download.oracle.com/otn-pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.tar.gz
    JDK_FILE=jdk-8u112-linux-x64.tar.gz
    ANACONDA_URL=https://repo.continuum.io/archive/Anaconda2-4.3.0-Linux-x86_64.sh
    ANACONDA_FILE=Anaconda2-4.3.0-Linux-x86_64.sh
fi



##############################
# installation de Java
##############################
if [ ! -d $PACKAGEDIR ]; then
    echo "CREATING PACKAGE DIRECTORY"
    mkdir $PACKAGEDIR
fi

if [ ! -f $PACKAGEDIR/$JDK_FILE ]; then
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" $JDK_URL -P $PACKAGEDIR
fi
cp -f $PACKAGEDIR/$JDK_FILE .
tar xvf $JDK_FILE
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


####################################
# installation d'Anaconda
####################################
if [ ! -f $PACKAGEDIR/$ANACONDA_FILE ]; then
    wget $ANACONDA_URL -P $PACKAGEDIR
fi
cp -f $PACKAGEDIR/$ANACONDA_FILE .
bash ./$ANACONDA_FILE -b -p /home/vagrant/anaconda2
echo 'PATH=$PATH:$HOME/anaconda2/bin' >> .bashrc
echo 'export PATH' >> .bashrc

####################################
# installation de TOREE
####################################
if [ ! -f $PACKAGEDIR/apache-toree-0.1.0.tar.gz ]; then
    wget https://dist.apache.org/repos/dist/dev/incubator/toree/0.1.0/rc6/toree-pip/apache-toree-0.1.0.tar.gz -P $PACKAGEDIR
fi
cp -f $PACKAGEDIR/apache-toree-0.1.0.tar.gz .
/home/vagrant/anaconda2/bin/pip install ./apache-toree-0.1.0.tar.gz

#####################################
# ajout du path vers bin
#####################################
chmod 555 /vagrant/bin/*.sh
echo 'PATH=$PATH:/vagrant/bin' >> .bashrc
echo 'export PATH' >> .bashrc


##################################
# Clean up
###################################
rm *.gz
rm *.tgz
rm *.sh
