#!/bin/bash

cd ./baidu
python crawler_baidugame.py

cd ../wandoujia
python crawler_wandoujia.py

cd ../xiaomi
python crawler_xiaomi.py

cd ../yingyongbao
python crawler_yingyongbao.py

cd ../zhushou360
python crawler_360game.py
