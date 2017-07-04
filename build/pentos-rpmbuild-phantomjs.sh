dt=$(date +%Y%j)
release=2.1.1

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/*hantomj*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES

# build from source has changed
# requires apt and docker
#git clone https://github.com/ariya/phantomjs.git
#cd phantomjs
#mv build.py build-remote.py
#sed 's/"--remote"//' build-remote.py > build.py
#chmod +x build.py
#echo Y | ./build.py

# build from binary
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${release}-linux-x86_64.tar.bz2
tar xvjf phantomjs-${release}-linux-x86_64.tar.bz2
mv phantomjs-${release}-linux-x86_64 pentos-phantomjs-${release}
tar -czf pentos-phantomjs-${release}.tar.gz pentos-phantomjs-${release}

# create rpm
cp /opt/pentos/rpmbuild/SPECS/pentos-phantomjs.spec.stub /opt/pentos/rpmbuild/SPECS/pentos-phantomjs.spec
cd /opt/pentos/rpmbuild/SOURCES/pentos-phantomjs-${release}
find . | sed 's#^\.#/usr/local/pentos/apps/phantomjs#' >> /opt/pentos/rpmbuild/SPECS/pentos-phantomjs.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-phantomjs.spec
echo "%changelog" >> /opt/pentos/rpmbuild/SPECS/pentos-phantomjs.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-phantomjs.spec
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-phantomjs.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*phantomjs*
