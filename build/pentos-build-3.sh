mkdir /opt/pentos/apps
mkdir /opt/pentos/rpmbuild/BUILD
mkdir /opt/pentos/rpmbuild/BUILDROOT
mkdir /opt/pentos/rpmbuild/RPMS
mkdir /opt/pentos/rpmbuild/SOURCES
mkdir /opt/pentos/rpmbuild/SOURCES/x86_64
mkdir /opt/pentos/rpmbuild/SRPMS
echo "%_topdir    %{getenv:HOME}/rpmbuild" >> ~/.rpmmacros

#./pentos-build-clamav.sh
#yum install clamav
./pentos-rpmbuild-creddump.sh
./pentos-rpmbuild-exploitdb.sh
./pentos-rpmbuild-httpscreenshot.sh
./pentos-build-john.sh
#yum install john
##./pentos-build-m2crypto.sh
##yum install m2crypto
./pentos-build-masscan.sh
#yum install masscan
./pentos-build-metasploit.sh
#yum install metasploit-framework
#./pentos-build-nikto.sh
#yum install nikto
#./pentos-build-openvas.sh
#yum install openvas
# this is messed up. Not build.py in current 
#./pentos-rpmbuild-phantomjs.sh
./pentos-rpmbuild-pil.sh
#>> ./pentos-build-rat.sh
./pentos-rpmbuild-responder.sh
./pentos-rpmbuild-sqlmap.sh
./pentos-rpmbuild-squirrelsql.sh
#>> ./pentos-build-veil.sh
./pentos-rpmbuild-w3af.sh
./pentos-rpmbuild-zap.sh
