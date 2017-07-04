#----------------------------------
# make pentos repo and rpms
#----------------------------------

mkdir /opt/pentos/rpmbuild/BUILD
mkdir /opt/pentos/rpmbuild/BUILDROOT
mkdir /opt/pentos/rpmbuild/RPMS
mkdir /opt/pentos/rpmbuild/SOURCES
mkdir /opt/pentos/rpmbuild/SOURCES/x86_64
mkdir /opt/pentos/rpmbuild/SRPMS
echo "%_topdir    /opt/pentos/rpmbuild" >> ~/.rpmmacros

./pentos-rpmbuild-aircrack.sh
./pentos-rpmbuild-creddump.sh
./pentos-rpmbuild-exploitdb.sh
./pentos-rpmbuild-httpscreenshot.sh
./pentos-build-john.sh
./pentos-rpmbuild-phantomjs.sh
./pentos-rpmbuild-pil.sh
./pentos-rpmbuild-responder.sh
./pentos-rpmbuild-sqlmap.sh
./pentos-rpmbuild-squirrelsql.sh
./pentos-rpmbuild-w3af.sh
./pentos-rpmbuild-zap.sh

# use createrepo to create repodata directory and files
# use repo/7/pentos/x86_64 for path to rpms
# copy files from /opt/pentos/rpmbuild/RPMS/x86_64
