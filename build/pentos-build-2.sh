echo y | yum -y upgrade

# --------- tools ----------

yum -y install mailx
yum -y install mutt
yum -y install lynx
yum -y install wget
yum -y install curl
yum -y install bind-utils
yum -y install openssh-clients
yum -y install ftp
yum -y install telnet
yum -y install samba-client
yum -y install tcpdump
yum -y install nmap
yum -y install freedts
yum -y install postgresql
yum -y install mysql
yum -y install openldap-clients
yum -y install tftp
yum -y install rpcbind
yum -y install firefox
yum -y install evolution
#yum -y install libreoffice-*
yum -y install nfs-utils
yum -y install tigervnc
yum -y install irssi
yum -y install net-snmp-utils
yum -y install nc
yum -y install rsh
yum -y install wireshark

# --------- scripting ----------

yum -y install php
yum -y install php-dba
yum -y install php-ldap
yum -y install php-mysql
yum -y install php-odbc
yum -y install php-pgsql
yum -y install php-pdo
yum -y install php-process
yum -y install php-snmp
yum -y install php-soap
yum -y install php-xml
yum -y install php-xmlrpc


yum -y install python-dateutil
yum -y install python-ipaddr
yum -y install python-linux-procfs
yum -y install python-oauth
yum -y install python-simplejson
yum -y install python-simpleparse
yum -y install python-tornado
yum -y install pytz
yum -y install pywbem
yum -y install scipy
yum -y install python-matplotlib
yum -y install tkinter


yum -y install perl-LDAP

yum -y install ruby
yum -y install rubygems

yum -y install aide
yum -y install postgresql-server

# --------- build tools ----------
yum -y install gcc
yum -y install openssl
yum -y install openssl-devel
yum -y install libcurl-devel
yum -y install libxml2-devel
yum -y install libxslt-devel
yum -y install pcre-devel
yum -y install bzip2-devel
yum -y install libtool
yum -y install swig

# --------- enable epel ----------
wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm
# for pip, you need this env variable
# export https_proxy="http://<proxy.server>:<port>"
yum -y install pip
yum -y install p7zip
#yum -y install ntfs-3g
yum -y install rkhunter
