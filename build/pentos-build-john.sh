#----------------------------------
# John the Ripper
#----------------------------------
# /opt/john-1.8.0-jumbo-1/run/john
yum -y install openssl-devel

cd /opt/pentos/apps
wget http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz
tar xvzf john-1.8.0-jumbo-1.tar.gz
rm john-1.8.0-jumbo-1.tar.gz
cd /opt/pentos/apps/john-1.8.0-jumbo-1/src
./configure --disable-openmp
make
make install

chgrp -hR pentester /opt/pentos/apps/john-1.8.0-jumbo-1
chmod 750 /opt/pentos/apps/john-1.8.0-jumbo-1/
chmod 770 /opt/pentos/apps/john-1.8.0-jumbo-1/run

echo "pathmunge /opt/pentos/apps/john-1.8.0-jumbo-1/run" > /etc/profile.d/pentos-john.sh
