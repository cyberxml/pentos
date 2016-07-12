# cd /opt/pentos/rpmbuild/SOURCES
# git clone https://github.com/moyix/creddump
# mv creddump pentos-creddump-0.3
# tar --exclude='pentos-creddump-0.3/.git' -czf pentos-creddump-0.3.tar.gz pentos-creddump-0.3
# from pentos top directory run
# rpmbuild -ba rpmbuild/SPECS/pentos-creddump.spec

Name:           pentos-creddump
Version:        0.3
Release:        0
Summary:        creddump is a python tool to extract various credentials and secrets from Windows registry hives.
Group:          Applications/Other
License:        GPL
URL:            https://github.com/moyix/creddump
Vendor:         http://moyix.blogspot.com/
Source:         pentos-creddump-0.3.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
creddump is a python tool to extract various credentials and secrets from Windows registry hives. It currently extracts:
* LM and NT hashes (SYSKEY protected)
* Cached domain passwords
* LSA secrets

It essentially performs all the functions that bkhive/samdump2, cachedump, and lsadump2 do, but in a platform-independent way.

It is also the first tool that does all of these things in an offline way (actually, Cain & Abel does, but is not open source and is only available on Windows).

%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/creddump"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/creddump"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/pentos/apps/creddump/README
/usr/local/pentos/apps/creddump/pwdump.py
/usr/local/pentos/apps/creddump/cachedump.py
/usr/local/pentos/apps/creddump/framework/addrspace.py
/usr/local/pentos/apps/creddump/framework/__init__.py
/usr/local/pentos/apps/creddump/framework/newobj.py
/usr/local/pentos/apps/creddump/framework/types.py
/usr/local/pentos/apps/creddump/framework/win32/domcachedump.py
/usr/local/pentos/apps/creddump/framework/win32/__init__.py
/usr/local/pentos/apps/creddump/framework/win32/hashdump.py
/usr/local/pentos/apps/creddump/framework/win32/lsasecrets.py
/usr/local/pentos/apps/creddump/framework/win32/rawreg.py
/usr/local/pentos/apps/creddump/framework/object.py
/usr/local/pentos/apps/creddump/lsadump.py
/usr/local/pentos/apps/creddump/COPYING
/usr/local/pentos/apps/creddump/CHANGELOG
# generated in BUILDROOT
/usr/local/pentos/apps/creddump/cachedump.pyc
/usr/local/pentos/apps/creddump/cachedump.pyo
/usr/local/pentos/apps/creddump/framework/__init__.pyc
/usr/local/pentos/apps/creddump/framework/__init__.pyo
/usr/local/pentos/apps/creddump/framework/addrspace.pyc
/usr/local/pentos/apps/creddump/framework/addrspace.pyo
/usr/local/pentos/apps/creddump/framework/newobj.pyc
/usr/local/pentos/apps/creddump/framework/newobj.pyo
/usr/local/pentos/apps/creddump/framework/object.pyc
/usr/local/pentos/apps/creddump/framework/object.pyo
/usr/local/pentos/apps/creddump/framework/types.pyc
/usr/local/pentos/apps/creddump/framework/types.pyo
/usr/local/pentos/apps/creddump/framework/win32/__init__.pyc
/usr/local/pentos/apps/creddump/framework/win32/__init__.pyo
/usr/local/pentos/apps/creddump/framework/win32/domcachedump.pyc
/usr/local/pentos/apps/creddump/framework/win32/domcachedump.pyo
/usr/local/pentos/apps/creddump/framework/win32/hashdump.pyc
/usr/local/pentos/apps/creddump/framework/win32/hashdump.pyo
/usr/local/pentos/apps/creddump/framework/win32/lsasecrets.pyc
/usr/local/pentos/apps/creddump/framework/win32/lsasecrets.pyo
/usr/local/pentos/apps/creddump/framework/win32/rawreg.pyc
/usr/local/pentos/apps/creddump/framework/win32/rawreg.pyo
/usr/local/pentos/apps/creddump/lsadump.pyc
/usr/local/pentos/apps/creddump/lsadump.pyo
/usr/local/pentos/apps/creddump/pwdump.pyc
/usr/local/pentos/apps/creddump/pwdump.pyo


%changelog
