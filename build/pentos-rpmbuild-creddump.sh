#----------------------------------
# creddump
#----------------------------------

# cleanup directory
rm -rf /opt/pentos/rpmbuild/SOURCES/creddump
rm -rf /opt/pentos/rpmbuild/SOURCES/pentos-creddump*

# prepare sources
cd /opt/pentos/rpmbuild/SOURCES
git clone https://github.com/moyix/creddump
mv creddump pentos-creddump-0.3
tar --exclude='pentos-creddump-0.3/.git' -czf pentos-creddump-0.3.tar.gz pentos-creddump-0.3

# from pentos top directory run
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-creddump.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*creddump*

