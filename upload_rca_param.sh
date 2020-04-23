#!/bin/bash

function list_rca_files(){
	echo ''''''''''''''''''''''''''''''''''''''''''''''
        echo These are the rca files available:
        ls -l /data/rca
	echo ''''''''''''''''''''''''''''''''''''''''''''''
}

while getopts ":i:p:u:w:h" opt; do
   case $opt in 
      i) proxy_url="$OPTARG"
      ;;
      p) proxy_port="$OPTARG"
      ;;
      u) proxy_username="$OPTARG"
      ;;
      w) proxy_pwd="$OPTARG"
      ;;
      h) echo Command options:
            echo -i : Proxy IP
            echo -p : port
	    echo -u : proxy username
	    echo -w : proxy password
	    echo -h : Display this message and exit
	    exit 0
      ;;
   esac
done   
         

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
> nohup.out
if /opt/maglev/bin/python _main.py; then
   nohup /opt/maglev/bin/python uploadRca.py &
fi
