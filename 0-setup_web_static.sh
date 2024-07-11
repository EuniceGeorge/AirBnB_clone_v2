#!/usr/bin/env bash
# This is a bash scrip that proforms the following:
        ###########################################################
        # --> Install nginx if it not exist                       #
        # --> Create a bunch of dir as seen below                 #
        # --> Create a fake html                                  #
        # --> Create a symbolic link                              #
        # --> Assign ownership to user ubuntu and group           #
        # --> Update the Nginx configuration to serve the         #
        # content of /data/web_static/current/ to hbnb_static     #
        # Finally: restart Nginx after updating the configuration #
        ###########################################################

        ##################################################################
        # set_up_requirements: this is a function that strieves to       #
        # the above set requirements by having it in a function i        #
        # can get installing nginx,apply the requirements and exit       #
        # if nginx does exist then i jump to applying the requirements   #
        ##################################################################

# Script begins here

set_up_requirements () {
        # Both commands create a directory
        mkdir -p /data/web_static/releases/test/
        mkdir -p /data/web_static/shared/

        # This writes into the below file
        echo \
                "
<html>
        <head>
        </head>
        <body>
          Holberton School
        </body>
</html>"> /data/web_static/releases/test/index.html

        # the ln allows for symbolic link creation
        # where -s == soft link and -f delete link if exist
        ln -sf /data/web_static/releases/test /data/web_static/current

        # chown command allows for giving and updating permissions
        chown -R ubuntu:ubuntu /data/

        # using the sed command to match a pattern and append
        # \ at the end of each line that continues onto the next line to indicate continuation.
        sed -i -e '/http {/a \
\        server {\
\            listen 80;\
\            server_name localhost;\
\            location /hbnb_static/ {\
\                alias /data/web_static/current/;\
\            }\
\        }\
' /etc/nginx/nginx.conf
        sudo nginx -s reload
}

if ! command -v nginx &> /dev/null; then

        # Update package list
        sudo apt-get -y update

        # Install nginx
        sudo apt-get -y install nginx

        # Start nginx (if not started automatically)
        sudo nginx

        # Call the requirements function runner
        set_up_requirements
        exit 0
else
        # A call to the requirements functon runner
        set_up_requirements
        exit 0
fi
