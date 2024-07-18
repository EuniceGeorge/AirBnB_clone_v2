#!/usr/bin/env bash
# Install Nginx

TARGET="/data/web_static/releases/test/"
LINK="/data/web_static/current"
DIR="/data/"

sudo apt-get -y update
sudo apt-get install nginx -y

#create necessary folders
#sudo mkdir -p /data/
#sudo mkdir -p /data/web_static/
#sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f "$TARGET" "$LINK"
sudo chown -R ubuntu:ubuntu "$DIR"

sudo sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-enabled/default

sudo service nginx restart
