
cd /opt
git clone https://github.com/Veil-Framework/Veil
cd Veil
./Install.sh -c

# enable epel
wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm

# install mingw64
yum -y install mingw64-binutils \
 mingw64-cpp \
 mingw64-gcc \
 mingw64-gcc-c++ 

# install mono
yum -y install mono-core \
 mono-data \
 mono-data-oracle \
 mono-data-postgresql \
 mono-data-sqlite \
 mono-devel \
 mono-extras \
 mono-locale-extras \
 mono-mvc \
 mono-mvc-devel \
 mono-nunit \
 mono-nunit-devel \
 mono-wcf \
 mono-web \
 mono-web-devel \
 mono-winforms \
 mono-winfx 

yum -y install wine
