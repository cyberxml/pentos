# for rpm environment?
mkdir /opt/pentos/apps
mkdir /opt/pentos/apps/Perl-Net-RawIP
cd /opt/pentos/apps/Perl-Net-RaqIP
wget http://grotte2.intello.com/repository/intello/centos/7/stable/x86_64/packages/perl-Net-RawIP-0.25-1.el7.centos.x86_64.rpm
rpm -i perl-Net-RawIP-0.25-1.el7.centos.x86_64.rpm
cd /opt/pentos/build

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

#------------------------
# binwalk
#------------------------
cd /opt/pentos/apps
https://github.com/devttys0/binwalk/archive/v2.1.1.tar.gz
tar xvzf v2.1.1.tar.gz
cd binwalk-2.1.1
python setup.py install


#------------------------
# corkscrew: ssh over http
#------------------------
cd /opt/pentos/apps
git clone https://github.com/elia/corkscrew
cd corkscrew

#------------------------
# uncork: ssh over https
#------------------------
cd /opt/pentos/apps
git clone https://github.com/compulim/uncork
cd uncork
npm install uncork -g

#------------------------
# icmptunnel: tcp over icmp
#------------------------
cd /opt/pentos/apps

#------------------------
# iodine: tcp over dns
#------------------------
cd /opt/pentos/apps

#------------------------
# empire: python and powershell
#------------------------
cd /opt/pentos/apps
git clone https://github.com/EmpireProject/Empire
cd empire
./setup/install.sh

#------------------------
# crackmapexec:
#------------------------
cd /opt/pentos/apps
git clone https://github.com/byt3bl33d3r/CrackMapExec
cd empire
./setup/install.sh

#------------------------
# egressbuster
#------------------------
cd /opt/pentos/apps
git clone https://github.com/trustedsec/egressbuster
cd egressbuster
