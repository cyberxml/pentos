Name:           pentos-aircrack
Version:        1.2
Release:        rc4
Summary:        aircrack
Group:          Applications/Other
License:        GPL
URL:            http://download.aircrack-ng.org/aircrack-ng-1.2-rc4.tar.gz
Vendor:         http://aircrack-ng.org
Source:         pentos-aircrack-1.2.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Aircrack-ng is a complete suite of tools to assess WiFi network security.
It focuses on different areas of WiFi security:
-    Monitoring: Packet capture and export of data to text files for further processing by third party tools.
-    Attacking: Replay attacks, deauthentication, fake access points and others via packet injection.
-    Testing: Checking WiFi cards and driver capabilities (capture and injection).
-    Cracking: WEP and WPA PSK (WPA 1 and 2).
All tools are command line which allows for heavy scripting. A lot of GUIs have taken advantage of this feature. It works primarily Linux but also Windows, OS X, FreeBSD, OpenBSD, NetBSD, as well as Solaris and even eComStation 2. 

%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/aircrack-ng"
mkdir -p "$RPM_BUILD_ROOT/usr/share/applications"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/aircrack-ng"
#cp /opt/pentos/menu/pentos-cachedump.desktop "$RPM_BUILD_ROOT/usr/share/applications"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/pentos/apps/aircrack-ng/bin/aircrack-ng
/usr/local/pentos/apps/aircrack-ng/bin/airdecap-ng
/usr/local/pentos/apps/aircrack-ng/bin/airdecloak-ng
/usr/local/pentos/apps/aircrack-ng/bin/airodump-ng
/usr/local/pentos/apps/aircrack-ng/bin/airodump-ng-oui-update
/usr/local/pentos/apps/aircrack-ng/bin/besside-ng-crawler
/usr/local/pentos/apps/aircrack-ng/bin/ivstools
/usr/local/pentos/apps/aircrack-ng/bin/kstats
/usr/local/pentos/apps/aircrack-ng/bin/makeivs-ng
/usr/local/pentos/apps/aircrack-ng/bin/packetforge-ng
/usr/local/pentos/apps/aircrack-ng/bin/wpaclean
/usr/local/pentos/apps/aircrack-ng/bin/airmon-ng
/usr/local/pentos/apps/aircrack-ng/bin/airbase-ng
/usr/local/pentos/apps/aircrack-ng/bin/aireplay-ng
/usr/local/pentos/apps/aircrack-ng/bin/airserv-ng
/usr/local/pentos/apps/aircrack-ng/bin/airtun-ng
/usr/local/pentos/apps/aircrack-ng/man/airbase-ng.8
/usr/local/pentos/apps/aircrack-ng/man/aircrack-ng.1
/usr/local/pentos/apps/aircrack-ng/man/airdecap-ng.1
/usr/local/pentos/apps/aircrack-ng/man/airdecloak-ng.1
/usr/local/pentos/apps/aircrack-ng/man/aireplay-ng.8
/usr/local/pentos/apps/aircrack-ng/man/airmon-ng.8
/usr/local/pentos/apps/aircrack-ng/man/airodump-ng.8
/usr/local/pentos/apps/aircrack-ng/man/airodump-ng-oui-update.8
/usr/local/pentos/apps/aircrack-ng/man/airolib-ng.1
/usr/local/pentos/apps/aircrack-ng/man/airserv-ng.8
/usr/local/pentos/apps/aircrack-ng/man/airtun-ng.8
/usr/local/pentos/apps/aircrack-ng/man/besside-ng.8
/usr/local/pentos/apps/aircrack-ng/man/besside-ng-crawler.1
/usr/local/pentos/apps/aircrack-ng/man/buddy-ng.1
/usr/local/pentos/apps/aircrack-ng/man/easside-ng.8
/usr/local/pentos/apps/aircrack-ng/man/ivstools.1
/usr/local/pentos/apps/aircrack-ng/man/kstats.1
/usr/local/pentos/apps/aircrack-ng/man/makeivs-ng.1
/usr/local/pentos/apps/aircrack-ng/man/packetforge-ng.1
/usr/local/pentos/apps/aircrack-ng/man/tkiptun-ng.8
/usr/local/pentos/apps/aircrack-ng/man/wesside-ng.8
/usr/local/pentos/apps/aircrack-ng/man/wpaclean.1

%changelog

