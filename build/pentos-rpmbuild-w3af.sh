release=1.6.45

# cleanup
rm -rf /opt/pentos/rpmbuild/SOURCES/*w3af*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
git clone --depth 1 https://github.com/andresriancho/w3af.git

cd /opt/pentos/rpmbuild/SOURCES
mv w3af pentos-w3af-${release}
tar --exclude=pentos-w3af-${release}/.git -czf pentos-w3af-${release}.tar.gz pentos-w3af-${release}

# create rpm
cd /opt/pentos/rpmbuild/SOURCES/pentos-w3af-${release}
cp /opt/pentos/rpmbuild/SPECS/pentos-w3af.spec.stub /opt/pentos/rpmbuild/SPECS/pentos-w3af.spec
find . | sed 's#^\.#/usr/local/pentos/apps/w3af#' | grep -v "git"  >> /opt/pentos/rpmbuild/SPECS/pentos-w3af.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-w3af.spec
echo "%changelog" >> /opt/pentos/rpmbuild/SPECS/pentos-w3af.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-w3af.spec
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-w3af.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*w3af*

