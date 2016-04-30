# require pip
# require phantomjs
# require PIL
# require M2Crypto

#pip install m2crypto
pip install requests
pip install selenium
pip install beautifulsoup4
#pip install pillow
pip install requesocks

yum -y install openssl-devel
yum -y install fontconfig
yum -y install freetype

cd /opt
git clone https://github.com/breenmachine/httpscreenshot

mkdir /usr/local/httpscreenshot
mkdir /usr/local/httpscreenshot/bin
cp -rp /opt/httpscreenshot/* /usr/local/httpscreenshot/bin

echo "pathmunge /usr/local/httpscreenshot/bin" > /etc/profile.d/pentos-httpscreenshot.sh


