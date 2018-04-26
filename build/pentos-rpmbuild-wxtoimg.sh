# --------------------------
# define variables
# --------------------------
BLD=/opt/pentos/rpmbuild/BUILD
SRC=/opt/pentos/rpmbuild/SOURCES
SPECS=/opt/pentos/rpmbuild/SPECS
release=2.10.11

# --------------------------
# clean before build
# --------------------------
rm -rf ${BLD}/*wxtoimg*
rm -rf ${SRC}/*wxtoimg*

# --------------------------
# install hackrf software
# --------------------------
cd ${BLD}
wget http://www.wxtoimg.com/downloads/wxtoimg-linux64-${release}-1.tar.gz
mkdir pentos-wxtoimg-${release}
cd pentos-wxtoimg-${release}
tar xzf ../wxtoimg-linux64-${release}-1.tar.gz
cd ..

tar czf pentos-wxtoimg-${release}.tar.gz pentos-wxtoimg-${release}/
mv pentos-wxtoimg-${release}.tar.gz ${SRC}

cd /opt/pentos

# create rpm
cp /opt/pentos/rpmbuild/SPECS/pentos-wxtoimg.spec.stub /opt/pentos/rpmbuild/SPECS/pentos-wxtoimg.spec
cd ${BLD}/pentos-wxtoimg-${release}
find . | sed 's#^.##' >> /opt/pentos/rpmbuild/SPECS/pentos-wxtoimg.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-wxtoimg.spec
echo "%changelog" >> /opt/pentos/rpmbuild/SPECS/pentos-wxtoimg.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-wxtoimg.spec
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-wxtoimg.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*wxtoimg*

