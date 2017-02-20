#!/bin/sh
start-master.sh
start-slave.sh $SPARK_URL
jupyter toree install --user --spark_opt="--master=$SPARK_URL" --interpreters=Scala --spark_home=$SPARK_HOME
