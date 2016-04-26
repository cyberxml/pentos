# require metasploit
echo This build could take longer than an hour

# enable epel
wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm

# install mingw64
yum -y install mingw64-binutils \
 mingw64-cpp \
 mingw64-gcc \
 mingw64-gcc-c++ 

# install mono
yum -y install mono-core \
 mono-data \
 mono-data-oracle \
 mono-data-postgresql \
 mono-data-sqlite \
 mono-devel \
 mono-extras \
 mono-locale-extras \
 mono-mvc \
 mono-mvc-devel \
 mono-nunit \
 mono-nunit-devel \
 mono-wcf \
 mono-web \
 mono-web-devel \
 mono-winforms \
 mono-winfx 

yum -y install wine
yum -y install golang

# python-pefile
rpm -i https://forensics.cert.org/centos/cert/6/i386/python-pefile-1.2.10_114-1.el6.noarch.rpm

# mss tt fonts
# need to automate this
yum -y install cabextract
rpm -i http://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6.1.noarch.rpm

# --------------------------------------------
# Veil-Evasion: Source
# --------------------------------------------
cd /opt 
git clone https://github.com/Veil-Framework/Veil-Evasion.git
cd /opt/Veil-Evasion/setup
runuser="$(whoami)"
rootdir=$(cd "$( dirname "${BASH_SOURCE[0]}" )/../" && pwd)
silent=false

git clone https://github.com/Veil-Framework/Veil
cd Veil
./Install.sh -c

# --------------------------------------------
# Veil-Evasion: Python in Wine
# --------------------------------------------
pip install capstone
pip install symmetricjsonrpc

wget -qO - "http://winezeug.googlecode.com/svn/trunk/install-addons.sh" | bash -
wine cmd.exe /c ipconfig

echo -e '\n\n [*] Preparing (Wine) Directories...'
mkdir -p ~/.wine/drive_c/Python27/Lib/site-packages/ ~/.wine/drive_c/Python27/Scripts/
unzip -q -o -d ~/.wine/drive_c/Python27/Lib/ "${rootdir}/setup/python-distutils.zip"
unzip -q -o -d ~/.wine/drive_c/Python27/ "${rootdir}/setup/python-tcl.zip"
unzip -q -o -d ~/.wine/drive_c/Python27/ "${rootdir}/setup/python-Tools.zip"

# Install Setup Files
echo -e '\n\n [*] Installing (Wine) Python...'
arg="TARGETDIR=C:\Python27 ALLUSERS=1 /q"
wine msiexec /i "${rootdir}/setup/python-2.7.5.msi" ${arg}
tmp="$?"
[ "${tmp}" -ne "0" ] && echo -e " [ERROR] Failed To Install (Wine) Python 2.7.5... Exit Code: ${tmp}.\n"

echo -e '\n\n [*] Installing (Wine) Python Dependencies...'
pushd "${rootdir}/setup/" >/dev/null
for FILE in pywin32-219.win32-py2.7.exe pycrypto-2.6.win32-py2.7.exe; do
    echo -e "\n\n [*] Installing Python's $FILE..."
    if [[ "${silent}" == "true" ]]; then
      unzip -q -o "${FILE}"
      cp -rf PLATLIB/* ~/.wine/drive_c/Python27/Lib/site-packages/
      [ -e "SCRIPTS" ] && cp -rf SCRIPTS/* ~/.wine/drive_c/Python27/Scripts/
      rm -rf "PLATLIB/" "SCRIPTS/"
    else
      wine "${FILE}"
      tmp="$?"
      [ "${tmp}" -ne "0" ] && echo -e " [ERROR] Failed To Install ${FILE}... Exit Code: ${tmp}.\n" && exit 1
    fi
done

echo -e '\n\n [*] Installing (Wine) Python Dependencies - pywin32...'
wine C://Python27//python.exe C://Python27//Scripts//pywin32_postinstall.py -install

echo -e '\n\n [*] Installing PyInstaller (via ZIP)'
sudo unzip -q -o -d /opt "${rootdir}/setup/pyinstaller-2.0.zip"
sudo chmod -R 0755 /opt/pyinstaller-2.0/

# --------------------------------------------
# Veil-Evasion: Ruby in Wine
# --------------------------------------------
echo -e '\n\n [*] Initializing (Wine) Ruby Dependencies Installation...'

pushd "${rootdir}/setup/" >/dev/null

# Install Ruby Under Wine
echo -e '\n\n [*] Installing (Wine) Ruby & Dependencies'
mkdir -p ~/.wine/drive_c/Ruby187/lib/ruby/gems/1.8/

[[ "${silent}" == "true" ]] && arg="/silent"
arg="/silent"
wine "${rootdir}/setup/rubyinstaller-1.8.7-p371.exe" "${arg}"
tmp="$?"
[ "${tmp}" -ne "0" ] && echo -e " [ERROR] Failed To Install (Wine) Ruby.exe... Exit Code: ${tmp}.\n" && exit 1

# Install the OCRA Gem Under Wine
wine ~/.wine/drive_c/Ruby187/bin/ruby.exe ~/.wine/drive_c/Ruby187/bin/gem install ocra-1.3.0.gem
tmp="$?"
[ "${tmp}" -ne "0" ] && echo -e " [ERROR] Failed To Install (Wine) OCRA Gem... Exit Code: ${tmp}.\n" && exit 1

# Unzip the Ruby Dependencies
unzip -q -o -d ~/.wine/drive_c/Ruby187/lib/ruby/gems/1.8/ "${rootdir}/setup/ruby_gems-1.8.zip"

popd >/dev/null

# --------------------------------------------
# Veil-Evasion: Compiling GO
# --------------------------------------------
#echo -e '\n\n [*] Initializing Go Dependencies Installation...'
#pushd "/tmp/" >/dev/null


#mkdir -p /usr/src/go/
#echo -e ' [*] Installing Go (via TAR)'
##tar -xf "${rootdir}/setup/go1.4.2.src.tar.gz" -C /usr/src/
##20160422rb: new go source
#cd /opt/Veil-Evasion/setup
#wget https://www.veil-framework.com/InstallMe/go153x64.tar.gz
#tar -xf "${rootdir}/setup/go153x64.tar.gz" -C /usr/src/


# Compile
#cd /usr/src/go/src/
#./make.bash
#tmp="$?"
#[ "${tmp}" -ne "0" ] && echo -e " [ERROR] Failed To Compile Go... Exit Code: ${tmp}.\n" && exit 1

# Cross-Compile
#env GOOS=windows GOARCH=386 ./make.bash --no-clean
#env CGO_ENABLED=1 GOOS=windows GOARCH=386 CC_FOR_TARGET="i686-w64-mingw32-gcc -fno-stack-protector  -#D_FORTIFY_SOURCE=0 -lssp" ./make.bash --no-clean

# Done
#popd >/dev/null

# --------------------------------------------
# Veil-Evasion: Final Setup
# --------------------------------------------
echo -e '\n\n [*] Updating Veil-Framework Configuration...'
cd "${rootdir}/config/"
python update.py

mkdir -p /usr/share/veil-output/

# Chown Output Directory
echo -e "\n\n [*] Ensuring this account (${runuser}) owns veil output directory (/usr/share/veil-output/)..."
chown -R "${runuser}" /usr/share/veil-output/


