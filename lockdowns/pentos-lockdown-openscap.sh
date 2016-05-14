
cp /opt/pentos/lockdowns/fiiles/ssg-centos6-* /usr/share/xml/scap/ssg

oscap xccdf eval --remediate --profile server \
 --cpe /usr/share/xml/scap/ssg/content/ssg-centos6-cpe-dictionary.xml \
 /usr/share/xml/scap/ssg/content/ssg-rhel6-xccdf.xml

