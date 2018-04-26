grep -q ^NOZEROCONF /etc/sysconfig/network && \
  sed -i "s/NOZEROCONF.*/NOZEROCONF=yes/g" /etc/sysconfig/network
if ! [ $? -eq 0 ]; then
    echo "NOZEROCONF=yes" >> /etc/sysconfig/network
fi
