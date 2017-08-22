#!/usr/bin/env bash
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "
<html>
   <head>
   </head>
   <body>
     Holberton School
   </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sed -i "44 i location /hbnb_static/ { \n alias /data/web_static/current/; }" \
    /etc/nginx/sites-enabled/default
service nginx restart
