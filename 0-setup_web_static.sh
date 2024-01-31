#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

echo "<html><head></head><body>Test page</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo chown -R ubuntu:ubuntu /data/

config_content="
server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
    location / {
        add_header X-Served-By \$hostname;
        proxy_pass http://localhost:5000;
    }
}
"

echo "$config_content" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
