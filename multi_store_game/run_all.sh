#!/bin/bash

cd /home/zzhou/crawler/multi_store_game/baidu
python crawler_baidugame.py

cd /home/zzhou/crawler/multi_store_game/wandoujia
python crawler_wandoujia.py

cd /home/zzhou/crawler/multi_store_game/xiaomi
python crawler_xiaomi.py

cd /home/zzhou/crawler/multi_store_game/yingyongbao
python crawler_yingyongbao.py

cd /home/zzhou/crawler/multi_store_game/zhushou360
python crawler_360game.py

