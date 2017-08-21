#!/usr/bin/env bash
# configures nginx web server & setsup file structure
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html><body><p>hi</p></body></html>" > \
/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '42 i \location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' \
    /etc/nginx/sites-available/default
service nginx restart
