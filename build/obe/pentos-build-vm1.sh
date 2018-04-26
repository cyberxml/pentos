cd /opt/pentos/apps
#yum -y install kernel-headers
yum -y install yum-plugin-priorities
wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
rpm -K rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
rpm -i rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
yum -y --enablerepo rpmforge install dkms

echo From the "Oracle VM VirtualBox" winodw, select: Devices > Insert Guest Additions CD
echo ... and run the installation

