#----------------------------------
# Nikto
#----------------------------------

cd /opt
wget http://pkgs.repoforge.org/perl-Time-HiRes/perl-Time-HiRes-1.9724-1.el6.rfx.x86_64.rpm
rpm -i perl-Time-HiRes-1.9724-1.el6.rfx.x86_64.rpm

# /opt/nikto/program/nikto.pl
cd /opt
git clone https://github.com/sullo/nikto

mkdir /usr/local/nikto
mkdir /usr/local/nikto/bin

cp -rp /opt/nikto/program/* /usr/local/nikto/bin

echo "pathmunge /usr/local/nikto/bin" > /etc/profile.d/pentos-nikto.sh

