#----------------------------------
# John the Ripper
#----------------------------------
#/bin/bash
# Centos 7 John the Ripper Installation
yum -y install wget gpgme
yum -y group install "Development Tools"
cd /opt/pentos/apps
wget http://www.openwall.com/john/j/john-1.8.0.tar.xz
wget http://www.openwall.com/john/j/john-1.8.0.tar.xz.sign
wget http://www.openwall.com/signatures/openwall-signatures.asc
gpg --import openwall-signatures.asc
gpg --verify john-1.8.0.tar.xz.sign
tar xvfJ john-1.8.0.tar.xz
cd john-1.8.0/src
make clean linux-x86-64
cd ../run/
#./john --test
#password dictionnary download
wget -O - http://mirrors.kernel.org/openwall/wordlists/all.gz | gunzip -c > openwall.dico

chgrp -hR pentester /opt/pentos/apps/john-1.8.0
chmod 750 /opt/pentos/apps/john-1.8.0/
chmod 770 /opt/pentos/apps/john-1.8.0/run

#echo "pathmunge /opt/pentos/apps/john-1.8.0/run" > /etc/profile.d/pentos-john.sh
