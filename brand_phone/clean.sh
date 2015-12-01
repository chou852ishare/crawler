#!/bin/bash

#cat ./uniq_device_info_from_game_center/* |sed 's\#\,\g'|sort >phone_brand
sort phone_brand |uniq >temp
mv temp phone_brand 
awk -F, '{if($0~/\?/); else print $0}' phone_brand > temp
mv temp phone_brand
awk -F, 'BEGIN{OFS=","}{gsub($1,"",$2); print $0}' phone_brand>temp
mv temp phone_brand
awk -F, 'BEGIN{OFS=","}{if($2~/[0-9]|[\w]/)print $0}' phone_brand >temp
mv temp phone_brand
sed 's\, *\,\g' phone_brand > temp
mv temp phone_brand 
awk -F, 'BEGIN{OFS=","}{if(length($1)<1) {gsub(" ",",",$2); print $2} else print $0}' phone_brand >temp
sed 's\^ *\\g' temp >temp1; mv temp1 temp  
mv temp phone_brand
sed 's\,_*\,\g' phone_brand >temp
sed 's\,-*\,\g' temp >temp1; mv temp1 temp
mv temp phone_brand 
awk -F, 'BEGIN{OFS=","}{if($1~/unknown/) {gsub(" ",",",$2);print $2} else print $0}' phone_brand > temp
mv temp phone_brand 
