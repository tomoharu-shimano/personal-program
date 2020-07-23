#!/bin/bash

# set interval
interval=30

# set deviceid
deviceid=28-0300a2799855

# set Kinesis Firehoses name
streamname=sugiyt2-stream

while [ 1 ]
do
        (
                time=`date '+%F %T'`
                # mesure temp
                temp=$(awk -F= 'END {print $2/1000}' < /sys/bus/w1/devices/$deviceid/w1_slave)
                 
                if [ -n "$temp" ] ; then
                        payload='{\"time\":\"'$time'\", \"temperature\":'$temp'}'
                        # JSONを画面に表示
#                        echo $payload
#                        echo $temp
                        python led_org.py $temp
                        # put-record
                        aws firehose put-record --delivery-stream-name $streamname --record="{\"Data\":\"$payload\n\"}"
                fi
        ) &
        sleep $interval
done
