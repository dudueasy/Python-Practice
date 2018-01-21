#!bin/bash
#check nginx packages
rpm -qa | grep nginx >/dev/null
if [ $? -ne 0 ]
    then
    #install nginx
        echo 'nginx is not installed'
        #yum install epel-release && yum install nginx
else
        echo 'nginx is installed'
fi       
#check status of nginx
systemctl | grep running | grep nginx
if [ $? -ne 0 ] 
    then
        echo "nginx is not active"
else
        echo "nginx is active"
fi
#preparation
sed -ri 's/(enforcing)$/disabled/' /etc/sysconfig/selinux
  #disabling selinux requires reboot
systemctl stop firewalld
systemctl disable firewalld

#configure nginx
message="upstream pythonweb { server server_1 weight=3;server server_2;server server_3;"
sed -ri "/^(http \{)/a $message" /etc/nginx/nginx.conf'
systemctl reload nginx

