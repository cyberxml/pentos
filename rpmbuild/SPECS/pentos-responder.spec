# cd /opt/pentos/rpmbuild/SOURCES
# git clone https://github.com/breenmachine/httpscreenshot
# mv Responder pentos-responder-2.3
# tar --exclude='pentos-responder-2.3/.git' -czf pentos-responder-2.3.tar.gz pentos-responder-2.3
# from pentos top directory run
# rpmbuild -ba rpmbuild/SPECS/pentos-responder.spec

Name:           pentos-responder
Version:        2.3
Release:        0
Summary:        Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server
Group:          Applications/Other
License:        GPL
URL:            https://github.com/SpiderLabs/Responder
Vendor:         Spider Labs
Source:         pentos-responder-2.3.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server

%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/responder"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/responder"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/pentos/apps/responder/odict.py
/usr/local/pentos/apps/responder/certs/responder.crt
/usr/local/pentos/apps/responder/certs/responder.key
/usr/local/pentos/apps/responder/certs/gen-self-signed-cert.sh
/usr/local/pentos/apps/responder/LICENSE
/usr/local/pentos/apps/responder/poisoners/__init__.py
/usr/local/pentos/apps/responder/poisoners/MDNS.py
/usr/local/pentos/apps/responder/poisoners/LLMNR.py
/usr/local/pentos/apps/responder/poisoners/NBTNS.py
/usr/local/pentos/apps/responder/packets.py
/usr/local/pentos/apps/responder/README.md
/usr/local/pentos/apps/responder/tools/SMBRelay.py
/usr/local/pentos/apps/responder/tools/DHCP.py
/usr/local/pentos/apps/responder/tools/DHCP_Auto.sh
/usr/local/pentos/apps/responder/tools/BrowserListener.py
/usr/local/pentos/apps/responder/tools/FindSMB2UPTime.py
/usr/local/pentos/apps/responder/tools/RelayPackets.py
/usr/local/pentos/apps/responder/tools/FindSQLSrv.py
/usr/local/pentos/apps/responder/tools/Icmp-Redirect.py
/usr/local/pentos/apps/responder/settings.py
/usr/local/pentos/apps/responder/fingerprint.py
/usr/local/pentos/apps/responder/utils.py
/usr/local/pentos/apps/responder/servers/__init__.py
/usr/local/pentos/apps/responder/servers/MSSQL.py
/usr/local/pentos/apps/responder/servers/SMTP.py
/usr/local/pentos/apps/responder/servers/Browser.py
/usr/local/pentos/apps/responder/servers/LDAP.py
/usr/local/pentos/apps/responder/servers/DNS.py
/usr/local/pentos/apps/responder/servers/FTP.py
/usr/local/pentos/apps/responder/servers/HTTP.py
/usr/local/pentos/apps/responder/servers/Kerberos.py
/usr/local/pentos/apps/responder/servers/POP3.py
/usr/local/pentos/apps/responder/servers/SMB.py
/usr/local/pentos/apps/responder/servers/IMAP.py
/usr/local/pentos/apps/responder/servers/HTTP_Proxy.py
/usr/local/pentos/apps/responder/Responder.conf
/usr/local/pentos/apps/responder/files/BindShell.exe
/usr/local/pentos/apps/responder/files/AccessDenied.html
/usr/local/pentos/apps/responder/Responder.py
# added by rpmbuild
/usr/local/pentos/apps/responder/Responder.pyc
/usr/local/pentos/apps/responder/Responder.pyo
/usr/local/pentos/apps/responder/fingerprint.pyc
/usr/local/pentos/apps/responder/fingerprint.pyo
/usr/local/pentos/apps/responder/odict.pyc
/usr/local/pentos/apps/responder/odict.pyo
/usr/local/pentos/apps/responder/packets.pyc
/usr/local/pentos/apps/responder/packets.pyo
/usr/local/pentos/apps/responder/poisoners/LLMNR.pyc
/usr/local/pentos/apps/responder/poisoners/LLMNR.pyo
/usr/local/pentos/apps/responder/poisoners/MDNS.pyc
/usr/local/pentos/apps/responder/poisoners/MDNS.pyo
/usr/local/pentos/apps/responder/poisoners/NBTNS.pyc
/usr/local/pentos/apps/responder/poisoners/NBTNS.pyo
/usr/local/pentos/apps/responder/poisoners/__init__.pyc
/usr/local/pentos/apps/responder/poisoners/__init__.pyo
/usr/local/pentos/apps/responder/servers/Browser.pyc
/usr/local/pentos/apps/responder/servers/Browser.pyo
/usr/local/pentos/apps/responder/servers/DNS.pyc
/usr/local/pentos/apps/responder/servers/DNS.pyo
/usr/local/pentos/apps/responder/servers/FTP.pyc
/usr/local/pentos/apps/responder/servers/FTP.pyo
/usr/local/pentos/apps/responder/servers/HTTP.pyc
/usr/local/pentos/apps/responder/servers/HTTP.pyo
/usr/local/pentos/apps/responder/servers/HTTP_Proxy.pyc
/usr/local/pentos/apps/responder/servers/HTTP_Proxy.pyo
/usr/local/pentos/apps/responder/servers/IMAP.pyc
/usr/local/pentos/apps/responder/servers/IMAP.pyo
/usr/local/pentos/apps/responder/servers/Kerberos.pyc
/usr/local/pentos/apps/responder/servers/Kerberos.pyo
/usr/local/pentos/apps/responder/servers/LDAP.pyc
/usr/local/pentos/apps/responder/servers/LDAP.pyo
/usr/local/pentos/apps/responder/servers/MSSQL.pyc
/usr/local/pentos/apps/responder/servers/MSSQL.pyo
/usr/local/pentos/apps/responder/servers/POP3.pyc
/usr/local/pentos/apps/responder/servers/POP3.pyo
/usr/local/pentos/apps/responder/servers/SMB.pyc
/usr/local/pentos/apps/responder/servers/SMB.pyo
/usr/local/pentos/apps/responder/servers/SMTP.pyc
/usr/local/pentos/apps/responder/servers/SMTP.pyo
/usr/local/pentos/apps/responder/servers/__init__.pyc
/usr/local/pentos/apps/responder/servers/__init__.pyo
/usr/local/pentos/apps/responder/settings.pyc
/usr/local/pentos/apps/responder/settings.pyo
/usr/local/pentos/apps/responder/tools/BrowserListener.pyc
/usr/local/pentos/apps/responder/tools/BrowserListener.pyo
/usr/local/pentos/apps/responder/tools/DHCP.pyc
/usr/local/pentos/apps/responder/tools/DHCP.pyo
/usr/local/pentos/apps/responder/tools/FindSMB2UPTime.pyc
/usr/local/pentos/apps/responder/tools/FindSMB2UPTime.pyo
/usr/local/pentos/apps/responder/tools/FindSQLSrv.pyc
/usr/local/pentos/apps/responder/tools/FindSQLSrv.pyo
/usr/local/pentos/apps/responder/tools/Icmp-Redirect.pyc
/usr/local/pentos/apps/responder/tools/Icmp-Redirect.pyo
/usr/local/pentos/apps/responder/tools/RelayPackets.pyc
/usr/local/pentos/apps/responder/tools/RelayPackets.pyo
/usr/local/pentos/apps/responder/tools/SMBRelay.pyc
/usr/local/pentos/apps/responder/tools/SMBRelay.pyo
/usr/local/pentos/apps/responder/utils.pyc
/usr/local/pentos/apps/responder/utils.pyo

%changelog
