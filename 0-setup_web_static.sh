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
		Holberton School
	</body>
</html>" | sudo tee -a /data/web_static/releases/test/index.html >/dev/null

#creating a symbolic link
if [ -L /data/web_static/current ]; then
	    sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#granting ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#making nginx serve content from current
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
