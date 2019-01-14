#!/usr/bin/env bash
# This script will install nginx and create a bunch of directories
apt-get update
apt-get -y upgrade
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "TEST. Welcome to pwu test page" > /data/web_static/releases/test/index.html
ln -f -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
NW="server_name localhost;\n\tlocation \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t}"
SRCH="server_name localhost;"
sed -i "0,/$SRCH/s/$SRCH/$NW/" /etc/nginx/sites-available/default
service nginx restart
