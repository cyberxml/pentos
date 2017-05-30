yum -y install agg
yum -y install aide
yum -y install fltk
yum -y install ftp
yum -y install graphviz
yum -y install irssi
yum -y install libsmi
yum -y install lynx
yum -y install mariadb
yum -y install mutt
yum -y install net-snmp
yum -y install net-snmp-utils
yum -y install nmap
yum -y install openldap-clients
yum -y install openscap-utils
yum -y install openssh-askpass
yum -y install perl-Authen-SASL
yum -y install perl-Convert-ASN1
yum -y install perl-Digest-HMAC
yum -y install perl-GSSAPI
yum -y install perl-LDAP
yum -y install perl-XML-Filter-BufferText
yum -y install perl-XML-SAX-Writer
yum -y install php-dba
yum -y install php-ldap
yum -y install php-mysql
yum -y install php-odbc
yum -y install php-pgsql
yum -y install php-snmp
yum -y install php-soap
yum -y install php-xmlrpc
yum -y install postgresql-server
yum -y install python-linux-procfs
yum -y install python-matplotlib
yum -y install python-tornado
yum -y install rpmdevtools
yum -y install rsh
yum -y install scap-workbench
yum -y install scipy
yum -y install telnet
yum -y install texlive-base
yum -y install texlive-dvipng-bin
yum -y install texlive-dvipng
yum -y install texlive-kpathsea-bin
yum -y install texlive-kpathsea-lib
yum -y install texlive-kpathsea
yum -y install tftp
yum -y install tigervnc
yum -y install tigervnc-icons
yum -y install tix
yum -y install tkinter
yum -y install tokyocabinet
yum -y install urlview
yum -y install wireshark
yum -y install wireshark-gnome

#-- EPEL --

REL=$(wget -O- http://dl.fedoraproject.org/pub/epel/7/x86_64/e/ 2>/dev/null | grep -Po 'epel-release-7-.*?noarch.rpm')
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/${REL} 
rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/${REL}
yum -y update

yum install python-pip
yum install python-pip34
pip install --upgrade pip
pip3 install --upgrade pip

#ettercap
#freedts
yum -y install ntfs-3g
yum -y install p7zip
yum -y install perl-NetPacket
#perl-Net-RawIP
yum -y install python-oauth
yum -y install python-pip
yum -y install python-simplejson
#python-simpleparse
yum -y install rkhunter

# pen apps
yum -y install clamav
yum -y install nikto
#yum install john
#yum install m2crypto
#yum install masscan
#yum install metasploit-framework
#yum install openvas

# for phantomjs
yum -y install gperf

yum -y install p0f
yum -y install hping3

yum -y install dnsenum
yum -y install dnstop
yum -y install dnsmap

yum -y install lynis

yum -y install reaver
yum -y install rtl-sdr

yum -y install thc-ipv6

yum -y install dc3dd
yum -y install ddrescue
yum -y install extundelete
yum -y install tcpxtract
yum -y install CutyCapt

yum -y install slowhttptest
yum -y install hydra
yum -y install hydra-frontend

yum -y install scapy
