
# required pentos components
# phantomjs
# PIL
# M2Crypto

# install pip
cd /opt
wget http://peak.telecommunity.com/dist/ez_setup.py
python ez_setup.py
easy_install pip

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
cd /opt/httpscreenshot
