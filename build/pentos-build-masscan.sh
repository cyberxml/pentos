#----------------------------------
# Masscan
#----------------------------------
# /usr/bin/masscan
yum -y install libpcap-devel
cd /opt/pentos/apps
git clone https://github.com/robertdavidgraham/masscan
cd /opt/pentos/apps/masscan
make
make install
