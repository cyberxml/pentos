
release=1.0

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/*sqlmap*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
git clone https://github.com/sqlmapproject/sqlmap
mv sqlmap pentos-sqlmap-${release}
tar --exclude=pentos-sqlmap-${release}/.git -czf pentos-sqlmap-${release}.tar.gz pentos-sqlmap-${release}

# create rpm
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-sqlmap.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*sqlmap*

# use nodeps on rpm
