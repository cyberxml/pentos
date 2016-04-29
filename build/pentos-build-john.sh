#----------------------------------
# John the Ripper
#----------------------------------
# /opt/john-1.8.0-jumbo-1/run/john
yum -y install openssl-devel

cd /opt
wget http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz
tar xvzf john-1.8.0-jumbo-1.tar.gz
rm john-1.8.0-jumbo-1.tar.gz
cd /opt/john-1.8.0-jumbo-1/src
./configure --disable-openmp
make
make install
mkdir /usr/local/john
mkdir /usr/local/john/bin
cp -rp /opt/john-1.8.0-jumbo-1/run/* /usr/local/john/bin 

echo "pathmunge /usr/local/john/bin" > /etc/profile.d/pentos-john.sh
