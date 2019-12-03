#!/bin/bash

function list_rca_files(){
	echo ''''''''''''''''''''''''''''''''''''''''''''''
        echo These are the rca files available:
        ls -l /data/rca
	echo ''''''''''''''''''''''''''''''''''''''''''''''
}

echo "Enter Proxy settings. Hit Enter to proceed if field is Not Applicable"
printf "\n"

read -p "Enter HTTPS Proxy URL/ IP : " proxy_url
read -p "Enter Proxy port number : " proxy_port
read -p "Enter Proxy username( if any): " proxy_username
read -s  -p "Enter Proxy password( if any): " proxy_pwd
printf "\n"

if [ ${#proxy_url} -le 1 ]; 
   then echo "No proxy set. Proceeding";
elif [ ${#proxy_username} -le 1 ];
   then echo "Setting proxy. No proxy credentials. Proceeding";
   export https_proxy=http://$proxy_url:$proxy_port/ ;
else
   echo "Setting proxy with credentials. Proceeding";
   export https_proxy=http://$proxy_username:$proxy_pwd@$proxy_url:$proxy_port/ ;
fi

export PYTHONWARNINGS="ignore:Unverified HTTPS request"

list_rca_files
if /opt/maglev/bin/python _main.py; then
   nohup /opt/maglev/bin/python uploadRca.py &
fi
