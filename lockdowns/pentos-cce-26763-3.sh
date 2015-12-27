# Add the following to the appropriate /etc/modprobe.d configuration file to prevent the loading of the Bluetooth module: 
echo "install net-pf-31 /bin/false" >> /etc/modprobe.d/disabled.conf
echo "install bluetooth /bin/false" >> /etc/modprobe.d/disabled.conf
