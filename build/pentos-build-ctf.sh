
# ------------------------
# featherduster
# ------------------------
cd /opt/pentos/apps
yum -y install gmp gmp-devel
yum -y install ncurses ncurses-devel
git clone https://github.com/nccgroup/featherduster
cd featherduster
python setup.py install


# ------------------------
# pkcrack
# ------------------------
cd /opt/pentos/apps
wget https://www.unix-ag.uni-kl.de/%7Econrad/krypto/pkcrack/pkcrack-1.2.2.tar.gz
tar xvzf pkcrack-1.2.2.tar.gz
cd pkcrack-1.2.2
cd src
make

# ------------------------
# pkcrack
# ------------------------
cd /opt/pentos/apps
git clone https://github.com/ius/rsatool
cd rsatool
python setup.py install

# ------------------------
# xortool
# ------------------------
cd /opt/pentos/apps
git clone https://github.com/hellman/xortool
cd xortool
python setup.py install

# ------------------------
# hashcat
# ------------------------
cd /opt/pentos/apps
wget https://hashcat.net/files/hashcat-3.6.0.7z
7za x hashcat-3.6.0
cd hashcat-3.6.0

# ------------------------
# hydra
# ------------------------
cd /opt/pentos/apps
wget https://github.com/vanhauser-thc/thc-hydra/archive/8.6.tar.gz
tar xvzf 8.6.tar.gz
cd thc-hydra-8.6
./configure
make
make install





