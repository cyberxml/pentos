Name:           pentos-squirrelsql
Version:        3.7
Release:        0
Summary:        squirrelsql
Group:          Applications/Other
License:        GPL
URL:            https://github.com/moyix/creddump
Vendor:         http://moyix.blogspot.com/
Source:         pentos-squirrelsql-3.7.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
squirrelsql

%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/squirrelsql"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/squirrelsql"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/pentos/apps/squirrelsql/pentos-squirrelsql-3.7.tar.gz
/usr/local/pentos/apps/squirrelsql/squirrel-sql-3.7-standard.jar
/usr/local/pentos/apps/squirrelsql/squirrelsql.sh

%changelog
