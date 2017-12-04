#!bin/bash
#Auto deploy nfs client side 
#preparation
rpm -qa | grep "rpcbind"
if [ $? -ne 0 ]; then
    yum install rpcbind
fi
rpm -qa | grep "nfs-utils"
if [ $? -ne 0 ]; then
    yum install nfs-utils
fi
#check rpc-bind and nfs-server status
if [[ `systemctl|grep running|grep rpcbind` && `systemctl|grep nfs-server` ]] ; then
    echo 'rpcbind and nfs running'
else 
    echo 'rpcbind or nfs not running'
fi

#mount shared server file
#root_path should be defined

root_path=`sed -n '/location/{n;p}' /etc/nginx/nginx.conf | awk '/root/{print $2}'|sed 's/;$//'`
if [[ $root_path ]]; then
    echo $root_path
    mount -t nfs 192.168.0.110:/share $root_path 
else
    i=0
    while [[ $i -lt 3 && $i -ge 0 ]]
    #require a new root_path, change nginx.conf, mount shared file to root_path
    do
        read -p "please enter a valid path as nginx root: " root_path
        #check if entered path is valid
        if [ -d  "$root_path" ]; then
	#root_path valid
	    echo "$root_path valid"
            message="root $root_path"
	    sed -ri "/^[^#].*location \/ \{/a $message;" /etc/nginx/nginx.conf
            mount -t nfs 192.168.0.110:/share $root_path
            i=-1    
	else
  	      ((i++))
	     
        fi
    done

fi
