# cd /opt/pentos/rpmbuild/SOURCES
# git clone https://github.com/breenmachine/httpscreenshot
# mv httpscreenshot pentos-httpscreenshot-YYYYMM
# tar --exclude='pentos-httpscreenshot-YYYYMM/.git' -czf pentos-httpscreenshot-YYYYMM.tar.gz pentos-httpscreenshot-YYYYMM
# from pentos top directory run
# rpmbuild -ba rpmbuild/SPECS/pentos-httpscreenshot.spec

Name:           pentos-httpscreenshot
Version:        201607
Release:        0
Summary:        HTTPScreenshot is a tool for grabbing screenshots and HTML of large numbers of websites
Group:          Applications/Other
License:        GPL
URL:            https://github.com/breenmachine/httpscreenshot
Vendor:         Breen Machine
Source:         pentos-httpscreenshot-201607.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
HTTPScreenshot is a tool for grabbing screenshots and HTML of large numbers of websites. The goal is for it to be both thorough and fast which can sometimes oppose each other.

%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/httpscreenshot"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/httpscreenshot"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/pentos/apps/httpscreenshot/httpscreenshot.py
/usr/local/pentos/apps/httpscreenshot/requirements.txt
/usr/local/pentos/apps/httpscreenshot/masshttp.sh
/usr/local/pentos/apps/httpscreenshot/screenshotClustering
/usr/local/pentos/apps/httpscreenshot/screenshotClustering/cluster.py
/usr/local/pentos/apps/httpscreenshot/screenshotClustering/popup.js
/usr/local/pentos/apps/httpscreenshot/README.md
/usr/local/pentos/apps/httpscreenshot/LiberationSerif-BoldItalic.ttf
/usr/local/pentos/apps/httpscreenshot/install-dependencies.sh
# inserted at BUILDROOT
/usr/local/pentos/apps/httpscreenshot/httpscreenshot.pyc
/usr/local/pentos/apps/httpscreenshot/httpscreenshot.pyo


%changelog
