# fix eth0
#cd /etc/sysconfig/network-scripts/ 
#sed -i -e 's@^ONBOOT=no@ONBOOT=yes@' ifcfg-eth0
#ifup eth0

# create pentest group
groupadd pentester
usermod -G pentester penne

# add penne to the sudoers
echo "penne    ALL=(ALL)       ALL" >> /etc/sudoers
echo "%pentester ALL=(ALL:ALL) ALL" >> /etc/sudoers

# disable SELinux for OPENVAS
sed -i -e 's@^SELINUX=.*$@SELINUX=disabled@' /etc/selinux/config
setenforce 0
