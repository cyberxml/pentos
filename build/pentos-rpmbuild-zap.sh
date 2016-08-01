# 
release=2.5.0

# cleanup
rm -rf /opt/pentos/rpmbuild/SOURCES/*ZAP*
rm -rf /opt/pentos/rpmbuild/SOURCES/*zap*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
wget https://github.com/zaproxy/zaproxy/releases/download/${release}/ZAP_${release}_Linux.tar.gz
tar xzf ZAP_${release}_Linux.tar.gz
mv ZAP_${release} pentos-zap-${release}
rm ZAP_${release}_Linux.tar.gz
tar --exclude=pentos-zap-${release}/.git -czf pentos-zap-${release}.tar.gz pentos-zap-${release}

# create rpm
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-zap.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*zap*

