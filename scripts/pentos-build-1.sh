# fix eth0
cd /etc/sysconfig/network-scripts/ 
sed -i -e 's@^ONBOOT=no@ONBOOT=yes@' ifcfg-eth0
ifup eth0
cd

# install git
yum -y install git

# add the PentOS build repository
cd /opt
git 
