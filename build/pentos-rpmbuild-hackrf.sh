# --------------------------
# define variables
# --------------------------
BLD=/opt/pentos/rpmbuild/BUILD
SRC=/opt/pentos/rpmbuild/SOURCES
SPECS=/opt/pentos/rpmbuild/SPECS
release=2017.02.1

# --------------------------
# clean before build
# --------------------------
rm -rf ${BLD}/*hackrf*
rm -rf ${SRC}/*hackrf*

# --------------------------
# install hackrf software
# --------------------------
cd ${BLD}
wget https://github.com/mossmann/hackrf/releases/download/v2017.02.1/hackrf-2017.02.1.tar.xz
tar xJf hackrf-${release}.tar.xz
cd hackrf-${release}
cd host
mkdir build
cd build
cmake ..
make

mkdir ${SRC}/pentos-hackrf-${release}
mkdir ${SRC}/pentos-hackrf-${release}/usr
mkdir ${SRC}/pentos-hackrf-${release}/usr/local
mkdir ${SRC}/pentos-hackrf-${release}/usr/local/bin
mkdir ${SRC}/pentos-hackrf-${release}/usr/local/include
mkdir ${SRC}/pentos-hackrf-${release}/usr/local/include/libhackrf
mkdir ${SRC}/pentos-hackrf-${release}/usr/local/lib
mkdir ${SRC}/pentos-hackrf-${release}/usr/local/lib/pkgconfig

cp ${BLD}/hackrf-2017.02.1/host/build/libhackrf/src/libhackrf.so.0.5.0 ${SRC}/pentos-hackrf-${release}/usr/local/lib/libhackrf.so.0.5.0
cp ${BLD}/hackrf-2017.02.1/host/build/libhackrf/src/libhackrf.so.0 ${SRC}/pentos-hackrf-${release}/usr/local/lib/libhackrf.so.0
cp ${BLD}/hackrf-2017.02.1/host/build/libhackrf/src/libhackrf.so ${SRC}/pentos-hackrf-${release}/usr/local/lib/libhackrf.so
cp ${BLD}/hackrf-2017.02.1/host/build/libhackrf/src/libhackrf.a ${SRC}/pentos-hackrf-${release}/usr/local/lib/libhackrf.a
cp ${BLD}/hackrf-2017.02.1/host/build/libhackrf/libhackrf.pc ${SRC}/pentos-hackrf-${release}/usr/local/lib/pkgconfig/libhackrf.pc
cp ${BLD}/hackrf-2017.02.1/host/libhackrf/src/hackrf.h ${SRC}/pentos-hackrf-${release}/usr/local/include/libhackrf/hackrf.h
cp ${BLD}/hackrf-2017.02.1/host/build/hackrf-tools/src/hackrf_cpldjtag ${SRC}/pentos-hackrf-${release}/usr/local/bin/hackrf_cpldjtag
cp ${BLD}/hackrf-2017.02.1/host/build/hackrf-tools/src/hackrf_debug ${SRC}/pentos-hackrf-${release}/usr/local/bin/hackrf_debug
cp ${BLD}/hackrf-2017.02.1/host/build/hackrf-tools/src/hackrf_info ${SRC}/pentos-hackrf-${release}/usr/local/bin/hackrf_info
cp ${BLD}/hackrf-2017.02.1/host/build/hackrf-tools/src/hackrf_spiflash ${SRC}/pentos-hackrf-${release}/usr/local/bin/hackrf_spiflash
cp ${BLD}/hackrf-2017.02.1/host/build/hackrf-tools/src/hackrf_sweep ${SRC}/pentos-hackrf-${release}/usr/local/bin/hackrf_sweep
cp ${BLD}/hackrf-2017.02.1/host/build/hackrf-tools/src/hackrf_transfer ${SRC}/pentos-hackrf-${release}/usr/local/bin/hackrf_transfer

cd ${SRC}
tar czf pentos-hackrf-${release}.tar.gz pentos-hackrf-${release}/

cd /opt/pentos

# create rpm
cp /opt/pentos/rpmbuild/SPECS/pentos-hackrf.spec.stub /opt/pentos/rpmbuild/SPECS/pentos-hackrf.spec
cd /opt/pentos/rpmbuild/SOURCES/pentos-hackrf-${release}
find . -type f  | sed 's#^.##' >> /opt/pentos/rpmbuild/SPECS/pentos-hackrf.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-hackrf.spec
echo "%changelog" >> /opt/pentos/rpmbuild/SPECS/pentos-hackrf.spec
echo  >> /opt/pentos/rpmbuild/SPECS/pentos-hackrf.spec
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-hackrf.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*hackrf*

