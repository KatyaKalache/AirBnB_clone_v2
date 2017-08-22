#!/usr/bin/env bash
#  sets up web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo '
<html>
   <head>
   </head>
   <body>
     Holberton School
   </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "44 i location /hbnb_static { \n alias /data/web_static/current/; }" \
    /etc/nginx/sites-enabled/default
service nginx restart
