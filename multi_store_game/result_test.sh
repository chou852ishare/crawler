#!/bin/bash

store=$1
cate=$2

wc -l text
grep $store text |awk -v s=$store -F"|" '{for(i=1;i<=NF;i++) if(gsub(s, s, $i)) print $1"| "$i}' |awk -v c=$cate -F" " '{for(i=1;i<=NF;i++) if(gsub(c, c, $i)) print $1"| "$i}'|sort -t":" -k2,2n |cat -n|tail
