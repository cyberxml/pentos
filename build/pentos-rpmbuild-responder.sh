#----------------------------------
# Responder
#----------------------------------
# /opt/Responder/Responder.py

dt=$(date +%Y%j)

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/*esponde*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
git clone https://github.com/SpiderLabs/Responder
chmod +x Responder/Responder.py
mv Responder pentos-responder-2.3
tar --exclude='pentos-responder-2.3/.git' -czf pentos-responder-2.3.tar.gz pentos-responder-2.3

# create rpm
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-responder.spec

# show rpm
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*esponder*
