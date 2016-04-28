# needs rsync port open
# failed without --wget option
# required:    openvas-mkcert-client -n -i  
# see https://fedoraproject.org/wiki/QA:Testcase_OpenVAS
#[root@localhost build]# openvasmd --create-user=admin
#User created with password 'c22c1142-01ef-4d46-adb5-31d052d52f07'.
#[root@localhost build]# openvasmd --create-user admin
#[root@localhost build]# openvasmd --user=admin --new-password=admin2wsx

yum -y install net-tools
yum -y install alien 

cd /opt

wget http://dl.fedoraproject.org/pub/epel/6/x86_64/heimdal-libs-1.6.0-0.9.20140621gita5adc06.el6.x86_64.rpm
rpm -i heimdal-libs-1.6.0-0.9.20140621gita5adc06.el6.x86_64.rpm

wget ftp://ftp.pbone.net/mirror/download.fedora.redhat.com/pub/fedora/epel/6/x86_64/hiredis-0.10.1-3.el6.x86_64.rpm
rpm -i hiredis-0.10.1-3.el6.x86_64.rpm

wget -q -O - http://www.atomicorp.com/installers/atomic |sh

yum -y --enablerepo=atomic-testing install redis
echo unixsocket /tmp/redis.sock >> /etc/redis.conf
echo unixsocketperm 700  >> /etc/redis.conf
/sbin/chkconfig --level 5 redis on
/sbin/chkconfig --level 4 redis on
/sbin/chkconfig --level 3 redis on
/sbin/chkconfig --level 2 redis on
service redis start

yum -y --enablerepo=atomic-testing install openvas-smb
yum -y --enablerepo=atomic-testing install openvas-libraries
yum -y --enablerepo=atomic-testing install openvas-scanner
yum -y --enablerepo=atomic-testing install openvas-cli
yum -y --enablerepo=atomic install wmi
yum -y --enablerepo=atomic downgrade openvas-libraries
yum -y --enablerepo=atomic install openvas-manager
yum -y --enablerepo=atomic install openvas
#yum -y --enablerepo=atomic install greenbone-security-assistant

#wget http://updates.atomicorp.com/channels/atomic-testing/centos/6/x86_64/RPMS/openvas-libraries-8.0.5-21.el6.art.x86_64.rpm
#rpm -ivh --force openvas-libraries-8.0.5-21.el6.art.x86_64.rpm

openvas-setup
# fails on sync
# this works: openvas-nvt-sync --wget
# this works: openvas-certdata-sync --wget

echo rebuilding openvasd
echo this will take several minutes
openvasmd --rebuild
openvasmd --create-user admin
openvasmd --user=admin --new-password=admin2wsx
openvasmd
echo default admin password set to 'admin2wsx'
echo it would be a good idea to change this later
echo 'openvasmd --user=admin --new-password=something'

#openvas-scapdata-sync
#openvas-certdata-sync
#openvas-nvt-sync

#service gsad start

echo to test the installation
echo open firefox to the url http://127.0.0.1:9392
echo and login with admin and admin2wsx
#echo please accept the security risk and log into OpenVas
#firefox --url https://127.0.0.1:9392 

