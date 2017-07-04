
release=1.0
dt=$(date +%Y%j)

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/*sqlmap*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
git clone https://github.com/sqlmapproject/sqlmap
mv sqlmap pentos-sqlmap-${dt}
tar --exclude=pentos-sqlmap-${dt}/.git -czf pentos-sqlmap-${dt}.tar.gz pentos-sqlmap-${dt}

# create rpm
cd /opt/pentos
sed -e "s/YYYYDDD/${dt}/" /opt/pentos/rpmbuild/SPECS/pentos-sqlmap.spec.stub > /opt/pentos/rpmbuild/SPECS/pentos-sqlmap.spec
cd /opt/pentos/rpmbuild/SOURCES/pentos-sqlmap-${dt}
find . | sed 's#^\.#/usr/local/pentos/apps/sqlmap#' | grep -v "git"  >> /opt/pentos/rpmbuild/SPECS/pentos-sqlmap.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-sqlmap.spec
echo "%changelog" >> /opt/pentos/rpmbuild/SPECS/pentos-sqlmap.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-sqlmap.spec
cd /opt/pentos

rpmbuild -ba rpmbuild/SPECS/pentos-sqlmap.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*sqlmap*

# use nodeps on rpm
