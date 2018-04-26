sed -i -e 's@^SELINUX=.*$@SELINUX=disabled@' /etc/selinux/config
echo you must reboot the system to complete the selinux configuration
