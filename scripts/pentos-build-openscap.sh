#----------------------------------
# OpenSCAP
#----------------------------------
# /usr/local/bin/oscap
yum -y install libcurl-devel
yum -y install libxml2-devel
yum -y install libxslt
yum -y install pcre

cd /opt
git clone https://github.com/OpenSCAP/openscap

cd /opt/openscap
./autogen.sh
./configure
make
make install