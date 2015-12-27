# 
grep -v " hard maxlogins " /etc/security/limits.conf > /tmp/limits.conf
cp -f /tmp/limits.conf /etc/security/limits.conf
rm /tmp/limits.conf
echo "* hard maxlogins 10" >> /etc/security/limits.conf
