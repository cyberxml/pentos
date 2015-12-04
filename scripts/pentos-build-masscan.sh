#----------------------------------
# Masscan
#----------------------------------
# /usr/bin/masscan
yum -y install libpcap-devel
cd /opt
git clone https://github.com/robertdavidgraham/masscan
cd /opt/masscan
make
make install
cd /opt
