echo This script may take over an hour to run
echo Phantomjs is a requirement for headless httpscreenshot
echo due to the larget size of the build directory,
echo ... it will be deleted after the buil

yum -y install gcc gcc-c++ make flex bison gperf ruby \
  openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \
  libpng-devel libjpeg-devel

cd /opt

git clone https://github.com/ariya/phantomjs.git

cd /opt/phantomjs
# build script includes remote option for git which breaks in CentOS 6
mv build.py build-remote.py
sed 's/"--remote"//' build-remote.py > build.py
chmod +x build.py
./build.py

cp /opt/phantomjs/bin/phantomjs /usr/local/bin

# currently this fails
# yum -y install rpm-build
# cd /opt/phantomjs/rpm
# ./mkrpm.sh phantom.js /opt/phantomjs/rpm

#rm -rf /opt/phantomjs

