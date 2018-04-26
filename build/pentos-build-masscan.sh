#----------------------------------
# Masscan
#----------------------------------
# /usr/bin/masscan
yum -y install libpcap-devel
cd /opt/pentos/apps
#git clone https://github.com/robertdavidgraham/masscan
#cd /opt/pentos/apps/masscan
wget https://github.com/robertdavidgraham/masscan/archive/1.0.4.tar.gz
tar xvzf 1.0.4.tar.gz
cd masscan-1.0.4
make
make install
