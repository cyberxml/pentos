#----------------------------------
# John the Ripper
#----------------------------------
# /opt/john-1.8.0-jumbo-1/run/john
yum -y install openssl-devel

cd /opt
wget http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz
tar xvzf john-1.8.0-jumbo-1.tar.gz
cd /opt/john-1.8.0-jumbo-1/src
./configure
make
make install