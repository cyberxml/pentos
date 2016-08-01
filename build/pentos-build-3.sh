#./pentos-build-clamav.sh
yum install clamav
./pentos-rpmbuild-creddump.sh
./pentos-rpmbuild-exploitdb.sh
./pentos-rpmbuild-httpscreenshot.sh
#./pentos-build-john.sh
yum install john
#./pentos-build-m2crypto.sh
yum install m2crypto
#./pentos-build-masscan.sh
yum install masscan
#./pentos-build-metasploit.sh
yum install metasploit-framework
#./pentos-build-nikto.sh
yum install nikto
#./pentos-build-openvas.sh
yum install openvas
./pentos-rpmbuild-phantomjs.sh
./pentos-rpmbuild-pil.sh
#>> ./pentos-build-rat.sh
./pentos-rpmbuild-responder.sh
./pentos-rpmbuild-sqlmap.sh
./pentos-rpmbuild-squirrelsql.sh
#>> ./pentos-build-veil.sh
./pentos-build-w3af.sh
./pentos-build-zap.sh
