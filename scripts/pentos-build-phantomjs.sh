echo This script may take over an hour to run
echo Phantomjs is a requirement for headless httpscreenshot

yum -y install gcc gcc-c++ make flex bison gperf ruby \
  openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \
  libpng-devel libjpeg-devel

cd /opt

git clone https://github.com/ariya/phantomjs.git

cd /opt/phantomjs
./build.py

cp /opt/phantomjs/bin/phantomjs /usr/local/bin

# currently this fails
# yum -y install rpm-build
# cd /opt/phantomjs/rpm
# ./mkrpm.sh phantom.js /opt/phantomjs/rpm

