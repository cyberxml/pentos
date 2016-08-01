dt=$(date +%Y%j)
release=2.1

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/*hantomj*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
git clone https://github.com/ariya/phantomjs.git
cd phantomjs
mv build.py build-remote.py
sed 's/"--remote"//' build-remote.py > build.py
chmod +x build.py
echo Y | ./build.py
cd /opt/pentos/rpmbuild/SOURCES
mv phantomjs pentos-phantomjs-${release}
tar --exclude=pentos-phantomjs-${release}/src -czf pentos-phantomjs-${release}.tar.gz pentos-phantomjs-${release}

# create rpm
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-phantomjs.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*phantomjs*
