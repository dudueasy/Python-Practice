#!bin/bash
#Auto deploy nfs server side 
#nfs shared file & targets config variable: msg
#preparation
rpm -qa | grep "rpcbind" 
if [ $? -ne 0 ]; then
    yum install rpcbind
fi   

rpm -qa | grep "nfs-utils"
if [ $? -ne 0 ]; then
    yum install nfs-utils
fi

#configuration of nfs
  #shared folder and 
msg="/share 192.168.0.0/24(rw,sync,fsid=0)"
echo "$msg"> /etc/exports

#change mode of shared folder
chmod -R o+rw /share

#enable and start rpcbind & nfs service
systemctl start rpcbind.service
systemctl start nfs-server.service

systemctl enable rpcbind.service nfs-server.service

#check deployment
echo '##################################'
echo '--------current--nfs--info--------'
exportfs

if [[ `systemctl|grep running|grep rpcbind` && `systemctl|grep nfs-server` ]] ; then
    echo 'rpcbind and nfs are running'
else 
    echo 'rpcbind or nfs are not running correctly'
fi

echo '##################################'
showmount -a 
