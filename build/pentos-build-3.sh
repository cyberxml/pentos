
#------------------------
# pentos repo installs
#------------------------

# use the repo
cp pentos.repo /etc/yums.repos.d

# yum -y --enablerepo pentos install "pentos-*"
yum -y --enablerepo pentos install pentos-creddump
# yum -y --enablerepo pentos install pentos-exploitdb
yum -y --enablerepo pentos install pentos-httpscreenshot
yum -y --enablerepo pentos install pentos-responder
yum -y --enablerepo pentos install pentos-sqlmap

mkdir /opt/pentos/apps
mkdir /opt/pentos/apps/Perl-Net-RawIP
cd /opt/pentos/apps/Perl-Net-RaqIP
wget http://grotte2.intello.com/repository/intello/centos/7/stable/x86_64/packages/perl-Net-RawIP-0.25-1.el7.centos.x86_64.rpm
rpm -i perl-Net-RawIP-0.25-1.el7.centos.x86_64.rpm
cd /opt/pentos/build

yum -y --enablerepo pentos install pentos-squirrelsql
yum -y --enablerepo pentos install pentos-w3af
yum -y --enablerepo pentos install pentos-zap
yum -y --enablerepo pentos install PIL

#------------------------
# manual installs
#------------------------

./pentos-build-john.sh
./pentos-build-masscan.sh
./pentos-build-metasploit.sh

#./pentos-build-openvas.sh
#yum install openvas
# this is messed up. Not build.py in current 
#./pentos-rpmbuild-phantomjs.sh
#>> ./pentos-build-rat.sh
#>> ./pentos-build-veil.sh
