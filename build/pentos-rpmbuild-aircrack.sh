#----------------------------------
# aircrack
#----------------------------------
rel='1.2'
ver='-rc4'
ver=''

# prerequisite
yum -y install libnl3 libnl3-devel

# cleanup directory
rm -rf /opt/pentos/rpmbuild/SOURCES/aircrack*
rm -rf /opt/pentos/rpmbuild/SOURCES/pentos-aircrack*

# prepare sources
cd /opt/pentos/rpmbuild/SOURCES
# errors in fedora 26
# wget http://download.aircrack-ng.org/aircrack-ng-1.2-rc4.tar.gz
# tar xvzf aircrack-ng-1.2-rc4.tar.gz
# cd aircrack-ng-1.2-rc4
git clone https://github.com/aircrack-ng/aircrack-ng
mv aircrack-ng aircrack-ng-${rel}${ver}
cd aircrack-ng-${rel}${ver}
make
cd ..

mkdir /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}
mkdir /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
mkdir /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/man

# Originally /usr/local/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airbase-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/aircrack-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airdecap-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airdecloak-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/aireplay-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airodump-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airserv-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airtun-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/airventriloquist-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/besside-ng-crawler /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/ivstools /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/kstats /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/makeivs-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/packetforge-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/src/wpaclean /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin

# Originally /usr/local/sbin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/scripts/airmon-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/scripts/airodump-ng-oui-update /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/bin

cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-${rel}${ver}/manpages/* /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/man
rm /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}/man/Makefile

tar -czf pentos-aircrack-${rel}.tar.gz pentos-aircrack-${rel}

# clean up
#rm -rf /opt/pentos/rpmbuild/SOURCES/aircrack-ng${ver}*
#rm -rf /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-${rel}

# from pentos top directory 
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-aircrack.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*aircrack*


#airbase-ng
#aircrack-ng
#airdecap-ng
#airdecloak-ng
#aireplay-ng
#airodump-ng
#airserv-ng
#airtun-ng
#besside-ng-crawler
#ivstools
#kstats
#makeivs-ng
#packetforge-ng
#wpaclean

