#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

#Creating requested folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

#Fake html file for testing purposes
sudo echo "
<html>
	<head>
	</head>
	<body>
		Thanks for visiting
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#creating a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#granting ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

making nginx serve content from current
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
