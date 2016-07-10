# Latest Metasploitable-Framework

cd /opt
rm -f metasploit-framework*rpm

base=`wget -qO- http://rpm.metasploit.com/ | grep metasploit-framework | tail -1 | cut -d'"' -f2`

rpm=`echo $base | cut -d'/' -f4`

rpmurl=https://rpm.metasploit.com/${base}

wget --no-check-certificate ${rpmurl}

rpm -ivh --replacefiles metasploit-framework*rpm

chgrp -hR pentester /opt/metasploit-framework/bin

echo "pathmunge /opt/metasploit-framework/bin" > /etc/profile.d/pentos-metasploit.sh


