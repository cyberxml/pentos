# OWASP Zed Attack Proxy 

cd /opt
wget https://github.com/zaproxy/zaproxy/releases/download/2.4.3/ZAP_2.4.3_Linux.tar.gz

tar xzf ZAP_2.4.3_Linux.tar.gz
rm ZAP_2.4.3_Linux.tar.gz

echo "pathmunge /opt/ZAP_2.4.3" > /etc/profile.d/pentos-zap.sh
