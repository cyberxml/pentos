# fix eth0
cd /etc/sysconfig/network-scripts/ 
sed -i -e 's@^ONBOOT=no@ONBOOT=yes@' ifcfg-eth0
ifup eth0

# add penne to the sudoers
echo "penne    ALL=(ALL)       ALL" >> /etc/sudoers


