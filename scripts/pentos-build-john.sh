#----------------------------------
# John the Ripper
#----------------------------------
# /opt/john-1.8.0-jumbo-1/run/john
cd /opt
wget http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz
tar xvzf john-1.8.0-jumbo-1.tar.gz
cd john-1.8.0-jumbo-1
./configure
make