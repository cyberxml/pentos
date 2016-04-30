# Latest Metasploitable-Framework

cd /opt
pwd

base=`wget -qO- http://rpm.metasploit.com/ | grep metasploit-framework | tail -1 | cut -d'"' -f2`

rpm=`echo $base | cut -d'/' -f4`

rpmurl=https://rpm.metasploit.com/${base}
echo ${rpmurl}
pwd
wget --no-check-certificate ${rpmurl}

rpm -ivh ${rpm}
pwd
