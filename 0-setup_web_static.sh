#!/usr/bin/env bash
#  sets up your web servers for the deployment of web_static
if [ ! /f "/usr/sbin/nginx "]
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Tester" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chmod ubuntu:ubuntu -R /data/

sudo service nginx restart
