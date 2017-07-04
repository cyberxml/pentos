#----------------------------------
# aircrack
#----------------------------------

# prerequisite
yum -y install libnl3 libnl3-devel

# cleanup directory
rm -rf /opt/pentos/rpmbuild/SOURCES/aircrack*
rm -rf /opt/pentos/rpmbuild/SOURCES/pentos-aircrack*

# prepare sources
cd /opt/pentos/rpmbuild/SOURCES
wget http://download.aircrack-ng.org/aircrack-ng-1.2-rc4.tar.gz
tar xvzf aircrack-ng-1.2-rc4.tar.gz
cd aircrack-ng-1.2-rc4
make 
cd ..
mkdir /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2
mkdir /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
mkdir /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/man

# Originally /usr/local/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/aircrack-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/airdecap-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/airdecloak-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/besside-ng-crawler /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/ivstools /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/kstats /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/makeivs-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/packetforge-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/wpaclean /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin

# Originally /usr/local/sbin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/scripts/airmon-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/scripts/airodump-ng-oui-update /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/airbase-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/aireplay-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/airserv-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin
cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/src/airtun-ng /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/bin

cp /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4/manpages/* /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/man
rm /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2/man/Makefile

tar -czf pentos-aircrack-1.2.tar.gz pentos-aircrack-1.2

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/aircrack-ng-1.2-rc4*
#rm -rf /opt/pentos/rpmbuild/SOURCES/pentos-aircrack-1.2

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

