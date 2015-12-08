sed -i -e 's/^PRELINKING=.*/PRELINKING=no/' /etc/sysconfig/prelink

/usr/sbin/prelink -ua
