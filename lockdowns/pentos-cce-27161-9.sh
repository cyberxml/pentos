grep -q ^NETWORKING_IPV6 /etc/sysconfig/network && \
  sed -i "s/NETWORKING_IPV6.*/NETWORKING_IPV6=no/g" /etc/sysconfig/network
if ! [ $? -eq 0 ]; then
    echo "NETWORKING_IPV6=no" >> /etc/sysconfig/network
fi

grep -q ^IPV6INIT /etc/sysconfig/network && \
  sed -i "s/IPV6INIT.*/IPV6INIT=no/g" /etc/sysconfig/network
if ! [ $? -eq 0 ]; then
    echo "IPV6INIT=no" >> /etc/sysconfig/network
fi
