# cd /opt/pentos/rpmbuild/SOURCES
# git clone https://github.com/moyix/creddump
# mv creddump pentos-creddump-0.3
# tar --exclude='pentos-creddump-0.3/.git' -cvzf pentos-creddump-0.3.tar.gz pentos-creddump-0.3
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
mkdir -p "$RPM_BUILD_ROOT"
cp -R * "$RPM_BUILD_ROOT"

%clean
#[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/README
/pwdump.py
/cachedump.py
/framework/addrspace.py
/framework/__init__.py
/framework/newobj.py
/framework/types.py
/framework/win32/domcachedump.py
/framework/win32/__init__.py
/framework/win32/hashdump.py
/framework/win32/lsasecrets.py
/framework/win32/rawreg.py
/framework/object.py
/lsadump.py
/COPYING
/CHANGELOG
# generated in BUILDROOT
/cachedump.pyc
/cachedump.pyo
/framework/__init__.pyc
/framework/__init__.pyo
/framework/addrspace.pyc
/framework/addrspace.pyo
/framework/newobj.pyc
/framework/newobj.pyo
/framework/object.pyc
/framework/object.pyo
/framework/types.pyc
/framework/types.pyo
/framework/win32/__init__.pyc
/framework/win32/__init__.pyo
/framework/win32/domcachedump.pyc
/framework/win32/domcachedump.pyo
/framework/win32/hashdump.pyc
/framework/win32/hashdump.pyo
/framework/win32/lsasecrets.pyc
/framework/win32/lsasecrets.pyo
/framework/win32/rawreg.pyc
/framework/win32/rawreg.pyo
/lsadump.pyc
/lsadump.pyo
/pwdump.pyc
/pwdump.pyo


%changelog
