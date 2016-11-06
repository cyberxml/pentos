Name:           pentos-sqlmap
Version:        1.0
Release:        0
Summary:        sqlmap automates the process of detecting and exploiting SQL injection
Group:          Applications/Other
License:        GPL
URL:            https://github.com/moyix/creddump
Vendor:         http://moyix.blogspot.com/
Source:         pentos-sqlmap-1.0.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.


%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/sqlmap"
mkdir -p "$RPM_BUILD_ROOT/usr/share/applications"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/sqlmap"
cp /opt/pentos/menu/pentos-sqlmap.desktop "$RPM_BUILD_ROOT/usr/share/applications"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/share/applications/pentos-sqlmap.desktop
/usr/local/pentos/apps/sqlmap
/usr/local/pentos/apps/sqlmap/udf
/usr/local/pentos/apps/sqlmap/udf/postgresql
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.1
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.1/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/8.2
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/8.2/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/8.3
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/8.3/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.2
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.2/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.4
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.4/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.0
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.0/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/8.4
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/8.4/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.3
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/32/9.3/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.1
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.1/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/8.2
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/8.2/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/8.3
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/8.3/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.2
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.2/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.4
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.4/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.0
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.0/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/8.4
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/8.4/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.3
/usr/local/pentos/apps/sqlmap/udf/postgresql/linux/64/9.3/lib_postgresqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/8.2
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/8.2/lib_postgresqludf_sys.dll_
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/8.3
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/8.3/lib_postgresqludf_sys.dll_
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/9.0
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/9.0/lib_postgresqludf_sys.dll_
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/8.4
/usr/local/pentos/apps/sqlmap/udf/postgresql/windows/32/8.4/lib_postgresqludf_sys.dll_
/usr/local/pentos/apps/sqlmap/udf/mysql
/usr/local/pentos/apps/sqlmap/udf/mysql/linux
/usr/local/pentos/apps/sqlmap/udf/mysql/linux/32
/usr/local/pentos/apps/sqlmap/udf/mysql/linux/32/lib_mysqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/mysql/linux/64
/usr/local/pentos/apps/sqlmap/udf/mysql/linux/64/lib_mysqludf_sys.so_
/usr/local/pentos/apps/sqlmap/udf/mysql/windows
/usr/local/pentos/apps/sqlmap/udf/mysql/windows/32
/usr/local/pentos/apps/sqlmap/udf/mysql/windows/32/lib_mysqludf_sys.dll_
/usr/local/pentos/apps/sqlmap/udf/mysql/windows/64
/usr/local/pentos/apps/sqlmap/udf/mysql/windows/64/lib_mysqludf_sys.dll_
/usr/local/pentos/apps/sqlmap/udf/README.txt
/usr/local/pentos/apps/sqlmap/txt
/usr/local/pentos/apps/sqlmap/txt/checksum.md5
/usr/local/pentos/apps/sqlmap/txt/keywords.txt
/usr/local/pentos/apps/sqlmap/txt/common-outputs.txt
/usr/local/pentos/apps/sqlmap/txt/common-columns.txt
/usr/local/pentos/apps/sqlmap/txt/wordlist.zip
/usr/local/pentos/apps/sqlmap/txt/common-tables.txt
/usr/local/pentos/apps/sqlmap/txt/smalldict.txt
/usr/local/pentos/apps/sqlmap/txt/user-agents.txt
/usr/local/pentos/apps/sqlmap/sqlmapapi.py
/usr/local/pentos/apps/sqlmap/plugins
/usr/local/pentos/apps/sqlmap/plugins/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sqlite/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/oracle/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/db2/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/sybase/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/postgresql/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/access/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mysql/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/hsqldb/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/mssqlserver/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/firebird/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/connector.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/dbms/maxdb/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/generic
/usr/local/pentos/apps/sqlmap/plugins/generic/connector.py
/usr/local/pentos/apps/sqlmap/plugins/generic/__init__.py
/usr/local/pentos/apps/sqlmap/plugins/generic/enumeration.py
/usr/local/pentos/apps/sqlmap/plugins/generic/search.py
/usr/local/pentos/apps/sqlmap/plugins/generic/filesystem.py
/usr/local/pentos/apps/sqlmap/plugins/generic/custom.py
/usr/local/pentos/apps/sqlmap/plugins/generic/takeover.py
/usr/local/pentos/apps/sqlmap/plugins/generic/databases.py
/usr/local/pentos/apps/sqlmap/plugins/generic/entries.py
/usr/local/pentos/apps/sqlmap/plugins/generic/fingerprint.py
/usr/local/pentos/apps/sqlmap/plugins/generic/syntax.py
/usr/local/pentos/apps/sqlmap/plugins/generic/misc.py
/usr/local/pentos/apps/sqlmap/plugins/generic/users.py
/usr/local/pentos/apps/sqlmap/thirdparty
/usr/local/pentos/apps/sqlmap/thirdparty/termcolor
/usr/local/pentos/apps/sqlmap/thirdparty/termcolor/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/termcolor/termcolor.py
/usr/local/pentos/apps/sqlmap/thirdparty/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/pagerank
/usr/local/pentos/apps/sqlmap/thirdparty/pagerank/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/pagerank/pagerank.py
/usr/local/pentos/apps/sqlmap/thirdparty/colorama
/usr/local/pentos/apps/sqlmap/thirdparty/colorama/ansitowin32.py
/usr/local/pentos/apps/sqlmap/thirdparty/colorama/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/colorama/ansi.py
/usr/local/pentos/apps/sqlmap/thirdparty/colorama/win32.py
/usr/local/pentos/apps/sqlmap/thirdparty/colorama/initialise.py
/usr/local/pentos/apps/sqlmap/thirdparty/colorama/winterm.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/langhebrewmodel.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/escsm.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/big5prober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/jisfreq.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/sbcsgroupprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/gb2312freq.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/mbcharsetprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/euctwprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/hebrewprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/compat.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/constants.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/langgreekmodel.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/euckrprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/mbcssm.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/charsetprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/eucjpprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/sbcharsetprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/codingstatemachine.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/langcyrillicmodel.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/utf8prober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/chardistribution.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/langthaimodel.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/chardetect.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/jpcntx.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/mbcsgroupprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/escprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/charsetgroupprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/langbulgarianmodel.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/big5freq.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/langhungarianmodel.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/euctwfreq.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/latin1prober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/cp949prober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/gb2312prober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/euckrfreq.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/sjisprober.py
/usr/local/pentos/apps/sqlmap/thirdparty/chardet/universaldetector.py
/usr/local/pentos/apps/sqlmap/thirdparty/prettyprint
/usr/local/pentos/apps/sqlmap/thirdparty/prettyprint/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/prettyprint/prettyprint.py
/usr/local/pentos/apps/sqlmap/thirdparty/multipart
/usr/local/pentos/apps/sqlmap/thirdparty/multipart/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/multipart/multipartpost.py
/usr/local/pentos/apps/sqlmap/thirdparty/ansistrm
/usr/local/pentos/apps/sqlmap/thirdparty/ansistrm/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/ansistrm/ansistrm.py
/usr/local/pentos/apps/sqlmap/thirdparty/beautifulsoup
/usr/local/pentos/apps/sqlmap/thirdparty/beautifulsoup/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/beautifulsoup/beautifulsoup.py
/usr/local/pentos/apps/sqlmap/thirdparty/magic
/usr/local/pentos/apps/sqlmap/thirdparty/magic/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/magic/magic.py
/usr/local/pentos/apps/sqlmap/thirdparty/socks
/usr/local/pentos/apps/sqlmap/thirdparty/socks/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/socks/LICENSE
/usr/local/pentos/apps/sqlmap/thirdparty/socks/socks.py
/usr/local/pentos/apps/sqlmap/thirdparty/bottle
/usr/local/pentos/apps/sqlmap/thirdparty/bottle/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/bottle/bottle.py
/usr/local/pentos/apps/sqlmap/thirdparty/keepalive
/usr/local/pentos/apps/sqlmap/thirdparty/keepalive/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/keepalive/keepalive.py
/usr/local/pentos/apps/sqlmap/thirdparty/pydes
/usr/local/pentos/apps/sqlmap/thirdparty/pydes/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/pydes/pyDes.py
/usr/local/pentos/apps/sqlmap/thirdparty/oset
/usr/local/pentos/apps/sqlmap/thirdparty/oset/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/oset/pyoset.py
/usr/local/pentos/apps/sqlmap/thirdparty/oset/_abc.py
/usr/local/pentos/apps/sqlmap/thirdparty/oset/LICENSE.txt
/usr/local/pentos/apps/sqlmap/thirdparty/clientform
/usr/local/pentos/apps/sqlmap/thirdparty/clientform/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/clientform/clientform.py
/usr/local/pentos/apps/sqlmap/thirdparty/fcrypt
/usr/local/pentos/apps/sqlmap/thirdparty/fcrypt/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/fcrypt/fcrypt.py
/usr/local/pentos/apps/sqlmap/thirdparty/gprof2dot
/usr/local/pentos/apps/sqlmap/thirdparty/gprof2dot/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/gprof2dot/gprof2dot.py
/usr/local/pentos/apps/sqlmap/thirdparty/odict
/usr/local/pentos/apps/sqlmap/thirdparty/odict/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/odict/odict.py
/usr/local/pentos/apps/sqlmap/thirdparty/xdot
/usr/local/pentos/apps/sqlmap/thirdparty/xdot/__init__.py
/usr/local/pentos/apps/sqlmap/thirdparty/xdot/xdot.py
/usr/local/pentos/apps/sqlmap/extra
/usr/local/pentos/apps/sqlmap/extra/__init__.py
/usr/local/pentos/apps/sqlmap/extra/runcmd
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/runcmd
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/runcmd/stdafx.h
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/runcmd/runcmd.cpp
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/runcmd/stdafx.cpp
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/runcmd/runcmd.vcproj
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/README.txt
/usr/local/pentos/apps/sqlmap/extra/runcmd/windows/runcmd.sln
/usr/local/pentos/apps/sqlmap/extra/runcmd/README.txt
/usr/local/pentos/apps/sqlmap/extra/sqlharvest
/usr/local/pentos/apps/sqlmap/extra/sqlharvest/__init__.py
/usr/local/pentos/apps/sqlmap/extra/sqlharvest/sqlharvest.py
/usr/local/pentos/apps/sqlmap/extra/icmpsh
/usr/local/pentos/apps/sqlmap/extra/icmpsh/__init__.py
/usr/local/pentos/apps/sqlmap/extra/icmpsh/icmpsh_m.py
/usr/local/pentos/apps/sqlmap/extra/icmpsh/icmpsh-m.pl
/usr/local/pentos/apps/sqlmap/extra/icmpsh/icmpsh.exe_
/usr/local/pentos/apps/sqlmap/extra/icmpsh/README.txt
/usr/local/pentos/apps/sqlmap/extra/icmpsh/icmpsh-s.c
/usr/local/pentos/apps/sqlmap/extra/icmpsh/icmpsh-m.c
/usr/local/pentos/apps/sqlmap/extra/shutils
/usr/local/pentos/apps/sqlmap/extra/shutils/pyflakes.sh
/usr/local/pentos/apps/sqlmap/extra/shutils/pep8.sh
/usr/local/pentos/apps/sqlmap/extra/shutils/regressiontest.py
/usr/local/pentos/apps/sqlmap/extra/shutils/pylint.py
/usr/local/pentos/apps/sqlmap/extra/shutils/blanks.sh
/usr/local/pentos/apps/sqlmap/extra/shutils/duplicates.py
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec/linux
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec/linux/shellcodeexec.x32_
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec/linux/shellcodeexec.x64_
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec/windows
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec/windows/shellcodeexec.x32.exe_
/usr/local/pentos/apps/sqlmap/extra/shellcodeexec/README.txt
/usr/local/pentos/apps/sqlmap/extra/mssqlsig
/usr/local/pentos/apps/sqlmap/extra/mssqlsig/update.py
/usr/local/pentos/apps/sqlmap/extra/safe2bin
/usr/local/pentos/apps/sqlmap/extra/safe2bin/__init__.py
/usr/local/pentos/apps/sqlmap/extra/safe2bin/README.txt
/usr/local/pentos/apps/sqlmap/extra/safe2bin/safe2bin.py
/usr/local/pentos/apps/sqlmap/extra/dbgtool
/usr/local/pentos/apps/sqlmap/extra/dbgtool/__init__.py
/usr/local/pentos/apps/sqlmap/extra/dbgtool/README.txt
/usr/local/pentos/apps/sqlmap/extra/dbgtool/dbgtool.py
/usr/local/pentos/apps/sqlmap/extra/beep
/usr/local/pentos/apps/sqlmap/extra/beep/__init__.py
/usr/local/pentos/apps/sqlmap/extra/beep/beep.wav
/usr/local/pentos/apps/sqlmap/extra/beep/beep.py
/usr/local/pentos/apps/sqlmap/extra/cloak
/usr/local/pentos/apps/sqlmap/extra/cloak/__init__.py
/usr/local/pentos/apps/sqlmap/extra/cloak/README.txt
/usr/local/pentos/apps/sqlmap/extra/cloak/cloak.py
/usr/local/pentos/apps/sqlmap/xml
/usr/local/pentos/apps/sqlmap/xml/errors.xml
/usr/local/pentos/apps/sqlmap/xml/queries.xml
/usr/local/pentos/apps/sqlmap/xml/payloads
/usr/local/pentos/apps/sqlmap/xml/payloads/stacked_queries.xml
/usr/local/pentos/apps/sqlmap/xml/payloads/boolean_blind.xml
/usr/local/pentos/apps/sqlmap/xml/payloads/inline_query.xml
/usr/local/pentos/apps/sqlmap/xml/payloads/time_blind.xml
/usr/local/pentos/apps/sqlmap/xml/payloads/union_query.xml
/usr/local/pentos/apps/sqlmap/xml/payloads/error_based.xml
/usr/local/pentos/apps/sqlmap/xml/banner
/usr/local/pentos/apps/sqlmap/xml/banner/server.xml
/usr/local/pentos/apps/sqlmap/xml/banner/servlet.xml
/usr/local/pentos/apps/sqlmap/xml/banner/mysql.xml
/usr/local/pentos/apps/sqlmap/xml/banner/mssql.xml
/usr/local/pentos/apps/sqlmap/xml/banner/cookie.xml
/usr/local/pentos/apps/sqlmap/xml/banner/x-aspnet-version.xml
/usr/local/pentos/apps/sqlmap/xml/banner/postgresql.xml
/usr/local/pentos/apps/sqlmap/xml/banner/oracle.xml
/usr/local/pentos/apps/sqlmap/xml/banner/sharepoint.xml
/usr/local/pentos/apps/sqlmap/xml/banner/generic.xml
/usr/local/pentos/apps/sqlmap/xml/banner/x-powered-by.xml
/usr/local/pentos/apps/sqlmap/xml/boundaries.xml
/usr/local/pentos/apps/sqlmap/xml/livetests.xml
/usr/local/pentos/apps/sqlmap/waf
/usr/local/pentos/apps/sqlmap/waf/uspses.py
/usr/local/pentos/apps/sqlmap/waf/urlscan.py
/usr/local/pentos/apps/sqlmap/waf/baidu.py
/usr/local/pentos/apps/sqlmap/waf/__init__.py
/usr/local/pentos/apps/sqlmap/waf/armor.py
/usr/local/pentos/apps/sqlmap/waf/incapsula.py
/usr/local/pentos/apps/sqlmap/waf/wallarm.py
/usr/local/pentos/apps/sqlmap/waf/netscaler.py
/usr/local/pentos/apps/sqlmap/waf/sitelock.py
/usr/local/pentos/apps/sqlmap/waf/nsfocus.py
/usr/local/pentos/apps/sqlmap/waf/sophos.py
/usr/local/pentos/apps/sqlmap/waf/blockdos.py
/usr/local/pentos/apps/sqlmap/waf/edgecast.py
/usr/local/pentos/apps/sqlmap/waf/paloalto.py
/usr/local/pentos/apps/sqlmap/waf/datapower.py
/usr/local/pentos/apps/sqlmap/waf/cloudflare.py
/usr/local/pentos/apps/sqlmap/waf/proventia.py
/usr/local/pentos/apps/sqlmap/waf/sucuri.py
/usr/local/pentos/apps/sqlmap/waf/netcontinuum.py
/usr/local/pentos/apps/sqlmap/waf/cloudfront.py
/usr/local/pentos/apps/sqlmap/waf/yundun.py
/usr/local/pentos/apps/sqlmap/waf/knownsec.py
/usr/local/pentos/apps/sqlmap/waf/teros.py
/usr/local/pentos/apps/sqlmap/waf/stingray.py
/usr/local/pentos/apps/sqlmap/waf/safe3.py
/usr/local/pentos/apps/sqlmap/waf/sonicwall.py
/usr/local/pentos/apps/sqlmap/waf/ciscoacexml.py
/usr/local/pentos/apps/sqlmap/waf/denyall.py
/usr/local/pentos/apps/sqlmap/waf/binarysec.py
/usr/local/pentos/apps/sqlmap/waf/profense.py
/usr/local/pentos/apps/sqlmap/waf/360.py
/usr/local/pentos/apps/sqlmap/waf/requestvalidationmode.py
/usr/local/pentos/apps/sqlmap/waf/jiasule.py
/usr/local/pentos/apps/sqlmap/waf/anquanbao.py
/usr/local/pentos/apps/sqlmap/waf/modsecurity.py
/usr/local/pentos/apps/sqlmap/waf/secureiis.py
/usr/local/pentos/apps/sqlmap/waf/isaserver.py
/usr/local/pentos/apps/sqlmap/waf/barracuda.py
/usr/local/pentos/apps/sqlmap/waf/radware.py
/usr/local/pentos/apps/sqlmap/waf/hyperguard.py
/usr/local/pentos/apps/sqlmap/waf/generic.py
/usr/local/pentos/apps/sqlmap/waf/kona.py
/usr/local/pentos/apps/sqlmap/waf/webappsecure.py
/usr/local/pentos/apps/sqlmap/waf/safedog.py
/usr/local/pentos/apps/sqlmap/waf/webknight.py
/usr/local/pentos/apps/sqlmap/waf/fortiweb.py
/usr/local/pentos/apps/sqlmap/waf/airlock.py
/usr/local/pentos/apps/sqlmap/waf/dotdefender.py
/usr/local/pentos/apps/sqlmap/waf/senginx.py
/usr/local/pentos/apps/sqlmap/waf/expressionengine.py
/usr/local/pentos/apps/sqlmap/waf/newdefend.py
/usr/local/pentos/apps/sqlmap/waf/trafficshield.py
/usr/local/pentos/apps/sqlmap/waf/bigip.py
/usr/local/pentos/apps/sqlmap/waf/comodo.py
/usr/local/pentos/apps/sqlmap/waf/varnish.py
/usr/local/pentos/apps/sqlmap/sqlmap.py
/usr/local/pentos/apps/sqlmap/sqlmap.conf
/usr/local/pentos/apps/sqlmap/tamper
/usr/local/pentos/apps/sqlmap/tamper/nonrecursivereplacement.py
/usr/local/pentos/apps/sqlmap/tamper/unionalltounion.py
/usr/local/pentos/apps/sqlmap/tamper/concat2concatws.py
/usr/local/pentos/apps/sqlmap/tamper/xforwardedfor.py
/usr/local/pentos/apps/sqlmap/tamper/__init__.py
/usr/local/pentos/apps/sqlmap/tamper/unmagicquotes.py
/usr/local/pentos/apps/sqlmap/tamper/halfversionedmorekeywords.py
/usr/local/pentos/apps/sqlmap/tamper/overlongutf8.py
/usr/local/pentos/apps/sqlmap/tamper/versionedmorekeywords.py
/usr/local/pentos/apps/sqlmap/tamper/securesphere.py
/usr/local/pentos/apps/sqlmap/tamper/modsecurityversioned.py
/usr/local/pentos/apps/sqlmap/tamper/modsecurityzeroversioned.py
/usr/local/pentos/apps/sqlmap/tamper/commalessmid.py
/usr/local/pentos/apps/sqlmap/tamper/multiplespaces.py
/usr/local/pentos/apps/sqlmap/tamper/space2mssqlhash.py
/usr/local/pentos/apps/sqlmap/tamper/versionedkeywords.py
/usr/local/pentos/apps/sqlmap/tamper/equaltolike.py
/usr/local/pentos/apps/sqlmap/tamper/ifnull2ifisnull.py
/usr/local/pentos/apps/sqlmap/tamper/escapequotes.py
/usr/local/pentos/apps/sqlmap/tamper/apostrophenullencode.py
/usr/local/pentos/apps/sqlmap/tamper/charencode.py
/usr/local/pentos/apps/sqlmap/tamper/space2dash.py
/usr/local/pentos/apps/sqlmap/tamper/space2mssqlblank.py
/usr/local/pentos/apps/sqlmap/tamper/informationschemacomment.py
/usr/local/pentos/apps/sqlmap/tamper/space2mysqlblank.py
/usr/local/pentos/apps/sqlmap/tamper/between.py
/usr/local/pentos/apps/sqlmap/tamper/appendnullbyte.py
/usr/local/pentos/apps/sqlmap/tamper/chardoubleencode.py
/usr/local/pentos/apps/sqlmap/tamper/greatest.py
/usr/local/pentos/apps/sqlmap/tamper/percentage.py
/usr/local/pentos/apps/sqlmap/tamper/symboliclogical.py
/usr/local/pentos/apps/sqlmap/tamper/space2morehash.py
/usr/local/pentos/apps/sqlmap/tamper/uppercase.py
/usr/local/pentos/apps/sqlmap/tamper/bluecoat.py
/usr/local/pentos/apps/sqlmap/tamper/charunicodeencode.py
/usr/local/pentos/apps/sqlmap/tamper/space2comment.py
/usr/local/pentos/apps/sqlmap/tamper/space2plus.py
/usr/local/pentos/apps/sqlmap/tamper/space2randomblank.py
/usr/local/pentos/apps/sqlmap/tamper/base64encode.py
/usr/local/pentos/apps/sqlmap/tamper/space2mysqldash.py
/usr/local/pentos/apps/sqlmap/tamper/lowercase.py
/usr/local/pentos/apps/sqlmap/tamper/randomcase.py
/usr/local/pentos/apps/sqlmap/tamper/randomcomments.py
/usr/local/pentos/apps/sqlmap/tamper/apostrophemask.py
/usr/local/pentos/apps/sqlmap/tamper/space2hash.py
/usr/local/pentos/apps/sqlmap/tamper/varnish.py
/usr/local/pentos/apps/sqlmap/tamper/commalesslimit.py
/usr/local/pentos/apps/sqlmap/tamper/sp_password.py
/usr/local/pentos/apps/sqlmap/procs
/usr/local/pentos/apps/sqlmap/procs/oracle
/usr/local/pentos/apps/sqlmap/procs/oracle/dns_request.sql
/usr/local/pentos/apps/sqlmap/procs/postgresql
/usr/local/pentos/apps/sqlmap/procs/postgresql/dns_request.sql
/usr/local/pentos/apps/sqlmap/procs/mysql
/usr/local/pentos/apps/sqlmap/procs/mysql/write_file_limit.sql
/usr/local/pentos/apps/sqlmap/procs/mysql/dns_request.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/run_statement_as_user.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/configure_openrowset.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/activate_sp_oacreate.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/configure_xp_cmdshell.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/disable_xp_cmdshell_2000.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/create_new_xp_cmdshell.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/dns_request.sql
/usr/local/pentos/apps/sqlmap/procs/mssqlserver/enable_xp_cmdshell_2000.sql
/usr/local/pentos/apps/sqlmap/procs/README.txt
/usr/local/pentos/apps/sqlmap/README.md
/usr/local/pentos/apps/sqlmap/lib
/usr/local/pentos/apps/sqlmap/lib/techniques
/usr/local/pentos/apps/sqlmap/lib/techniques/__init__.py
/usr/local/pentos/apps/sqlmap/lib/techniques/error
/usr/local/pentos/apps/sqlmap/lib/techniques/error/__init__.py
/usr/local/pentos/apps/sqlmap/lib/techniques/error/use.py
/usr/local/pentos/apps/sqlmap/lib/techniques/union
/usr/local/pentos/apps/sqlmap/lib/techniques/union/__init__.py
/usr/local/pentos/apps/sqlmap/lib/techniques/union/test.py
/usr/local/pentos/apps/sqlmap/lib/techniques/union/use.py
/usr/local/pentos/apps/sqlmap/lib/techniques/brute
/usr/local/pentos/apps/sqlmap/lib/techniques/brute/__init__.py
/usr/local/pentos/apps/sqlmap/lib/techniques/brute/use.py
/usr/local/pentos/apps/sqlmap/lib/techniques/dns
/usr/local/pentos/apps/sqlmap/lib/techniques/dns/__init__.py
/usr/local/pentos/apps/sqlmap/lib/techniques/dns/test.py
/usr/local/pentos/apps/sqlmap/lib/techniques/dns/use.py
/usr/local/pentos/apps/sqlmap/lib/techniques/blind
/usr/local/pentos/apps/sqlmap/lib/techniques/blind/__init__.py
/usr/local/pentos/apps/sqlmap/lib/techniques/blind/inference.py
/usr/local/pentos/apps/sqlmap/lib/__init__.py
/usr/local/pentos/apps/sqlmap/lib/parse
/usr/local/pentos/apps/sqlmap/lib/parse/__init__.py
/usr/local/pentos/apps/sqlmap/lib/parse/configfile.py
/usr/local/pentos/apps/sqlmap/lib/parse/sitemap.py
/usr/local/pentos/apps/sqlmap/lib/parse/handler.py
/usr/local/pentos/apps/sqlmap/lib/parse/banner.py
/usr/local/pentos/apps/sqlmap/lib/parse/cmdline.py
/usr/local/pentos/apps/sqlmap/lib/parse/payloads.py
/usr/local/pentos/apps/sqlmap/lib/parse/html.py
/usr/local/pentos/apps/sqlmap/lib/parse/headers.py
/usr/local/pentos/apps/sqlmap/lib/controller
/usr/local/pentos/apps/sqlmap/lib/controller/__init__.py
/usr/local/pentos/apps/sqlmap/lib/controller/checks.py
/usr/local/pentos/apps/sqlmap/lib/controller/handler.py
/usr/local/pentos/apps/sqlmap/lib/controller/action.py
/usr/local/pentos/apps/sqlmap/lib/controller/controller.py
/usr/local/pentos/apps/sqlmap/lib/takeover
/usr/local/pentos/apps/sqlmap/lib/takeover/udf.py
/usr/local/pentos/apps/sqlmap/lib/takeover/__init__.py
/usr/local/pentos/apps/sqlmap/lib/takeover/icmpsh.py
/usr/local/pentos/apps/sqlmap/lib/takeover/abstraction.py
/usr/local/pentos/apps/sqlmap/lib/takeover/registry.py
/usr/local/pentos/apps/sqlmap/lib/takeover/metasploit.py
/usr/local/pentos/apps/sqlmap/lib/takeover/web.py
/usr/local/pentos/apps/sqlmap/lib/takeover/xp_cmdshell.py
/usr/local/pentos/apps/sqlmap/lib/core
/usr/local/pentos/apps/sqlmap/lib/core/__init__.py
/usr/local/pentos/apps/sqlmap/lib/core/session.py
/usr/local/pentos/apps/sqlmap/lib/core/testing.py
/usr/local/pentos/apps/sqlmap/lib/core/target.py
/usr/local/pentos/apps/sqlmap/lib/core/wordlist.py
/usr/local/pentos/apps/sqlmap/lib/core/convert.py
/usr/local/pentos/apps/sqlmap/lib/core/profiling.py
/usr/local/pentos/apps/sqlmap/lib/core/bigarray.py
/usr/local/pentos/apps/sqlmap/lib/core/dicts.py
/usr/local/pentos/apps/sqlmap/lib/core/dump.py
/usr/local/pentos/apps/sqlmap/lib/core/common.py
/usr/local/pentos/apps/sqlmap/lib/core/readlineng.py
/usr/local/pentos/apps/sqlmap/lib/core/option.py
/usr/local/pentos/apps/sqlmap/lib/core/agent.py
/usr/local/pentos/apps/sqlmap/lib/core/log.py
/usr/local/pentos/apps/sqlmap/lib/core/settings.py
/usr/local/pentos/apps/sqlmap/lib/core/update.py
/usr/local/pentos/apps/sqlmap/lib/core/subprocessng.py
/usr/local/pentos/apps/sqlmap/lib/core/datatype.py
/usr/local/pentos/apps/sqlmap/lib/core/threads.py
/usr/local/pentos/apps/sqlmap/lib/core/revision.py
/usr/local/pentos/apps/sqlmap/lib/core/optiondict.py
/usr/local/pentos/apps/sqlmap/lib/core/data.py
/usr/local/pentos/apps/sqlmap/lib/core/defaults.py
/usr/local/pentos/apps/sqlmap/lib/core/enums.py
/usr/local/pentos/apps/sqlmap/lib/core/unescaper.py
/usr/local/pentos/apps/sqlmap/lib/core/replication.py
/usr/local/pentos/apps/sqlmap/lib/core/decorators.py
/usr/local/pentos/apps/sqlmap/lib/core/shell.py
/usr/local/pentos/apps/sqlmap/lib/core/exception.py
/usr/local/pentos/apps/sqlmap/lib/utils
/usr/local/pentos/apps/sqlmap/lib/utils/api.py
/usr/local/pentos/apps/sqlmap/lib/utils/xrange.py
/usr/local/pentos/apps/sqlmap/lib/utils/__init__.py
/usr/local/pentos/apps/sqlmap/lib/utils/sqlalchemy.py
/usr/local/pentos/apps/sqlmap/lib/utils/deps.py
/usr/local/pentos/apps/sqlmap/lib/utils/pivotdumptable.py
/usr/local/pentos/apps/sqlmap/lib/utils/getch.py
/usr/local/pentos/apps/sqlmap/lib/utils/purge.py
/usr/local/pentos/apps/sqlmap/lib/utils/search.py
/usr/local/pentos/apps/sqlmap/lib/utils/timeout.py
/usr/local/pentos/apps/sqlmap/lib/utils/hashdb.py
/usr/local/pentos/apps/sqlmap/lib/utils/crawler.py
/usr/local/pentos/apps/sqlmap/lib/utils/progress.py
/usr/local/pentos/apps/sqlmap/lib/utils/hash.py
/usr/local/pentos/apps/sqlmap/lib/utils/htmlentities.py
/usr/local/pentos/apps/sqlmap/lib/utils/versioncheck.py
/usr/local/pentos/apps/sqlmap/lib/request
/usr/local/pentos/apps/sqlmap/lib/request/rangehandler.py
/usr/local/pentos/apps/sqlmap/lib/request/__init__.py
/usr/local/pentos/apps/sqlmap/lib/request/redirecthandler.py
/usr/local/pentos/apps/sqlmap/lib/request/methodrequest.py
/usr/local/pentos/apps/sqlmap/lib/request/connect.py
/usr/local/pentos/apps/sqlmap/lib/request/basicauthhandler.py
/usr/local/pentos/apps/sqlmap/lib/request/inject.py
/usr/local/pentos/apps/sqlmap/lib/request/basic.py
/usr/local/pentos/apps/sqlmap/lib/request/dns.py
/usr/local/pentos/apps/sqlmap/lib/request/templates.py
/usr/local/pentos/apps/sqlmap/lib/request/pkihandler.py
/usr/local/pentos/apps/sqlmap/lib/request/direct.py
/usr/local/pentos/apps/sqlmap/lib/request/httpshandler.py
/usr/local/pentos/apps/sqlmap/lib/request/comparison.py
/usr/local/pentos/apps/sqlmap/doc
/usr/local/pentos/apps/sqlmap/doc/THIRD-PARTY.md
/usr/local/pentos/apps/sqlmap/doc/AUTHORS
/usr/local/pentos/apps/sqlmap/doc/THANKS.md
/usr/local/pentos/apps/sqlmap/doc/FAQ.pdf
/usr/local/pentos/apps/sqlmap/doc/COPYING
/usr/local/pentos/apps/sqlmap/doc/CHANGELOG.md
/usr/local/pentos/apps/sqlmap/doc/translations
/usr/local/pentos/apps/sqlmap/doc/translations/README-es-MX.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-id-ID.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-zh-CN.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-gr-GR.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-hr-HR.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-ja-JP.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-pt-BR.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-tr-TR.md
/usr/local/pentos/apps/sqlmap/doc/translations/README-fr-FR.md
/usr/local/pentos/apps/sqlmap/doc/README.pdf
/usr/local/pentos/apps/sqlmap/doc/CONTRIBUTING.md
/usr/local/pentos/apps/sqlmap/shell
/usr/local/pentos/apps/sqlmap/shell/stager.asp_
/usr/local/pentos/apps/sqlmap/shell/backdoor.jsp_
/usr/local/pentos/apps/sqlmap/shell/backdoor.aspx_
/usr/local/pentos/apps/sqlmap/shell/stager.php_
/usr/local/pentos/apps/sqlmap/shell/backdoor.asp_
/usr/local/pentos/apps/sqlmap/shell/README.txt
/usr/local/pentos/apps/sqlmap/shell/stager.aspx_
/usr/local/pentos/apps/sqlmap/shell/backdoor.php_
/usr/local/pentos/apps/sqlmap/shell/stager.jsp_
/usr/local/pentos/apps/sqlmap/shell/runcmd.exe_

%changelog
