cd /opt
wget https://forensics.cert.org/cert-forensics-tools-release-el7.rpm
rpm -ivh cert-forensics-tools-release-el7.rpm
yum -y update
yum -y install --disablerepo=\* --enablerepo=cert-forensics install \*
