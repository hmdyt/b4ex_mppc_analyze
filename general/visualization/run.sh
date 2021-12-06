#!/bin/bash
# /data/hamada/easiroc_data/*root下のrootファイル全てに対してdrawVadc64ch.Cをかける
# <=> ADC High Gain の64chの絵を全てのrootファイルで書く

for file in /data/hamada/easiroc_data/*root
do
    a="drawVadc64ch.C("
    a+='"'
    a+=$file
    a+='")'
    root -b -q $a
done