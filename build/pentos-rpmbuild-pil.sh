# required for httpscreenshot

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/PIL
rm -rf /opt/pentos/rpmbuild/SOURCES/pentos-pil*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
wget http://effbot.org/media/downloads/PIL-1.1.7.tar.gz
tar xzf PIL-1.1.7.tar.gz
cd /opt/pentos/rpmbuild/SOURCES/PIL-1.1.7

# create rpm
python setup.py bdist_rpm
cp dist/PIL-1.1.7-1.src.rpm /opt/pentos/rpmbuild/SRPMS
cp dist/PIL-1.1.7-1.x86_64.rpm /opt/pentos/rpmbuild/RPMS/x86_64
cp dist/PIL-debuginfo-1.1.7-1.x86_64.rpm /opt/pentos/rpmbuild/RPMS/x86_64

