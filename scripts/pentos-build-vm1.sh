cd /opt
yum -y install yum-plugin-priorities
wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
rpm -K rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
rpm -i rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
yum -y --enablerepo rpmforge install dkms	

# In the "[hostname][Running] - Oracle VM VirtualBox" window,
#	select: Devices > Insert Guest Additions CD image

# In the "VOBXADDITIONS_5.0.10_104061" dialog,
#	select: Open Autorun Prompt
#	select: OK

# In the "VOBXADDITIONS_5.0.10_104061" dialog,
#	select: Run

# In the "Authenticate" dialog,
#	enter the password for root
#	Select: Authenticate

# workaround for above failure
mkdir /tmp/vbox
cp -rp /media/VBOXADDITIONS_5.0.10_104061/* /tmp/vbox
ln -s /usr/src/kernels/2.6.32-573.8.1.el6.x86_64 /usr/src/kernels/2.6.32-431.el6.x86_64
cd /tmp/vbox
./VBoxLinuxAdditions.run

# shared folder (optional)
mkdir /mnt/host
mount -t vboxsf host /mnt/host

