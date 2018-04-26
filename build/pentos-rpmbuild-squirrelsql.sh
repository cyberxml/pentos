# Squirrel SQL - database browswer
release=3.7

# cleanup
rm -rf /opt/pentos/rpmbuild/SOURCES/*squirrelsql*

# prepare source
cd /opt/pentos/rpmbuild/SOURCES
mkdir /opt/pentos/rpmbuild/SOURCES/pentos-squirrelsql-${release}
cd /opt/pentos/rpmbuild/SOURCES/pentos-squirrelsql-${release}
wget http://downloads.sourceforge.net/project/squirrel-sql/1-stable/${release}.0/squirrel-sql-${release}-standard.jar
echo java -jar /usr/local/pentos/apps/squirrelsql/squirrel-sql-${release}-standard.jar > squirrelsql.sh
chmod 755 squirrelsql.sh
cd /opt/pentos/rpmbuild/SOURCES
tar -czf pentos-squirrelsql-${release}.tar.gz pentos-squirrelsql-${release}

# create rpm
cd /opt/pentos
rpmbuild -ba rpmbuild/SPECS/pentos-squirrelsql.spec

# show result
ls -l /opt/pentos/rpmbuild/RPMS/x86_64/*squirrelsql*

