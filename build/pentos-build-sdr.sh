yum -y install cmake
# the following adds 750MB, figure out how to trim it
yum -y install qt5-* 
yum -y install pulseaudio-*
yum -y install gpredict
yum -y install audacity

# --------------------------
# install rtl-sdr software
# --------------------------
yum install rtl-sdr rtl-sdr-devel kalibrate-rtl libosmo-dsp

# --------------------------
# install hackrf software
# --------------------------
cd /opt/pentos/apps
yum install libgusb libgusb-devel
yum install fftw fftw-devel
wget https://github.com/mossmann/hackrf/releases/download/v2017.02.1/hackrf-2017.02.1.tar.xz
tar xvJf hackrf-2017.02.1.tar.xz
cd hackrf-2017.02.1
cd host
mkdir build
cd build
cmake ..
make
make install
ldconfig

# --------------------------
# install airspyone
# --------------------------
cd /opt/pentos/apps
git clone https://github.com/airspy/airspyone_host
cd airspyone_host
cd host
mkdir build
cd build
cmake ..
make
make install
ldconfig

# --------------------------
# install osmo-sdr
# --------------------------
cd /opt/pentos/apps
git clone https://git.osmocom.org/osmo-sdr
cd osmo-sdr
cd software
cd libosmodr
mkdir build
cd build
cmake ..
make
make install
ldconfig

# --------------------------
# install gr-osmosdr
# --------------------------
cd /opt/pentos/apps
#git clone https://git.osmocom.org/gr-osmosdr
#cd gr-osmodr
#cd software
#cd libosmodr
#mkdir build
#cd build
#cmake ..
#make
#make install
ldconfig

wget  http://cgit.osmocom.org/gr-osmosdr/snapshot/gr-osmosdr-0.1.4.tar.gz
tar xvzf gr-osmosdr-0.1.4.tar.gz
cd gr-osmosdr-0.1.4
mkdir build
cd build
cmake ..
make
make install
ldconfig

# --------------------------
# build gnuradio
# --------------------------
cd /opt/pentos/apps
sudo yum install libusb1-devel libusb-devel qt5-qtbase-devel python-cheetah boost148-devel bzip2-libs boost-thread.x86_64 boost148-thread.x86_64 gcc-c++
yum install cppunit cppunit-devel
yum install boost boost-devel
pip install Cheetah

#wget gnuradio-3.7.11.tar.gz
mkdir build
cd build
cmake ../
make
make install
ldconfig

# --------------------------
# build gnuradio
# --------------------------
cd /opt/pentos/apps
git clone https://github.com/csete/gqrx
cd gqrx
mkdir build
cd build
cmake ../
make
make install

# --------------------------
# build dump1090
# --------------------------
# ADS-B air traffic
cd /opt/pentos/apps
git clone https://github.com/antirez/dump1090
cd dump1090
make
cp dump1090 /usr/local/bin

# --------------------------
# rtl_ais
# --------------------------
cd /opt/pentos/apps
git clone https://github.com/dgiardini/rtl-ais
cd rtl-ais
make
cp rtl_ais /usr/local/bin

# --------------------------
# rtl_biast
# --------------------------
cd /opt/pentos/apps
git clone https://github.com/rtlsdrblog/rtl_biast
cd rtl-biast
mkdir build
cd build
cmake ..
make
cp src/rtl_biast /usr/local/bin

# --------------------------
# gnss-sdr
# --------------------------
ln -s /bin/aclocal /usr/bin/aclocal-1.15
yum -y install lapack lapack-devel
cd /opt/pentos/apps
git clone https://github.com/gnss-sdr/gnss-sdr
cd gnss-sdr
cd build
cmake ..
make

# --------------------------
# Xastir
# --------------------------
yum -y install motif-devel
cd /opt/pentos/apps
git clone https://github.com/Xastir/Xastir
cd Xastir
./bootstraph.sh
mkdir build
cd build
../configure
make
make install

# --------------------------
# multimon-ng
# --------------------------
cd /opt/pentos/apps
git clone https://github.com/EliasOenal/multimon-ng
cd multimon-ng
mkdir build
cd build
qmake-qt4 ../multimon-ng.pro
make
make install


# --------------------------
# freqwatch
# --------------------------
cd /opt/pentos/apps
git clone https://github.com/covertcodes/freqwatch
cd freqwatch
python setup.py make
python setup.py install
# will need to do some mysql configuration

# Description - Mode 			Frequency
# 12m Amateur Radio (AM/FM/CW/USB/LSB) 	24.890 - 24.990MHz
# CB Radio (AM/FM/USB/LSB) 		26 - 28MHZ
# 10m Amateur Radio (AM/FM/CW/USB/LSB) 	28.400 - 29.700MHz
# 6m Amateur Radio (AM/FM/CW/USB/LSB) 	50 - 52MHZ
# Civil Airband (AM) 			117.975 - 136.000 MHz
# 2m Amateur Radio (AM/FM/CW/USB/LSB) 	144 - 146MHZ
# Marine Band (FM) 			156 - 163MHz
# PMR (Private Mobile Radio) (NFM) 	163 - 185MHZ
# Military Airband (AM) 		200 - 399MHZ
# 70 cm Amateur Radio (AM/FM/CW/USB/LSB)430 - 440MHZ
# PMR and Security (NFM) 		440 - 470MHZ


# https://en.wikipedia.org/wiki/Advanced_Train_Control_System
# The RF segment operates at 4800 bits per second in the 900 MHZ radio band
# http://www.atcsmon.com/frequencies.html
Channel 	MCP (MHz) 	BCP (MHz) 	Predominant User
1 	896.8875 	935.8875 	Union Pacific
2 	896.9375 	935.9375 	CSX
3 	896.9875 	935.9875 	Shared ATCS Network
4 	897.8875 	936.8875 	BNSF
5 	897.9375 	936.9375 	Norfolk Southern
6 	897.9875 	936.9875 	Southern Pacific
