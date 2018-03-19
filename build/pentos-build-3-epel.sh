#-- EPEL --

ret=$(cat /etc/redhat-release | grep CentOS)
if (( $? < 1 )); then
    yum -y install epel-release
else
    REL=$(wget -O- http://dl.fedoraproject.org/pub/epel/7/x86_64/e/ 2>/dev/null | grep -Po 'epel-release-7-.*?noarch.rpm')
    wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/${REL} 
    rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/${REL}
fi
yum -y update

yum -y install python-pip
# what package did I think was here?
yum -y install python34-pip

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
#yum -y install rtl-sdr

yum -y install thc-ipv6

yum -y install dc3dd
yum -y install ddrescue
yum -y install extundelete
yum -y install tcpxtract
yum -y install CutyCapt

yum -y install slowhttptest
yum -y install hydra
yum -y install hydra-frontend

#yum -y install sc

yum -y install jack-audio-connection-kit jack-audio-connection-kit-devel
yum -y install portaudio portaudio-devel
yum -y install qwt qwt-devel
yum -y install scapy
yum -y install webkitgtk
yum -y install wxPython wxPython-devel

yum -y install npm

yum -y install clang

