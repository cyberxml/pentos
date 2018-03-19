#------------------------
# pentos repo installs
#------------------------
mkdir /opt/pentos/apps

# use the repo
cp pentos.repo /etc/yum.repos.d

# yum -y --enablerepo pentos install "pentos-*"
yum -y --enablerepo pentos install pentos-creddump
# yum -y --enablerepo pentos install pentos-exploitdb
yum -y --enablerepo pentos install pentos-httpscreenshot
# broke
#yum -y --enablerepo pentos install pentos-responder
#yum -y --enablerepo pentos install pentos-sqlmap

mkdir /opt/pentos/apps
mkdir /opt/pentos/apps/Perl-Net-RawIP
yum -y install perl-Test-use-ok
cd /opt/pentos/apps/Perl-Net-RaqIP
wget http://grotte2.intello.com/repository/intello/centos/7/stable/x86_64/packages/perl-Net-RawIP-0.25-1.el7.centos.x86_64.rpm
rpm -i perl-Net-RawIP-0.25-1.el7.centos.x86_64.rpm
cd /opt/pentos/build

yum -y --enablerepo pentos install pentos-squirrelsql
yum -y --enablerepo pentos install pentos-w3af
yum -y --enablerepo pentos install pentos-zap
#yum -y --enablerepo pentos install PIL

