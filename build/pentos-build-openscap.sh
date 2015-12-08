#----------------------------------
# OpenSCAP
#----------------------------------
# /usr/local/bin/oscap
yum -y install libcurl-devel
yum -y install libxml2-devel
yum -y install libxslt-devel
yum -y install pcre-devel
yum -y install bzip2-devel
yum -y install libtool
yum -y install swig

cd /opt
git clone https://github.com/OpenSCAP/openscap

cd /opt/openscap
./autogen.sh
./configure
make
make install
