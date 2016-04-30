#----------------------------------
# creddump
#----------------------------------
cd /opt
git clone https://github.com/moyix/creddump

mkdir /usr/local/creddump
mkdir /usr/local/creddump/bin
cp -rp /opt/creddump/* /usr/local/creddump/bin

echo "pathmunge /usr/local/creddump/bin" > /etc/profile.d/pentos-creddump.sh



