#!/bin/sh
start-master.sh
start-slave.sh spark://contrib-jessie:7077
jupyter toree install --user --spark_opt='--master=spark://contrib-jessie:7077' --interpreters=Scala --spark_home=$SPARK_HOME
