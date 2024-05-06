#!/usr/bin/env bash
# config server for deploying Airbnb static files
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Azul Dounit!" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
to_replace="# Add location to Airbnb static files\n\
\tlocation /hbnb_static {\n\
\t\talias /data/web_static/current/;\n\
\t}\n\
\n\
\terror_page 404 /404.html;"
sed -i "s@error_page 404 /404.html;@$to_replace@g" /etc/nginx/sites-available/default
service nginx restart
