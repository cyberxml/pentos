# require pip
# require phantomjs
# require PIL
# require M2Crypto

#pip install m2crypto
#pip install requests
#pip install selenium
#pip install beautifulsoup4
#pip install pillow
#pip install requesocks

#yum -y install openssl-devel
#yum -y install fontconfig
#yum -y install freetype


dt=$(date +%Y%j)

# clean up
rm -rf /opt/pentos/rpmbuild/SOURCES/*pscreenshot*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
git clone https://github.com/breenmachine/httpscreenshot
mv httpscreenshot pentos-httpscreenshot-${dt}
tar --exclude='pentos-httpscreenshot-${dt}/.git' -czf pentos-httpscreenshot-${dt}.tar.gz pentos-httpscreenshot-${dt}

# prepare SPEC
sed -e "s/YYYYDDD/${dt}/" /opt/pentos/rpmbuild/SPECS/pentos-httpscreenshot.spec.stub > /opt/pentos/rpmbuild/SPECS/pentos-httpscreenshot.spec

# create rpm
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-httpscreenshot.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*httpscreenshot*
